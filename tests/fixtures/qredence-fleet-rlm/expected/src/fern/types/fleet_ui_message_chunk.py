

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fleet_ui_message_chunk_data_artifact_data import FleetUiMessageChunkDataArtifactData
from .fleet_ui_message_chunk_data_attachment_data import FleetUiMessageChunkDataAttachmentData
from .fleet_ui_message_chunk_data_child_progress_data import FleetUiMessageChunkDataChildProgressData
from .fleet_ui_message_chunk_data_rlm_code_data import FleetUiMessageChunkDataRlmCodeData
from .fleet_ui_message_chunk_data_rlm_output_data import FleetUiMessageChunkDataRlmOutputData
from .fleet_ui_message_chunk_data_skill_data import FleetUiMessageChunkDataSkillData
from .fleet_ui_message_chunk_data_status_data import FleetUiMessageChunkDataStatusData
from .fleet_ui_message_chunk_data_structured_result_data import FleetUiMessageChunkDataStructuredResultData
from .fleet_ui_message_chunk_data_usage_data import FleetUiMessageChunkDataUsageData
from .fleet_ui_message_chunk_data_warning_data import FleetUiMessageChunkDataWarningData
from .fleet_ui_message_chunk_finish_finish_reason import FleetUiMessageChunkFinishFinishReason


class FleetUiMessageChunk_Start(UniversalBaseModel):
    type: typing.Literal["start"] = "start"
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")]
    message_metadata: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="messageMetadata"), pydantic.Field(alias="messageMetadata")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_StartStep(UniversalBaseModel):
    type: typing.Literal["start-step"] = "start-step"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_FinishStep(UniversalBaseModel):
    type: typing.Literal["finish-step"] = "finish-step"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_ReasoningStart(UniversalBaseModel):
    type: typing.Literal["reasoning-start"] = "reasoning-start"
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_ReasoningDelta(UniversalBaseModel):
    type: typing.Literal["reasoning-delta"] = "reasoning-delta"
    id: str
    delta: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_ReasoningEnd(UniversalBaseModel):
    type: typing.Literal["reasoning-end"] = "reasoning-end"
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataStatus(UniversalBaseModel):
    type: typing.Literal["data-status"] = "data-status"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataStatusData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataChildProgress(UniversalBaseModel):
    type: typing.Literal["data-child-progress"] = "data-child-progress"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataChildProgressData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataSkill(UniversalBaseModel):
    type: typing.Literal["data-skill"] = "data-skill"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataSkillData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataRlmCode(UniversalBaseModel):
    type: typing.Literal["data-rlm-code"] = "data-rlm-code"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataRlmCodeData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataRlmOutput(UniversalBaseModel):
    type: typing.Literal["data-rlm-output"] = "data-rlm-output"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataRlmOutputData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_ToolInputAvailable(UniversalBaseModel):
    type: typing.Literal["tool-input-available"] = "tool-input-available"
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    tool_name: typing_extensions.Annotated[str, FieldMetadata(alias="toolName"), pydantic.Field(alias="toolName")]
    input: typing.Any
    dynamic: typing.Optional[bool] = None
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


class FleetUiMessageChunk_ToolOutputAvailable(UniversalBaseModel):
    type: typing.Literal["tool-output-available"] = "tool-output-available"
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    output: typing.Any
    dynamic: typing.Optional[bool] = None
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


class FleetUiMessageChunk_ToolOutputError(UniversalBaseModel):
    type: typing.Literal["tool-output-error"] = "tool-output-error"
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    error_text: typing_extensions.Annotated[str, FieldMetadata(alias="errorText"), pydantic.Field(alias="errorText")]
    dynamic: typing.Optional[bool] = None
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


class FleetUiMessageChunk_DataAttachment(UniversalBaseModel):
    type: typing.Literal["data-attachment"] = "data-attachment"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataAttachmentData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataWarning(UniversalBaseModel):
    type: typing.Literal["data-warning"] = "data-warning"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataWarningData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataArtifact(UniversalBaseModel):
    type: typing.Literal["data-artifact"] = "data-artifact"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataArtifactData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataUsage(UniversalBaseModel):
    type: typing.Literal["data-usage"] = "data-usage"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataUsageData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_DataStructuredResult(UniversalBaseModel):
    type: typing.Literal["data-structured-result"] = "data-structured-result"
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataStructuredResultData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_TextStart(UniversalBaseModel):
    type: typing.Literal["text-start"] = "text-start"
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_TextDelta(UniversalBaseModel):
    type: typing.Literal["text-delta"] = "text-delta"
    id: str
    delta: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_TextEnd(UniversalBaseModel):
    type: typing.Literal["text-end"] = "text-end"
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_Finish(UniversalBaseModel):
    type: typing.Literal["finish"] = "finish"
    finish_reason: typing_extensions.Annotated[
        FleetUiMessageChunkFinishFinishReason, FieldMetadata(alias="finishReason"), pydantic.Field(alias="finishReason")
    ]
    message_metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="messageMetadata"),
        pydantic.Field(alias="messageMetadata"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_Abort(UniversalBaseModel):
    type: typing.Literal["abort"] = "abort"
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FleetUiMessageChunk_Error(UniversalBaseModel):
    type: typing.Literal["error"] = "error"
    error_text: typing_extensions.Annotated[str, FieldMetadata(alias="errorText"), pydantic.Field(alias="errorText")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FleetUiMessageChunk = typing_extensions.Annotated[
    typing.Union[
        FleetUiMessageChunk_Start,
        FleetUiMessageChunk_StartStep,
        FleetUiMessageChunk_FinishStep,
        FleetUiMessageChunk_ReasoningStart,
        FleetUiMessageChunk_ReasoningDelta,
        FleetUiMessageChunk_ReasoningEnd,
        FleetUiMessageChunk_DataStatus,
        FleetUiMessageChunk_DataChildProgress,
        FleetUiMessageChunk_DataSkill,
        FleetUiMessageChunk_DataRlmCode,
        FleetUiMessageChunk_DataRlmOutput,
        FleetUiMessageChunk_ToolInputAvailable,
        FleetUiMessageChunk_ToolOutputAvailable,
        FleetUiMessageChunk_ToolOutputError,
        FleetUiMessageChunk_DataAttachment,
        FleetUiMessageChunk_DataWarning,
        FleetUiMessageChunk_DataArtifact,
        FleetUiMessageChunk_DataUsage,
        FleetUiMessageChunk_DataStructuredResult,
        FleetUiMessageChunk_TextStart,
        FleetUiMessageChunk_TextDelta,
        FleetUiMessageChunk_TextEnd,
        FleetUiMessageChunk_Finish,
        FleetUiMessageChunk_Abort,
        FleetUiMessageChunk_Error,
    ],
    pydantic.Field(discriminator="type"),
]
