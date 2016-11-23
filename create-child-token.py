#!/usr/bin/env python

"""create-child-token.py
Creates a child token for the given secret key

Usage:
    create-child-token.py [--policy=POLICY] [--lease=LEASE]

Options:
    --policy=POLICY                  the policy that the child token should be created for
    --lease=LEASE
"""

import config
import hvac

from docopt import docopt

if __name__ == "__main__":
    args = docopt(__doc__)

    config = config.load_config()

    client = hvac.Client(url=config['vault_url'], token=config['token'])

    if args['--lease']:
        lease = args['--lease']
    else:
        lease = "30m"

    if args['--policy']:
        policies = []
        policies.append(args['--policy'])
        child_token = client.create_token(policies=policies, lease=lease)
    else:
        child_token = client.create_token(lease=lease)

    print child_token['auth']['client_token']
