

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_results_error_results_not_ready_result_state import JobResultsErrorResultsNotReadyResultState
from .job_results_error_results_not_ready_state import JobResultsErrorResultsNotReadyState
from .job_results_error_results_unavailable_result_state import JobResultsErrorResultsUnavailableResultState
from .job_results_error_results_unavailable_state import JobResultsErrorResultsUnavailableState


class JobResultsError_ResultsNotReady(UniversalBaseModel):
    code: typing.Literal["results_not_ready"] = "results_not_ready"
    message: str
    state: JobResultsErrorResultsNotReadyState
    result_state: typing_extensions.Annotated[
        JobResultsErrorResultsNotReadyResultState,
        FieldMetadata(alias="resultState"),
        pydantic.Field(alias="resultState"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class JobResultsError_ResultsUnavailable(UniversalBaseModel):
    code: typing.Literal["results_unavailable"] = "results_unavailable"
    message: str
    state: JobResultsErrorResultsUnavailableState
    result_state: typing_extensions.Annotated[
        JobResultsErrorResultsUnavailableResultState,
        FieldMetadata(alias="resultState"),
        pydantic.Field(alias="resultState"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


JobResultsError = typing_extensions.Annotated[
    typing.Union[JobResultsError_ResultsNotReady, JobResultsError_ResultsUnavailable],
    pydantic.Field(discriminator="code"),
]
