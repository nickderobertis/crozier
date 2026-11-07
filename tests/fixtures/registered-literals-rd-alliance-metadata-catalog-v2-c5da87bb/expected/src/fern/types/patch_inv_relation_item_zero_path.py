

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchInvRelationItemZeroPath(enum.StrEnum):
    """
    Type of relationship to add.
    """

    CHILD_SCHEMES = "/child schemes"
    MAINTAINED_SCHEMES = "/maintained schemes"
    FUNDED_SCHEMES = "/funded schemes"
    USED_SCHEMES = "/used schemes"
    TOOLS = "/tools"
    MAINTAINED_TOOLS = "/maintained tools"
    FUNDED_TOOLS = "/funded tools"
    INPUT_TO_MAPPINGS = "/input to mappings"
    OUTPUT_FROM_MAPPINGS = "/output from mappings"
    MAINTAINED_MAPPINGS = "/maintained mappings"
    FUNDED_MAPPINGS = "/funded mappings"
    ENDORSEMENTS = "/endorsements"

    def visit(
        self,
        child_schemes: typing.Callable[[], T_Result],
        maintained_schemes: typing.Callable[[], T_Result],
        funded_schemes: typing.Callable[[], T_Result],
        used_schemes: typing.Callable[[], T_Result],
        tools: typing.Callable[[], T_Result],
        maintained_tools: typing.Callable[[], T_Result],
        funded_tools: typing.Callable[[], T_Result],
        input_to_mappings: typing.Callable[[], T_Result],
        output_from_mappings: typing.Callable[[], T_Result],
        maintained_mappings: typing.Callable[[], T_Result],
        funded_mappings: typing.Callable[[], T_Result],
        endorsements: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchInvRelationItemZeroPath.CHILD_SCHEMES:
            return child_schemes()
        if self is PatchInvRelationItemZeroPath.MAINTAINED_SCHEMES:
            return maintained_schemes()
        if self is PatchInvRelationItemZeroPath.FUNDED_SCHEMES:
            return funded_schemes()
        if self is PatchInvRelationItemZeroPath.USED_SCHEMES:
            return used_schemes()
        if self is PatchInvRelationItemZeroPath.TOOLS:
            return tools()
        if self is PatchInvRelationItemZeroPath.MAINTAINED_TOOLS:
            return maintained_tools()
        if self is PatchInvRelationItemZeroPath.FUNDED_TOOLS:
            return funded_tools()
        if self is PatchInvRelationItemZeroPath.INPUT_TO_MAPPINGS:
            return input_to_mappings()
        if self is PatchInvRelationItemZeroPath.OUTPUT_FROM_MAPPINGS:
            return output_from_mappings()
        if self is PatchInvRelationItemZeroPath.MAINTAINED_MAPPINGS:
            return maintained_mappings()
        if self is PatchInvRelationItemZeroPath.FUNDED_MAPPINGS:
            return funded_mappings()
        if self is PatchInvRelationItemZeroPath.ENDORSEMENTS:
            return endorsements()
