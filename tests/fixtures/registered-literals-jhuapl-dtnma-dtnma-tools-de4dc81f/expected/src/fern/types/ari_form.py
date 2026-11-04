

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AriForm(enum.StrEnum):
    URI = "uri"
    CBOR = "cbor"
    CBORHEX = "cborhex"

    def visit(
        self,
        uri: typing.Callable[[], T_Result],
        cbor: typing.Callable[[], T_Result],
        cborhex: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AriForm.URI:
            return uri()
        if self is AriForm.CBOR:
            return cbor()
        if self is AriForm.CBORHEX:
            return cborhex()
