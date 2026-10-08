

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectV1ConnectorExpansionStatusConnectorState(enum.StrEnum):
    """
    The state of the connector.
    """

    NONE = "NONE"
    PROVISIONING = "PROVISIONING"
    RUNNING = "RUNNING"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    PAUSED = "PAUSED"
    DELETED = "DELETED"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        provisioning: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectV1ConnectorExpansionStatusConnectorState.NONE:
            return none()
        if self is ConnectV1ConnectorExpansionStatusConnectorState.PROVISIONING:
            return provisioning()
        if self is ConnectV1ConnectorExpansionStatusConnectorState.RUNNING:
            return running()
        if self is ConnectV1ConnectorExpansionStatusConnectorState.DEGRADED:
            return degraded()
        if self is ConnectV1ConnectorExpansionStatusConnectorState.FAILED:
            return failed()
        if self is ConnectV1ConnectorExpansionStatusConnectorState.PAUSED:
            return paused()
        if self is ConnectV1ConnectorExpansionStatusConnectorState.DELETED:
            return deleted()
