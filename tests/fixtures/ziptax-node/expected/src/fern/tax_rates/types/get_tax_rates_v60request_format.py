

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTaxRatesV60RequestFormat(enum.StrEnum):
    """
    Serialization format of the response body. 'json' (default) returns a JSON object; 'xml' returns the same data as an XML document.
    """

    JSON = "json"
    XML = "xml"

    def visit(self, json: typing.Callable[[], T_Result], xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTaxRatesV60RequestFormat.JSON:
            return json()
        if self is GetTaxRatesV60RequestFormat.XML:
            return xml()
