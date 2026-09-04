

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .neutral_job_status_cancelled_result_state import NeutralJobStatusCancelledResultState
from .neutral_job_status_error_result_state import NeutralJobStatusErrorResultState
from .neutral_job_status_pending_result_state import NeutralJobStatusPendingResultState
from .neutral_job_status_running_result_state import NeutralJobStatusRunningResultState
from .neutral_job_status_success_result_state import NeutralJobStatusSuccessResultState


class NeutralJobStatus_Pending(UniversalBaseModel):
    state: typing.Literal["pending"] = "pending"
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    progress: typing.Optional[float] = None
    error_tail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorTail"), pydantic.Field(alias="errorTail")
    ] = None
    result_state: typing_extensions.Annotated[
        NeutralJobStatusPendingResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NeutralJobStatus_Running(UniversalBaseModel):
    state: typing.Literal["running"] = "running"
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    progress: typing.Optional[float] = None
    error_tail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorTail"), pydantic.Field(alias="errorTail")
    ] = None
    result_state: typing_extensions.Annotated[
        NeutralJobStatusRunningResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NeutralJobStatus_Success(UniversalBaseModel):
    state: typing.Literal["success"] = "success"
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    progress: typing.Optional[float] = None
    error_tail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorTail"), pydantic.Field(alias="errorTail")
    ] = None
    result_state: typing_extensions.Annotated[
        NeutralJobStatusSuccessResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NeutralJobStatus_Error(UniversalBaseModel):
    state: typing.Literal["error"] = "error"
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    progress: typing.Optional[float] = None
    error_tail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorTail"), pydantic.Field(alias="errorTail")
    ] = None
    result_state: typing_extensions.Annotated[
        NeutralJobStatusErrorResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NeutralJobStatus_Cancelled(UniversalBaseModel):
    state: typing.Literal["cancelled"] = "cancelled"
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    progress: typing.Optional[float] = None
    error_tail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorTail"), pydantic.Field(alias="errorTail")
    ] = None
    result_state: typing_extensions.Annotated[
        NeutralJobStatusCancelledResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


NeutralJobStatus = typing_extensions.Annotated[
    typing.Union[
        NeutralJobStatus_Pending,
        NeutralJobStatus_Running,
        NeutralJobStatus_Success,
        NeutralJobStatus_Error,
        NeutralJobStatus_Cancelled,
    ],
    pydantic.Field(discriminator="state"),
]
