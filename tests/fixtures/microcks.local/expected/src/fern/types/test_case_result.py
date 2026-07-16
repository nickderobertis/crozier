

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .test_step_result import TestStepResult


class TestCaseResult(UniversalBaseModel):
    """
    Companion objects for TestResult. Each TestCaseResult correspond to a particuliar service operation / action reference by the operationName field. TestCaseResults owns a collection of TestStepResults (one for every request associated to service operation / action).
    """

    elapsed_time: typing_extensions.Annotated[float, FieldMetadata(alias="elapsedTime")] = pydantic.Field()
    """
    Elapsed time in milliseconds since the test case beginning
    """

    operation_name: typing_extensions.Annotated[str, FieldMetadata(alias="operationName")] = pydantic.Field()
    """
    Name of operation this test case is bound to
    """

    success: bool = pydantic.Field()
    """
    Flag telling if test case is a success
    """

    test_step_results: typing_extensions.Annotated[
        typing.Optional[typing.List[TestStepResult]], FieldMetadata(alias="testStepResults")
    ] = pydantic.Field(default=None)
    """
    Test steps associated to this test case
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
