

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .major_type import MajorType


class OutputDescription_CompoundDateRange(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["COMPOUND_DATE_RANGE"] = "COMPOUND_DATE_RANGE"
    start_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startColumn"), pydantic.Field(alias="startColumn")
    ] = None
    end_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endColumn"), pydantic.Field(alias="endColumn")
    ] = None
    allow_open: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowOpen"), pydantic.Field(alias="allowOpen")
    ] = None
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OutputDescription_Copy(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["COPY"] = "COPY"
    input_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputColumn"), pydantic.Field(alias="inputColumn")
    ] = None
    input_type: typing_extensions.Annotated[
        typing.Optional[MajorType], FieldMetadata(alias="inputType"), pydantic.Field(alias="inputType")
    ] = None
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OutputDescription_DateRange(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["DATE_RANGE"] = "DATE_RANGE"
    start_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startColumn"), pydantic.Field(alias="startColumn")
    ] = None
    end_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endColumn"), pydantic.Field(alias="endColumn")
    ] = None
    allow_open: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowOpen"), pydantic.Field(alias="allowOpen")
    ] = None
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OutputDescription_Epoch(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["EPOCH"] = "EPOCH"
    input_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputColumn"), pydantic.Field(alias="inputColumn")
    ] = None
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OutputDescription_EpochDateRange(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["EPOCH_DATE_RANGE"] = "EPOCH_DATE_RANGE"
    start_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startColumn"), pydantic.Field(alias="startColumn")
    ] = None
    end_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endColumn"), pydantic.Field(alias="endColumn")
    ] = None
    allow_open: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowOpen"), pydantic.Field(alias="allowOpen")
    ] = None
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OutputDescription_Line(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["LINE"] = "LINE"
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OutputDescription_Null(UniversalBaseModel):
    """
    Operations to transform, then import, values into tables.
    """

    operation: typing.Literal["NULL"] = "NULL"
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


OutputDescription = typing_extensions.Annotated[
    typing.Union[
        OutputDescription_CompoundDateRange,
        OutputDescription_Copy,
        OutputDescription_DateRange,
        OutputDescription_Epoch,
        OutputDescription_EpochDateRange,
        OutputDescription_Line,
        OutputDescription_Null,
    ],
    pydantic.Field(discriminator="operation"),
]
