

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyProgramTerminology(UniversalBaseModel):
    """
    Represents the naming used for loyalty points.
    """

    one: str = pydantic.Field()
    """
    A singular unit for a point (for example, 1 point is called 1 star).
    """

    other: str = pydantic.Field()
    """
    A plural unit for point (for example, 10 points is called 10 stars).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
