

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .neutral_job_status_error_result_state import NeutralJobStatusErrorResultState


class NeutralJobStatusError(UniversalBaseModel):
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
