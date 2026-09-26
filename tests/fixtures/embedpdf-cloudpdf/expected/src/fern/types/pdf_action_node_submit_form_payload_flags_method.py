

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PdfActionNodeSubmitFormPayloadFlagsMethod(enum.StrEnum):
    POST = "post"
    GET = "get"

    def visit(self, post: typing.Callable[[], T_Result], get: typing.Callable[[], T_Result]) -> T_Result:
        if self is PdfActionNodeSubmitFormPayloadFlagsMethod.POST:
            return post()
        if self is PdfActionNodeSubmitFormPayloadFlagsMethod.GET:
            return get()
