

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DfuStateMode(enum.StrEnum):
    """
    * "idle"          - nothing downloading or downloaded
    * "error"         - halted and in the error state
    * "downloading"   - transferring data from cloud to module
    * "sideloading"   - transferring data via request to module
    * "ready"         - DFU data is ready/verified and waiting on external storage
    * "ready-retry"   - DFU data is ready/verified and retrying
    * "updating"      - currently updating
    * "completed"     - DFU is done successfully
    """

    IDLE = "idle"
    ERROR = "error"
    DOWNLOADING = "downloading"
    SIDELOADING = "sideloading"
    READY = "ready"
    READY_RETRY = "ready-retry"
    UPDATING = "updating"
    COMPLETED = "completed"

    def visit(
        self,
        idle: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        downloading: typing.Callable[[], T_Result],
        sideloading: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        ready_retry: typing.Callable[[], T_Result],
        updating: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DfuStateMode.IDLE:
            return idle()
        if self is DfuStateMode.ERROR:
            return error()
        if self is DfuStateMode.DOWNLOADING:
            return downloading()
        if self is DfuStateMode.SIDELOADING:
            return sideloading()
        if self is DfuStateMode.READY:
            return ready()
        if self is DfuStateMode.READY_RETRY:
            return ready_retry()
        if self is DfuStateMode.UPDATING:
            return updating()
        if self is DfuStateMode.COMPLETED:
            return completed()
