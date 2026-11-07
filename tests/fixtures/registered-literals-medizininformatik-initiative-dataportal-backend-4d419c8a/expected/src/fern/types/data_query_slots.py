

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataQuerySlots(UniversalBaseModel):
    used: int = pydantic.Field()
    """
    The amount of used dataquery slots for a user.
    """

    total: int = pydantic.Field()
    """
    The total amount of dataquery slots per user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
