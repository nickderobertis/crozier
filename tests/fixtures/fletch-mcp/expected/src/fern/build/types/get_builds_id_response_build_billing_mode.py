

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBuildsIdResponseBuildBillingMode(enum.StrEnum):
    """
    Immutable queued billing choice. Null means the older record did not capture this choice.
    """

    PLATFORM = "platform"
    OWN_KEY = "own_key"

    def visit(self, platform: typing.Callable[[], T_Result], own_key: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetBuildsIdResponseBuildBillingMode.PLATFORM:
            return platform()
        if self is GetBuildsIdResponseBuildBillingMode.OWN_KEY:
            return own_key()
