

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_results_result_state import JobResultsResultState
from .result_intent import ResultIntent


class JobResults(UniversalBaseModel):
    result_state: typing_extensions.Annotated[
        JobResultsResultState, FieldMetadata(alias="resultState"), pydantic.Field(alias="resultState")
    ]
    intents: typing.List[ResultIntent]
    missing: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
