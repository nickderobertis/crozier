

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SolrqueryPostRequestWt(enum.StrEnum):
    JSON = "json"
    XML = "xml"

    def visit(self, json: typing.Callable[[], T_Result], xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is SolrqueryPostRequestWt.JSON:
            return json()
        if self is SolrqueryPostRequestWt.XML:
            return xml()
