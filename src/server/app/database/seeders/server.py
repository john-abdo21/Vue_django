from app.models import Server
from constants import ServerStatus


def exec():
    servers = [
        Server(
            description="テストサーバー1",
            ip_address="192.168.2.11",
            host_name="test-server1",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー2",
            ip_address="192.168.2.12",
            host_name="test-server2",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー3",
            ip_address="192.168.2.13",
            host_name="test-server3",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー4",
            ip_address="192.168.2.14",
            host_name="test-server4",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー5",
            ip_address="192.168.2.15",
            host_name="test-server5",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー6",
            ip_address="192.168.2.16",
            host_name="test-server6",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー6",
            ip_address="192.168.2.16",
            host_name="test-server6",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー7",
            ip_address="192.168.2.17",
            host_name="test-server7",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー8",
            ip_address="192.168.2.18",
            host_name="test-server8",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー9",
            ip_address="192.168.2.19",
            host_name="test-server9",
            status=ServerStatus.UNCONFIRMED,
        ),
        Server(
            description="テストサーバー10",
            ip_address="192.168.2.20",
            host_name="test-server10",
            status=ServerStatus.UNCONFIRMED,
        ),
    ]

    Server.objects.bulk_create(servers)
