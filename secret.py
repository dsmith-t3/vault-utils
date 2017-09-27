#!/usr/bin/env python

"""secret.py
Creates a child token for the given secret key

Usage:
    secret.py --key=KEY [--value=VALUE] [--delete] [--token=VALUE]

Options:
    --key=KEY      the secret key
    --value=VALUE  the secret value
    --delete       delete a secret
    --token=VALUE  optional token to use instead of from the config file
"""

import config
import hvac
import os

from docopt import docopt

if __name__ == "__main__":
    args = docopt(__doc__)
    config = config.load_config()
    token = args['--token'] or config['token']
    client = hvac.Client(url=config['vault_url'], token=token)
    secret_key = "secret/" + args['--key']
    check = False
    if args['--delete']:
        client.delete(secret_key)
    elif args['--value']:
        if os.path.isfile(args['--value']):
            with open(args['--value']) as f:
                args['--value'] = f.read()
        check = True
        client.write(secret_key, value=args['--value'])
    response = client.read(secret_key)
    print response
    if check and response['data']['value'] != args['--value']:
        raise Exception("secret can not be retrieved from vault")
