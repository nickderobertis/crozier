

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesCreateRequestAttributesCategory(enum.StrEnum):
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
        if self is NodesCreateRequestAttributesCategory.ANALYSIS:
            return analysis()
        if self is NodesCreateRequestAttributesCategory.COMMUNICATION:
            return communication()
        if self is NodesCreateRequestAttributesCategory.DATA:
            return data()
        if self is NodesCreateRequestAttributesCategory.HYPOTHESIS:
            return hypothesis()
        if self is NodesCreateRequestAttributesCategory.INSTRUMENTATION:
            return instrumentation()
        if self is NodesCreateRequestAttributesCategory.METHODS_AND_MEASURES:
            return methods_and_measures()
        if self is NodesCreateRequestAttributesCategory.PROCEDURE:
            return procedure()
        if self is NodesCreateRequestAttributesCategory.PROJECT:
            return project()
        if self is NodesCreateRequestAttributesCategory.SOFTWARE:
            return software()
        if self is NodesCreateRequestAttributesCategory.OTHER:
            return other()
