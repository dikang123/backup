# noinspection PyPackageRequirements
import mock
# noinspection PyPackageRequirements
import pytest

from twindb_backup import INTERVALS
from twindb_backup.source.mysql_source import MySQLConnectInfo
from twindb_backup.source.remote_mysql_source import RemoteMySQLSource


@pytest.mark.parametrize('dest, port', [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4)
])
def test_clone(dest, port):
    arg = 'bash -c "sudo innobackupex --stream=xbstream ./ ' \
          '| gzip -c - | nc %s %d"' \
          % (dest, port)
    mock_client = mock.Mock()
    rmt_sql = RemoteMySQLSource({
        "run_type": INTERVALS[0],
        "full_backup": INTERVALS[0],
        "mysql_connect_info": MySQLConnectInfo("/"),
        "ssh_connection_info": None
    })
    rmt_sql._ssh_client = mock_client
    rmt_sql.clone(dest, port)
    mock_client.execute.assert_called_with(arg)
