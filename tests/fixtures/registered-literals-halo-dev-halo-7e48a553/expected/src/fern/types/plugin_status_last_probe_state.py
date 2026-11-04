

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PluginStatusLastProbeState(enum.StrEnum):
    """
    Last PF4J probe state observed for the plugin.
    """

    CREATED = "CREATED"
    DISABLED = "DISABLED"
    RESOLVED = "RESOLVED"
    STARTED = "STARTED"
    STOPPED = "STOPPED"
    FAILED = "FAILED"
    UNLOADED = "UNLOADED"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        unloaded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PluginStatusLastProbeState.CREATED:
            return created()
        if self is PluginStatusLastProbeState.DISABLED:
            return disabled()
        if self is PluginStatusLastProbeState.RESOLVED:
            return resolved()
        if self is PluginStatusLastProbeState.STARTED:
            return started()
        if self is PluginStatusLastProbeState.STOPPED:
            return stopped()
        if self is PluginStatusLastProbeState.FAILED:
            return failed()
        if self is PluginStatusLastProbeState.UNLOADED:
            return unloaded()
