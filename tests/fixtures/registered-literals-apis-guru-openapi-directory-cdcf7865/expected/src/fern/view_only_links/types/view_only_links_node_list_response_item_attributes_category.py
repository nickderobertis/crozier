

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOnlyLinksNodeListResponseItemAttributesCategory(enum.StrEnum):
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
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.ANALYSIS:
            return analysis()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.COMMUNICATION:
            return communication()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.DATA:
            return data()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.HYPOTHESIS:
            return hypothesis()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.INSTRUMENTATION:
            return instrumentation()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.METHODS_AND_MEASURES:
            return methods_and_measures()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.PROCEDURE:
            return procedure()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.PROJECT:
            return project()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.SOFTWARE:
            return software()
        if self is ViewOnlyLinksNodeListResponseItemAttributesCategory.OTHER:
            return other()
