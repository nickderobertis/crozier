

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ManifestScalarConfig_Boolean(UniversalBaseModel):
    type: typing.Literal["boolean"] = "boolean"
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_Date(UniversalBaseModel):
    type: typing.Literal["date"] = "date"
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_Datetime(UniversalBaseModel):
    type: typing.Literal["datetime"] = "datetime"
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_Float(UniversalBaseModel):
    type: typing.Literal["float"] = "float"
    enum: typing.Optional[typing.List[float]] = None
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_Integer(UniversalBaseModel):
    type: typing.Literal["integer"] = "integer"
    enum: typing.Optional[typing.List[int]] = None
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_Json(UniversalBaseModel):
    type: typing.Literal["json"] = "json"
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_SecureText(UniversalBaseModel):
    type: typing.Literal["secure_text"] = "secure_text"
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManifestScalarConfig_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    enum: typing.Optional[typing.List[str]] = None
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ManifestScalarConfig = typing_extensions.Annotated[
    typing.Union[
        ManifestScalarConfig_Boolean,
        ManifestScalarConfig_Date,
        ManifestScalarConfig_Datetime,
        ManifestScalarConfig_Float,
        ManifestScalarConfig_Integer,
        ManifestScalarConfig_Json,
        ManifestScalarConfig_SecureText,
        ManifestScalarConfig_Text,
    ],
    pydantic.Field(discriminator="type"),
]
