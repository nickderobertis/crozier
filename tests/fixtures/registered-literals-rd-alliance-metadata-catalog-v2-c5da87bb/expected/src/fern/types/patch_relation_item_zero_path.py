

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchRelationItemZeroPath(enum.StrEnum):
    """
    Type of relationship to add.
    """

    PARENT_SCHEMES = "/parent schemes"
    SUPPORTED_SCHEMES = "/supported schemes"
    INPUT_SCHEMES = "/input schemes"
    OUTPUT_SCHEMES = "/output schemes"
    ENDORSED_SCHEMES = "/endorsed schemes"
    MAINTAINERS = "/maintainers"
    FUNDERS = "/funders"
    USERS = "/users"
    ORIGINATORS = "/originators"

    def visit(
        self,
        parent_schemes: typing.Callable[[], T_Result],
        supported_schemes: typing.Callable[[], T_Result],
        input_schemes: typing.Callable[[], T_Result],
        output_schemes: typing.Callable[[], T_Result],
        endorsed_schemes: typing.Callable[[], T_Result],
        maintainers: typing.Callable[[], T_Result],
        funders: typing.Callable[[], T_Result],
        users: typing.Callable[[], T_Result],
        originators: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchRelationItemZeroPath.PARENT_SCHEMES:
            return parent_schemes()
        if self is PatchRelationItemZeroPath.SUPPORTED_SCHEMES:
            return supported_schemes()
        if self is PatchRelationItemZeroPath.INPUT_SCHEMES:
            return input_schemes()
        if self is PatchRelationItemZeroPath.OUTPUT_SCHEMES:
            return output_schemes()
        if self is PatchRelationItemZeroPath.ENDORSED_SCHEMES:
            return endorsed_schemes()
        if self is PatchRelationItemZeroPath.MAINTAINERS:
            return maintainers()
        if self is PatchRelationItemZeroPath.FUNDERS:
            return funders()
        if self is PatchRelationItemZeroPath.USERS:
            return users()
        if self is PatchRelationItemZeroPath.ORIGINATORS:
            return originators()
