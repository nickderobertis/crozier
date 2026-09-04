

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_results_error_results_unavailable_result_state import JobResultsErrorResultsUnavailableResultState
from .job_results_error_results_unavailable_state import JobResultsErrorResultsUnavailableState


class JobResultsErrorResultsUnavailable(UniversalBaseModel):
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
