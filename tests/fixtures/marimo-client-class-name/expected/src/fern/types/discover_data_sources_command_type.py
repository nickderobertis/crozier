

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DiscoverDataSourcesCommandType(enum.StrEnum):
    DISCOVER_DATA_SOURCES = "discover-data-sources"

    def visit(self, discover_data_sources: typing.Callable[[], T_Result]) -> T_Result:
        if self is DiscoverDataSourcesCommandType.DISCOVER_DATA_SOURCES:
            return discover_data_sources()
