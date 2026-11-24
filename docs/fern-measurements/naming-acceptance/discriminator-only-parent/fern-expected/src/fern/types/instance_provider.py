

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstanceProvider_BarcodeScan(UniversalBaseModel):
    type: typing.Literal["BARCODE_SCAN"] = "BARCODE_SCAN"
    barcode: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InstanceProvider_Manual(UniversalBaseModel):
    type: typing.Literal["MANUAL"] = "MANUAL"
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InstanceProvider = typing_extensions.Annotated[
    typing.Union[InstanceProvider_BarcodeScan, InstanceProvider_Manual], pydantic.Field(discriminator="type")
]
