

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .belt_status_belt import BeltStatusBelt
from .belt_status_id import BeltStatusId


class BeltStatus(UniversalBaseModel):
    """
    Seat belt condition.
    """

    belt: typing.Optional[BeltStatusBelt] = pydantic.Field(default=None)
    """
    Belt status.
    """

    id: typing.Optional[BeltStatusId] = pydantic.Field(default=None)
    """
    Seat identifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
