# pyinfra-formulas

*This project has just started, and is work in progress.*

Collection of pre-written [Pyinfra](https://github.com/Fizzadar/pyinfra) modules for common use cases. They are open-ended and can be used for tasks such as installing and configuring a software.

The motivation behind this project is to fill the gap between [modules](https://pyinfra.readthedocs.io/en/latest/modules.html) and [roles](https://pyinfra.readthedocs.io/en/latest/building_a_deploy.html#includes-roles): roles would not have to detail how a functionality is implemented and could use a level of abstraction above the exact modules required.

# Installation

`pip install pyinfra-formulas`

# Usage

Here is simple deploy file to illustrate how you can use a formula (assuming you have a folder named `example_org_files` containing your website and the DNS configured).
```python
from formulas.nginx import synced_website

synced_website(
    'www.example.org',
    'example_org_files',
)
```

Do deploy the website, just run:
```bash
pyinfra -i $MY_SERVER_IP deploy.py
```
