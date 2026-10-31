

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_result_status import TestResultStatus


class PreviousTestResult(UniversalBaseModel):
    status: TestResultStatus
    version: str
    artefact_id: int
    test_execution_id: int
    test_result_id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
