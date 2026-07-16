

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveLoyaltyProgramRequest(UniversalBaseModel):
    """
    A request to retrieve the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) that belongs to a seller. A seller can have only one loyalty program.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
