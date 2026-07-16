

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventOther(UniversalBaseModel):
    """
    Provides metadata when the event `type` is `OTHER`.
    """

    loyalty_program_id: str = pydantic.Field()
    """
    The Square-assigned ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram).
    """

    points: int = pydantic.Field()
    """
    The number of points added or removed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
