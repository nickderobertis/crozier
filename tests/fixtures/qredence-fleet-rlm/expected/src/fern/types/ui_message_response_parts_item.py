

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .json_value import JsonValue


class UiMessageResponsePartsItem_DataArtifact(UniversalBaseModel):
    type: typing.Literal["data-artifact"] = "data-artifact"
    data: JsonValue
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataAttachment(UniversalBaseModel):
    type: typing.Literal["data-attachment"] = "data-attachment"
    data: JsonValue
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataChildProgress(UniversalBaseModel):
    type: typing.Literal["data-child-progress"] = "data-child-progress"
    data: JsonValue
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataRlmCode(UniversalBaseModel):
    type: typing.Literal["data-rlm-code"] = "data-rlm-code"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataRlmOutput(UniversalBaseModel):
    type: typing.Literal["data-rlm-output"] = "data-rlm-output"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataSkill(UniversalBaseModel):
    type: typing.Literal["data-skill"] = "data-skill"
    data: JsonValue
    id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataStatus(UniversalBaseModel):
    type: typing.Literal["data-status"] = "data-status"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataStep(UniversalBaseModel):
    type: typing.Literal["data-step"] = "data-step"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataStructuredResult(UniversalBaseModel):
    type: typing.Literal["data-structured-result"] = "data-structured-result"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataUsage(UniversalBaseModel):
    type: typing.Literal["data-usage"] = "data-usage"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DataWarning(UniversalBaseModel):
    type: typing.Literal["data-warning"] = "data-warning"
    data: JsonValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_DynamicTool(UniversalBaseModel):
    type: typing.Literal["dynamic-tool"] = "dynamic-tool"
    tool_name: typing_extensions.Annotated[str, FieldMetadata(alias="toolName"), pydantic.Field(alias="toolName")]
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    state: str
    input: JsonValue
    output: typing.Optional[JsonValue] = None
    error_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorText"), pydantic.Field(alias="errorText")
    ] = None
    provider_executed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="providerExecuted"), pydantic.Field(alias="providerExecuted")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_Reasoning(UniversalBaseModel):
    type: typing.Literal["reasoning"] = "reasoning"
    text: str
    state: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_StepStart(UniversalBaseModel):
    type: typing.Literal["step-start"] = "step-start"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiMessageResponsePartsItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str
    state: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UiMessageResponsePartsItem = typing_extensions.Annotated[
    typing.Union[
        UiMessageResponsePartsItem_DataArtifact,
        UiMessageResponsePartsItem_DataAttachment,
        UiMessageResponsePartsItem_DataChildProgress,
        UiMessageResponsePartsItem_DataRlmCode,
        UiMessageResponsePartsItem_DataRlmOutput,
        UiMessageResponsePartsItem_DataSkill,
        UiMessageResponsePartsItem_DataStatus,
        UiMessageResponsePartsItem_DataStep,
        UiMessageResponsePartsItem_DataStructuredResult,
        UiMessageResponsePartsItem_DataUsage,
        UiMessageResponsePartsItem_DataWarning,
        UiMessageResponsePartsItem_DynamicTool,
        UiMessageResponsePartsItem_Reasoning,
        UiMessageResponsePartsItem_StepStart,
        UiMessageResponsePartsItem_Text,
    ],
    pydantic.Field(discriminator="type"),
]
