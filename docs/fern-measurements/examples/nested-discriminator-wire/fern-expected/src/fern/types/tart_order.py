

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TartOrder_Shortcrust(UniversalBaseModel):
    crust: typing.Literal["shortcrust"] = "shortcrust"
    kind: str
    fruit: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TartOrder_Puff(UniversalBaseModel):
    crust: typing.Literal["puff"] = "puff"
    kind: str
    cream: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TartOrder = typing_extensions.Annotated[
    typing.Union[TartOrder_Shortcrust, TartOrder_Puff], pydantic.Field(discriminator="crust")
]
