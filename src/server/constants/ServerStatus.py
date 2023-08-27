from .base import Constant


class ServerStatus(Constant):
    INACTIVE: str = "0"
    ACTIVE: str = "1"
    UNCONFIRMED: str = "2"
