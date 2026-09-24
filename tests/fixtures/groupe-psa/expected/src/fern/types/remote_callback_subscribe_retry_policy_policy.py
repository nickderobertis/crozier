

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteCallbackSubscribeRetryPolicyPolicy(enum.StrEnum):
    """
    Defines the retry rules following a notification failure (ie the return code is not HTTP 2XX for  WebHook mode). ```None``` means with a single try, ```Bounded``` with a limited number of tries.
    """

    NONE = "None"
    BOUNDED = "Bounded"

    def visit(self, none: typing.Callable[[], T_Result], bounded: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteCallbackSubscribeRetryPolicyPolicy.NONE:
            return none()
        if self is RemoteCallbackSubscribeRetryPolicyPolicy.BOUNDED:
            return bounded()
