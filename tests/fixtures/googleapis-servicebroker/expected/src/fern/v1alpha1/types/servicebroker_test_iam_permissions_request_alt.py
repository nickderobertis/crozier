

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ServicebrokerTestIamPermissionsRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServicebrokerTestIamPermissionsRequestAlt.JSON:
            return json()
        if self is ServicebrokerTestIamPermissionsRequestAlt.MEDIA:
            return media()
        if self is ServicebrokerTestIamPermissionsRequestAlt.PROTO:
            return proto()
