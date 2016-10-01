'''
Formulas for serving websites or web apps via Nginx.
'''

from hereby import Here
from pyinfra.modules import server, files, apt, init

here = Here(__file__)


def _deploy_user(name='deploy', group='deploy'):
    '''
    Configure a user to own files served by Nginx.

    + name: username
    + group: name of the group
    '''
    if not group:
        server.user(
            name,
            ensure_home=True,
        )
    else:
        server.group(
            group,
        )

        server.user(
            name,
            group=group,
            ensure_home=True,
        )
    return name, group


def static_website(name, directory):
    '''
    Configure Nginx to serve the files in `directory`.

    + name: domain name used to serve the files
    + directory: path to sync files from
    '''
    apt.packages(
        ['nginx'],
    )

    user, group = _deploy_user()

    files.directory(
        '/srv/web',
        user=user,
        group=group,
    )

    files.directory(
        '/srv/web/{}/'.format(name),
        user=user,
        group=group,
    )
    files.sync(
        'files/web/{}/'.format(name),
        '/srv/web/{}/'.format(name),
        user=user,
        group=group,
        # delete=True,
    )

    if files.template(
        here.abspath('files/static_website.nginx'),
        '/etc/nginx/sites-enabled/{}'.format(name),
        name=name,
    ).changed:
        init.systemd(
            'nginx',
            reloaded=True,
        )


def proxy(name, target):
    '''
    Configure Nginx to proxy requests to another HTTP server.

    + name: domain name used to serve the files
    + target: URL of the target to forward requests to
    '''
    apt.packages(
        ['nginx'],
    )

    if files.template(
        here.abspath('files/proxy.nginx'),
        '/etc/nginx/sites-enabled/{}'.format(name),
        name=name,
        target=target,
    ).changed:
        init.systemd(
            'nginx',
            reloaded=True,
        )
