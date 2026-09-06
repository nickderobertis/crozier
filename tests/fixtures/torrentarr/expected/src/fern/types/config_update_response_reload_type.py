

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfigUpdateResponseReloadType(enum.StrEnum):
    """
    Reload strategy applied after saving config changes.
    """

    NONE = "none"
    FRONTEND = "frontend"
    LIVE = "live"
    QBIT_HOT = "qbit_hot"
    WEBUI = "webui"
    SINGLE_ARR = "single_arr"
    MULTI_ARR = "multi_arr"
    FULL = "full"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        frontend: typing.Callable[[], T_Result],
        live: typing.Callable[[], T_Result],
        qbit_hot: typing.Callable[[], T_Result],
        webui: typing.Callable[[], T_Result],
        single_arr: typing.Callable[[], T_Result],
        multi_arr: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfigUpdateResponseReloadType.NONE:
            return none()
        if self is ConfigUpdateResponseReloadType.FRONTEND:
            return frontend()
        if self is ConfigUpdateResponseReloadType.LIVE:
            return live()
        if self is ConfigUpdateResponseReloadType.QBIT_HOT:
            return qbit_hot()
        if self is ConfigUpdateResponseReloadType.WEBUI:
            return webui()
        if self is ConfigUpdateResponseReloadType.SINGLE_ARR:
            return single_arr()
        if self is ConfigUpdateResponseReloadType.MULTI_ARR:
            return multi_arr()
        if self is ConfigUpdateResponseReloadType.FULL:
            return full()
