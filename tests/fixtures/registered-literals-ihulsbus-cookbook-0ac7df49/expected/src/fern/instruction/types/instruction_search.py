

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstructionSearch(UniversalBaseModel):
    """
    Returns searchresult of instructions belonging to the queried recipe
    """

    recipe_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the recipe
    """

    instruction_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array with ID's of instructions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
