

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetNgsiLdV1EntitiesRequestType(enum.StrEnum):
    ORGANIZATION = "Organization"

    def visit(self, organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetNgsiLdV1EntitiesRequestType.ORGANIZATION:
            return organization()
