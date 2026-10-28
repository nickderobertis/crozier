

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang(enum.StrEnum):
    CQL2JSON = "cql2-json"
    CQL2TEXT = "cql2-text"

    def visit(self, cql2json: typing.Callable[[], T_Result], cql2text: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang.CQL2JSON:
            return cql2json()
        if self is GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang.CQL2TEXT:
            return cql2text()
