# Installation

1. install virtualenv
2. create and activate a virtualenv
3. install python requirements

# Configuration

1. `cp config.yml.example config.yml`
2. update `vault_url` and `token` in `config.yml`


# Example

```
$ cp config.yml.example config.yml
$ vi config.yml
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./secret.py --key=abc/def [--value=123]
$ deactivate
```