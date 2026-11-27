

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Part_Bolt(UniversalBaseModel):
    type: typing.Literal["BOLT"] = "BOLT"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Nut(UniversalBaseModel):
    type: typing.Literal["NUT"] = "NUT"
    size: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Part = typing_extensions.Annotated[typing.Union[Part_Bolt, Part_Nut], pydantic.Field(discriminator="type")]
