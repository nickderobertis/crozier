

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ServicebrokerGetIamPolicyRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServicebrokerGetIamPolicyRequestAlt.JSON:
            return json()
        if self is ServicebrokerGetIamPolicyRequestAlt.MEDIA:
            return media()
        if self is ServicebrokerGetIamPolicyRequestAlt.PROTO:
            return proto()
