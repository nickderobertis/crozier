

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artefact_build_minimal_response import ArtefactBuildMinimalResponse
from .artefact_response import ArtefactResponse
from .environment_response import EnvironmentResponse
from .execution_metadata import ExecutionMetadata
from .test_execution_relevant_link_response import TestExecutionRelevantLinkResponse
from .test_execution_status import TestExecutionStatus
from .test_result_response import TestResultResponse


class TestExecutionResponseWithContext(UniversalBaseModel):
    id: int
    ci_link: typing.Optional[str] = None
    c3link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="c3_link"), pydantic.Field(alias="c3_link")
    ] = None
    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkResponse]] = None
    environment: EnvironmentResponse
    status: TestExecutionStatus
    test_plan: str
    created_at: dt.datetime
    execution_metadata: ExecutionMetadata
    is_triaged: bool
    artefact: ArtefactResponse
    artefact_build: ArtefactBuildMinimalResponse
    test_results: typing.Optional[typing.List[TestResultResponse]] = None
    is_rerun_requested: typing.Optional[bool] = None
    rerun_priority: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
