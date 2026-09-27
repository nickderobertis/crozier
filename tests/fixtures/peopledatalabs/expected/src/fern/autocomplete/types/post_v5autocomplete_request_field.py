

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostV5AutocompleteRequestField(enum.StrEnum):
    """
    An enumerated field that will be used to calculate the autocompletion
    """

    COMPANY = "company"
    COUNTRY = "country"
    INDUSTRY = "industry"
    LOCATION = "location"
    MAJOR = "major"
    REGION = "region"
    ROLE = "role"
    SCHOOL = "school"
    SUB_ROLE = "sub_role"
    SKILL = "skill"
    TITLE = "title"

    def visit(
        self,
        company: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        industry: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        major: typing.Callable[[], T_Result],
        region: typing.Callable[[], T_Result],
        role: typing.Callable[[], T_Result],
        school: typing.Callable[[], T_Result],
        sub_role: typing.Callable[[], T_Result],
        skill: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostV5AutocompleteRequestField.COMPANY:
            return company()
        if self is PostV5AutocompleteRequestField.COUNTRY:
            return country()
        if self is PostV5AutocompleteRequestField.INDUSTRY:
            return industry()
        if self is PostV5AutocompleteRequestField.LOCATION:
            return location()
        if self is PostV5AutocompleteRequestField.MAJOR:
            return major()
        if self is PostV5AutocompleteRequestField.REGION:
            return region()
        if self is PostV5AutocompleteRequestField.ROLE:
            return role()
        if self is PostV5AutocompleteRequestField.SCHOOL:
            return school()
        if self is PostV5AutocompleteRequestField.SUB_ROLE:
            return sub_role()
        if self is PostV5AutocompleteRequestField.SKILL:
            return skill()
        if self is PostV5AutocompleteRequestField.TITLE:
            return title()
