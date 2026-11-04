

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesReadResponseAttributesCategory(enum.StrEnum):
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
        if self is NodesReadResponseAttributesCategory.ANALYSIS:
            return analysis()
        if self is NodesReadResponseAttributesCategory.COMMUNICATION:
            return communication()
        if self is NodesReadResponseAttributesCategory.DATA:
            return data()
        if self is NodesReadResponseAttributesCategory.HYPOTHESIS:
            return hypothesis()
        if self is NodesReadResponseAttributesCategory.INSTRUMENTATION:
            return instrumentation()
        if self is NodesReadResponseAttributesCategory.METHODS_AND_MEASURES:
            return methods_and_measures()
        if self is NodesReadResponseAttributesCategory.PROCEDURE:
            return procedure()
        if self is NodesReadResponseAttributesCategory.PROJECT:
            return project()
        if self is NodesReadResponseAttributesCategory.SOFTWARE:
            return software()
        if self is NodesReadResponseAttributesCategory.OTHER:
            return other()
