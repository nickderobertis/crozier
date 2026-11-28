

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BarcodeQueryValuePart_BarcodeValue(UniversalBaseModel):
    type: typing.Literal["BARCODE_VALUE"] = "BARCODE_VALUE"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BarcodeQueryValuePart_FormFieldValue(UniversalBaseModel):
    type: typing.Literal["FORM_FIELD_VALUE"] = "FORM_FIELD_VALUE"
    key: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BarcodeQueryValuePart_RawString(UniversalBaseModel):
    type: typing.Literal["RAW_STRING"] = "RAW_STRING"
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


BarcodeQueryValuePart = typing_extensions.Annotated[
    typing.Union[
        BarcodeQueryValuePart_BarcodeValue, BarcodeQueryValuePart_FormFieldValue, BarcodeQueryValuePart_RawString
    ],
    pydantic.Field(discriminator="type"),
]
