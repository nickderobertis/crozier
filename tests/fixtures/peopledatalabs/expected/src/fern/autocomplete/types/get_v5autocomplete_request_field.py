

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetV5AutocompleteRequestField(enum.StrEnum):
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
        if self is GetV5AutocompleteRequestField.COMPANY:
            return company()
        if self is GetV5AutocompleteRequestField.COUNTRY:
            return country()
        if self is GetV5AutocompleteRequestField.INDUSTRY:
            return industry()
        if self is GetV5AutocompleteRequestField.LOCATION:
            return location()
        if self is GetV5AutocompleteRequestField.MAJOR:
            return major()
        if self is GetV5AutocompleteRequestField.REGION:
            return region()
        if self is GetV5AutocompleteRequestField.ROLE:
            return role()
        if self is GetV5AutocompleteRequestField.SCHOOL:
            return school()
        if self is GetV5AutocompleteRequestField.SUB_ROLE:
            return sub_role()
        if self is GetV5AutocompleteRequestField.SKILL:
            return skill()
        if self is GetV5AutocompleteRequestField.TITLE:
            return title()
