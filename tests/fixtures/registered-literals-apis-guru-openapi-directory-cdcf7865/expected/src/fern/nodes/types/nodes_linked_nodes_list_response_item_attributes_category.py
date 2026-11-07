

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesLinkedNodesListResponseItemAttributesCategory(enum.StrEnum):
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
        if self is NodesLinkedNodesListResponseItemAttributesCategory.ANALYSIS:
            return analysis()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.COMMUNICATION:
            return communication()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.DATA:
            return data()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.HYPOTHESIS:
            return hypothesis()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.INSTRUMENTATION:
            return instrumentation()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.METHODS_AND_MEASURES:
            return methods_and_measures()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.PROCEDURE:
            return procedure()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.PROJECT:
            return project()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.SOFTWARE:
            return software()
        if self is NodesLinkedNodesListResponseItemAttributesCategory.OTHER:
            return other()
