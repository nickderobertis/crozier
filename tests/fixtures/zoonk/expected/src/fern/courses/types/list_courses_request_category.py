

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListCoursesRequestCategory(enum.StrEnum):
    """
    Course category filter
    """

    ARTS = "arts"
    BUSINESS = "business"
    COMMUNICATION = "communication"
    CULTURE = "culture"
    ECONOMICS = "economics"
    ENGINEERING = "engineering"
    GEOGRAPHY = "geography"
    HEALTH = "health"
    HISTORY = "history"
    LANGUAGES = "languages"
    LAW = "law"
    MATH = "math"
    SCIENCE = "science"
    SOCIETY = "society"
    TECH = "tech"

    def visit(
        self,
        arts: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        communication: typing.Callable[[], T_Result],
        culture: typing.Callable[[], T_Result],
        economics: typing.Callable[[], T_Result],
        engineering: typing.Callable[[], T_Result],
        geography: typing.Callable[[], T_Result],
        health: typing.Callable[[], T_Result],
        history: typing.Callable[[], T_Result],
        languages: typing.Callable[[], T_Result],
        law: typing.Callable[[], T_Result],
        math: typing.Callable[[], T_Result],
        science: typing.Callable[[], T_Result],
        society: typing.Callable[[], T_Result],
        tech: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListCoursesRequestCategory.ARTS:
            return arts()
        if self is ListCoursesRequestCategory.BUSINESS:
            return business()
        if self is ListCoursesRequestCategory.COMMUNICATION:
            return communication()
        if self is ListCoursesRequestCategory.CULTURE:
            return culture()
        if self is ListCoursesRequestCategory.ECONOMICS:
            return economics()
        if self is ListCoursesRequestCategory.ENGINEERING:
            return engineering()
        if self is ListCoursesRequestCategory.GEOGRAPHY:
            return geography()
        if self is ListCoursesRequestCategory.HEALTH:
            return health()
        if self is ListCoursesRequestCategory.HISTORY:
            return history()
        if self is ListCoursesRequestCategory.LANGUAGES:
            return languages()
        if self is ListCoursesRequestCategory.LAW:
            return law()
        if self is ListCoursesRequestCategory.MATH:
            return math()
        if self is ListCoursesRequestCategory.SCIENCE:
            return science()
        if self is ListCoursesRequestCategory.SOCIETY:
            return society()
        if self is ListCoursesRequestCategory.TECH:
            return tech()
