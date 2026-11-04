

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesRegistrationsListResponseItemAttributesCategory(enum.StrEnum):
    """
    The category of the registered node.
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
        if self is NodesRegistrationsListResponseItemAttributesCategory.ANALYSIS:
            return analysis()
        if self is NodesRegistrationsListResponseItemAttributesCategory.COMMUNICATION:
            return communication()
        if self is NodesRegistrationsListResponseItemAttributesCategory.DATA:
            return data()
        if self is NodesRegistrationsListResponseItemAttributesCategory.HYPOTHESIS:
            return hypothesis()
        if self is NodesRegistrationsListResponseItemAttributesCategory.INSTRUMENTATION:
            return instrumentation()
        if self is NodesRegistrationsListResponseItemAttributesCategory.METHODS_AND_MEASURES:
            return methods_and_measures()
        if self is NodesRegistrationsListResponseItemAttributesCategory.PROCEDURE:
            return procedure()
        if self is NodesRegistrationsListResponseItemAttributesCategory.PROJECT:
            return project()
        if self is NodesRegistrationsListResponseItemAttributesCategory.SOFTWARE:
            return software()
        if self is NodesRegistrationsListResponseItemAttributesCategory.OTHER:
            return other()
