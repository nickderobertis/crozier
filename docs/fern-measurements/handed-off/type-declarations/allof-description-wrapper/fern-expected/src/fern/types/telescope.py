

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slot_id import SlotId


class Telescope(UniversalBaseModel):
    dome: typing.Optional[str] = pydantic.Field(default=None)
    """
    Where the telescope sits.
    """

    slot: typing.Optional[SlotId] = None
    aperture: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
