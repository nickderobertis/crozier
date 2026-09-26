

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApplicationChangeFundedPlaceRequestDataAttributes(UniversalBaseModel):
    """
    A NPQ application change funded place request attributes
    """

    funded_place: bool = pydantic.Field()
    """
    Whether the participant has a funded place
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
