

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseResourceCategoriesItem(enum.StrEnum):
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
        if self is CourseResourceCategoriesItem.ARTS:
            return arts()
        if self is CourseResourceCategoriesItem.BUSINESS:
            return business()
        if self is CourseResourceCategoriesItem.COMMUNICATION:
            return communication()
        if self is CourseResourceCategoriesItem.CULTURE:
            return culture()
        if self is CourseResourceCategoriesItem.ECONOMICS:
            return economics()
        if self is CourseResourceCategoriesItem.ENGINEERING:
            return engineering()
        if self is CourseResourceCategoriesItem.GEOGRAPHY:
            return geography()
        if self is CourseResourceCategoriesItem.HEALTH:
            return health()
        if self is CourseResourceCategoriesItem.HISTORY:
            return history()
        if self is CourseResourceCategoriesItem.LANGUAGES:
            return languages()
        if self is CourseResourceCategoriesItem.LAW:
            return law()
        if self is CourseResourceCategoriesItem.MATH:
            return math()
        if self is CourseResourceCategoriesItem.SCIENCE:
            return science()
        if self is CourseResourceCategoriesItem.SOCIETY:
            return society()
        if self is CourseResourceCategoriesItem.TECH:
            return tech()
