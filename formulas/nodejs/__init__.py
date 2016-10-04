from hereby import Here
from pyinfra import host
from pyinfra.modules import files, apt

here = Here(__file__)


def nodejs_6():
    '''
    Ensure that the Node.js Javascript runtime is installed in version 6.x.
    (Ubuntu 16.04 provides an older version)
    '''

    files.put(
        here.abspath('files/pubkey.gpg'),
        '/opt/nodesource.gpg',
    )
    apt.key(
        '/opt/nodesource.gpg',
    )

    # if host.fact.linux_distribution == {
    #         'major': '16',
    #         'name': 'Ubuntu',
    #         'minor': '04'}:
    DISTRIB_CODENAME = 'xenial'

    if apt.repo(
        'deb https://deb.nodesource.com/node_6.x {} main'
            .format(DISTRIB_CODENAME),
        present=True,
        filename='node_6',
    ).changed:
        apt.update()

    apt.packages(
        ['nodejs>=6'],
    )
