

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artefact_build_minimal_response import ArtefactBuildMinimalResponse
from .artefact_response import ArtefactResponse
from .test_execution_response import TestExecutionResponse
from .test_result_response import TestResultResponse


class TestResultResponseWithContext(UniversalBaseModel):
    """
    Test result response with artefact and test execution context
    """

    test_result: TestResultResponse
    test_execution: TestExecutionResponse
    artefact: ArtefactResponse
    artefact_build: ArtefactBuildMinimalResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
