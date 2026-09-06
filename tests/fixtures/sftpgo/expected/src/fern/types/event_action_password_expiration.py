

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventActionPasswordExpiration(UniversalBaseModel):
    threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    An email notification will be generated for users whose password expires in a number of days less than or equal to this threshold
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
