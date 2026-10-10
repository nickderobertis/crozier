

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Loaf_Sourdough(UniversalBaseModel):
    grain: typing.Literal["sourdough"] = "sourdough"
    starter_age_days: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Loaf_Rye(UniversalBaseModel):
    grain: typing.Literal["rye"] = "rye"
    caraway: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Loaf = typing_extensions.Annotated[typing.Union[Loaf_Sourdough, Loaf_Rye], pydantic.Field(discriminator="grain")]
