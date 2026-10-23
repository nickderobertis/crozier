

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBuildsIdResponseBuildCustodyMode(enum.StrEnum):
    PLATFORM = "platform"
    HOSTED = "hosted"
    GATEWAY = "gateway"

    def visit(
        self,
        platform: typing.Callable[[], T_Result],
        hosted: typing.Callable[[], T_Result],
        gateway: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBuildsIdResponseBuildCustodyMode.PLATFORM:
            return platform()
        if self is GetBuildsIdResponseBuildCustodyMode.HOSTED:
            return hosted()
        if self is GetBuildsIdResponseBuildCustodyMode.GATEWAY:
            return gateway()
