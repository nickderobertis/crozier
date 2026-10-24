

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FiringBookingEnding_Cooled(UniversalBaseModel):
    outcome: typing.Literal["cooled"] = "cooled"
    hours: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FiringBookingEnding_Vented(UniversalBaseModel):
    outcome: typing.Literal["vented"] = "vented"
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FiringBookingEnding = typing_extensions.Annotated[
    typing.Union[FiringBookingEnding_Cooled, FiringBookingEnding_Vented], pydantic.Field(discriminator="outcome")
]
