

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CpsPackageType(enum.StrEnum):
    MODEL = "model"
    DICTIONARY = "dictionary"
    KNOWLEDGE_GRAPH = "knowledge_graph"
    DATA_CATALOG = "data_catalog"
    DATA_FLOW = "data_flow"
    BUNDLE = "bundle"

    def visit(
        self,
        model: typing.Callable[[], T_Result],
        dictionary: typing.Callable[[], T_Result],
        knowledge_graph: typing.Callable[[], T_Result],
        data_catalog: typing.Callable[[], T_Result],
        data_flow: typing.Callable[[], T_Result],
        bundle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CpsPackageType.MODEL:
            return model()
        if self is CpsPackageType.DICTIONARY:
            return dictionary()
        if self is CpsPackageType.KNOWLEDGE_GRAPH:
            return knowledge_graph()
        if self is CpsPackageType.DATA_CATALOG:
            return data_catalog()
        if self is CpsPackageType.DATA_FLOW:
            return data_flow()
        if self is CpsPackageType.BUNDLE:
            return bundle()
