

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchArtifactsByContentRequestOrderby(enum.StrEnum):
    NAME = "name"
    CREATED_ON = "createdOn"

    def visit(self, name: typing.Callable[[], T_Result], created_on: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchArtifactsByContentRequestOrderby.NAME:
            return name()
        if self is SearchArtifactsByContentRequestOrderby.CREATED_ON:
            return created_on()
