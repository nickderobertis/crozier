

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_results_error_results_not_ready_result_state import JobResultsErrorResultsNotReadyResultState
from .job_results_error_results_not_ready_state import JobResultsErrorResultsNotReadyState


class JobResultsErrorResultsNotReady(UniversalBaseModel):
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
