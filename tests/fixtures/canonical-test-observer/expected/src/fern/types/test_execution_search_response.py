

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_execution_response_with_context import TestExecutionResponseWithContext


class TestExecutionSearchResponse(UniversalBaseModel):
    count: int
    limit: int
    offset: int
    test_executions: typing.List[TestExecutionResponseWithContext]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
