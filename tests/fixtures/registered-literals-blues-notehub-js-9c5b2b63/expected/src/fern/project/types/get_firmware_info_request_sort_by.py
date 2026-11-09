

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFirmwareInfoRequestSortBy(enum.StrEnum):
    CREATED = "created"
    NAME = "name"
    VERSION = "version"
    LENGTH = "length"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        version: typing.Callable[[], T_Result],
        length: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFirmwareInfoRequestSortBy.CREATED:
            return created()
        if self is GetFirmwareInfoRequestSortBy.NAME:
            return name()
        if self is GetFirmwareInfoRequestSortBy.VERSION:
            return version()
        if self is GetFirmwareInfoRequestSortBy.LENGTH:
            return length()
