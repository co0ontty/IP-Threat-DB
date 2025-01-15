# IP-Threat-DB

IP-Threat-DB is a project for automatically generating SafePoint malicious IP threat intelligence databases. The project collects, collates, and analyzes malicious IP address data to provide strong support for network security.

- Automatically collect malicious IP address data
- Generate threat intelligence database
- Provide API interface for other systems to call

## Automatic Update

This repository runs automatically every day and publishes the database to the release automatically, everyone can use it at will.

## CLI

Clone the repository:

```bash
git clone https://github.com/username/IP-Threat-DB.git
cd IP-Threat-DB

python3 cli.py
```

then

```
(IPDB) > 1.2.3.4
1.2.3.4 => UNKNOWN
(IPDB) > 35.203.210.243
35.203.210.243 => LIGHT_MALICIOUS
```

## How To Use

```python
from ipdb import IPDB

db = IPDB()
db.load('./ip-threat.db')

db.get(b'1.1.1.1')
```

