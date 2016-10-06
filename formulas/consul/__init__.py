from pyinfra import host
from pyinfra.modules import server, files, apt


def consul_present():
    '''
    Ensure that Consul is installed.
    '''
    version = '0.7.0'
    files.download(
        'https://releases.hashicorp.com/consul/{}/consul_{}_linux_amd64.zip'
        .format(version, version),
        '/opt/consul_{}_linux_amd64.zip'.format(version)
    )
    files.download(
        'https://releases.hashicorp.com/consul/{}/consul_{}_SHA256SUMS'
        .format(version, version),
        '/opt/consul_{}_SHA256SUMS'.format(version)
    )

    apt.packages(['unzip'])

    if not host.fact.file('/opt/consul'):
        server.shell(
            'unzip /opt/consul_{}_linux_amd64.zip'.format(version),
            chdir='/opt',
        )
