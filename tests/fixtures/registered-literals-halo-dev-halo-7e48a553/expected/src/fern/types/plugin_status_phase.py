

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PluginStatusPhase(enum.StrEnum):
    """
    Current plugin lifecycle phase.
    """

    PENDING = "PENDING"
    STARTING = "STARTING"
    CREATED = "CREATED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    RESOLVED = "RESOLVED"
    STARTED = "STARTED"
    STOPPED = "STOPPED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        created: typing.Callable[[], T_Result],
        disabling: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PluginStatusPhase.PENDING:
            return pending()
        if self is PluginStatusPhase.STARTING:
            return starting()
        if self is PluginStatusPhase.CREATED:
            return created()
        if self is PluginStatusPhase.DISABLING:
            return disabling()
        if self is PluginStatusPhase.DISABLED:
            return disabled()
        if self is PluginStatusPhase.RESOLVED:
            return resolved()
        if self is PluginStatusPhase.STARTED:
            return started()
        if self is PluginStatusPhase.STOPPED:
            return stopped()
        if self is PluginStatusPhase.FAILED:
            return failed()
        if self is PluginStatusPhase.UNKNOWN:
            return unknown()
