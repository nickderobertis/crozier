

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GameRecordSource(enum.StrEnum):
    ONLINE_ROOM = "online_room"
    LOCAL_APP = "local_app"
    IMPORT = "import"
    CSA_RELAY = "csa_relay"

    def visit(
        self,
        online_room: typing.Callable[[], T_Result],
        local_app: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
        csa_relay: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameRecordSource.ONLINE_ROOM:
            return online_room()
        if self is GameRecordSource.LOCAL_APP:
            return local_app()
        if self is GameRecordSource.IMPORT:
            return import_()
        if self is GameRecordSource.CSA_RELAY:
            return csa_relay()
