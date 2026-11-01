

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_result_response_with_context import TestResultResponseWithContext


class TestResultSearchResponseWithContext(UniversalBaseModel):
    """
    Response model for test results search endpoint with full context
    """

    count: int
    limit: int
    offset: int
    test_results: typing.List[TestResultResponseWithContext]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
