# pyinfra-formulas

*This project has just started, and is work in progress.*

Collection of pre-written [Pyinfra](https://github.com/Fizzadar/pyinfra) modules for common use cases. They are open-ended and can be used for tasks such as installing and configuring a software.

The motivation behind this project is to fill the gap between [modules](https://pyinfra.readthedocs.io/en/latest/modules.html) and [roles](https://pyinfra.readthedocs.io/en/latest/building_a_deploy.html#includes-roles): roles would not have to detail how a functionality is implemented and could use a level of abstraction above the exact modules required.

# Installation

`pip install git+https://github.com/hoh/pyinfra-formulas.git`

# Usage

Here is simple deploy file to illustrate how you can use a formula:
```python
from formulas.nginx import static_website

static_website(
    'www.example.org',
    'example_org_files',
)
```
