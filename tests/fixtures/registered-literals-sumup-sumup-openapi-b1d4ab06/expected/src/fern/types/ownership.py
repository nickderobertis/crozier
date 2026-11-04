

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ownership(UniversalBaseModel):
    share: int = pydantic.Field()
    """
    The percent of ownership shares held by the Person expressed in percent mille (1/100000). Only Persons with the relationship `owner` can have ownership.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
