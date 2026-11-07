

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesChildrenCreateRequestAttributesCategory(enum.StrEnum):
    """
    The category of the node, as selected by project contributors.
    """

    ANALYSIS = "analysis"
    COMMUNICATION = "communication"
    DATA = "data"
    HYPOTHESIS = "hypothesis"
    INSTRUMENTATION = "instrumentation"
    METHODS_AND_MEASURES = "methods and measures"
    PROCEDURE = "procedure"
    PROJECT = "project"
    SOFTWARE = "software"
    OTHER = "other"

    def visit(
        self,
        analysis: typing.Callable[[], T_Result],
        communication: typing.Callable[[], T_Result],
        data: typing.Callable[[], T_Result],
        hypothesis: typing.Callable[[], T_Result],
        instrumentation: typing.Callable[[], T_Result],
        methods_and_measures: typing.Callable[[], T_Result],
        procedure: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        software: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NodesChildrenCreateRequestAttributesCategory.ANALYSIS:
            return analysis()
        if self is NodesChildrenCreateRequestAttributesCategory.COMMUNICATION:
            return communication()
        if self is NodesChildrenCreateRequestAttributesCategory.DATA:
            return data()
        if self is NodesChildrenCreateRequestAttributesCategory.HYPOTHESIS:
            return hypothesis()
        if self is NodesChildrenCreateRequestAttributesCategory.INSTRUMENTATION:
            return instrumentation()
        if self is NodesChildrenCreateRequestAttributesCategory.METHODS_AND_MEASURES:
            return methods_and_measures()
        if self is NodesChildrenCreateRequestAttributesCategory.PROCEDURE:
            return procedure()
        if self is NodesChildrenCreateRequestAttributesCategory.PROJECT:
            return project()
        if self is NodesChildrenCreateRequestAttributesCategory.SOFTWARE:
            return software()
        if self is NodesChildrenCreateRequestAttributesCategory.OTHER:
            return other()
