

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataSourceDiscoveryResultNotificationOp(enum.StrEnum):
    DATA_SOURCE_DISCOVERY_RESULT = "data-source-discovery-result"

    def visit(self, data_source_discovery_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataSourceDiscoveryResultNotificationOp.DATA_SOURCE_DISCOVERY_RESULT:
            return data_source_discovery_result()
