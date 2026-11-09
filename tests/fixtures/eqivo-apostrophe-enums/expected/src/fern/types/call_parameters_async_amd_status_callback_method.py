

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallParametersAsyncAmdStatusCallbackMethod(enum.StrEnum):
    """
    HTTP method to be used when answering machine detection is completed (an Eqivo extension)
    """

    POST = "POST"
    GET = "GET"

    def visit(self, post: typing.Callable[[], T_Result], get: typing.Callable[[], T_Result]) -> T_Result:
        if self is CallParametersAsyncAmdStatusCallbackMethod.POST:
            return post()
        if self is CallParametersAsyncAmdStatusCallbackMethod.GET:
            return get()
