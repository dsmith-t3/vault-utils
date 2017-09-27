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
    lease = args['--lease'] or '30m'
    policies = [args['--policy']] if args['--policy'] else None
    config = config.load_config()
    client = hvac.Client(url=config['vault_url'], token=config['token'])
    print client.create_token(policies=policies, lease=lease)
