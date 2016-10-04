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


def static_website(name, path):
    '''
    Configure Nginx to serve files in server `path`.

    + name: domain name used to serve the files
    + path: path on the server where files are located
    '''
    apt.packages(
        ['nginx'],
    )

    if files.template(
        here.abspath('files/static_website.nginx'),
        '/etc/nginx/sites-enabled/{}'.format(name),
        name=name,
        path=path,
    ).changed:
        init.systemd(
            'nginx',
            reloaded=True,
        )


def synced_website(name, directory):
    '''
    Configure Nginx to serve the files in local `directory`.

    + name: domain name used to serve the files
    + directory: path to sync files from
    '''
    path = '/srv/web/{}/'.format(name)
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
        directory,
        path,
        user=user,
        group=group,
        # delete=True,
    )

    static_website(name, path)


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
