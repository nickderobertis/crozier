

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SolrqueryGetRequestWt(enum.StrEnum):
    JSON = "json"
    XML = "xml"
    CSV = "csv"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        xml: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SolrqueryGetRequestWt.JSON:
            return json()
        if self is SolrqueryGetRequestWt.XML:
            return xml()
        if self is SolrqueryGetRequestWt.CSV:
            return csv()
