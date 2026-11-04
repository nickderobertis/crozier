

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationStoreInfoHistoryRequestStoreType(enum.StrEnum):
    APPSTORE = "appstore"
    GOOGLEPLAY = "googleplay"

    def visit(self, appstore: typing.Callable[[], T_Result], googleplay: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApplicationStoreInfoHistoryRequestStoreType.APPSTORE:
            return appstore()
        if self is ApplicationStoreInfoHistoryRequestStoreType.GOOGLEPLAY:
            return googleplay()
