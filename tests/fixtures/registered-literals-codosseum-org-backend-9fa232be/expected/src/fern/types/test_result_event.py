

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .test_result_event_result import TestResultEventResult


class TestResultEvent(UniversalBaseModel):
    """
    Sent (asynchronously) in response to a request asking to run a test for a solution.
    This event is sent for every individual test that fails or succeeds.
    """

    test_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="testId"),
        pydantic.Field(
            alias="testId",
            description="the ID returned when the test runs were requested. This can be used to determine the state of the solution when the test request was made.",
        ),
    ] = None
    """
    the ID returned when the test runs were requested. This can be used to determine the state of the solution when the test request was made.
    """

    num: typing.Optional[int] = pydantic.Field(default=None)
    """
    Test number that was run
    """

    result: typing.Optional[TestResultEventResult] = pydantic.Field(default=None)
    """
    Test result. input, expectedOutput and actualOutput are only sent if the test failed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
