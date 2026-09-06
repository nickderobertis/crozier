

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt.JSON:
            return json()
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt.MEDIA:
            return media()
        if self is ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt.PROTO:
            return proto()
