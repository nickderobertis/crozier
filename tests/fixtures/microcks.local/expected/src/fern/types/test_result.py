

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operation_headers import OperationHeaders
from .secret_ref import SecretRef
from .test_case_result import TestCaseResult
from .test_runner_type import TestRunnerType


class TestResult(UniversalBaseModel):
    """
    Represents the result of a Service or API test run by Microcks. Tests are related to a service and made of multiple test cases corresponding to each operations / actions composing service. Tests are run against a specific endpoint named testedEndpoint. It holds global markers telling if test still ran, is a success, how many times is has taken and so on ...
    """

    elapsed_time: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="elapsedTime")] = (
        pydantic.Field(default=None)
    )
    """
    Elapsed time in milliseconds since test beginning
    """

    id: str = pydantic.Field()
    """
    Unique identifier of TestResult
    """

    in_progress: typing_extensions.Annotated[bool, FieldMetadata(alias="inProgress")] = pydantic.Field()
    """
    Flag telling is test is still in progress
    """

    operation_headers: typing_extensions.Annotated[
        typing.Optional[OperationHeaders], FieldMetadata(alias="operationHeaders")
    ] = pydantic.Field(default=None)
    """
    This test operations headers override
    """

    runner_type: typing_extensions.Annotated[TestRunnerType, FieldMetadata(alias="runnerType")] = pydantic.Field()
    """
    Runner used for this test
    """

    secret_ref: typing_extensions.Annotated[typing.Optional[SecretRef], FieldMetadata(alias="secretRef")] = (
        pydantic.Field(default=None)
    )
    """
    The referrence of the Secret used for connecting to test endpoint
    """

    service_id: typing_extensions.Annotated[str, FieldMetadata(alias="serviceId")] = pydantic.Field()
    """
    Unique identifier of service tested
    """

    success: bool = pydantic.Field()
    """
    Flag telling if test is a success
    """

    test_case_results: typing_extensions.Annotated[
        typing.Optional[typing.List[TestCaseResult]], FieldMetadata(alias="testCaseResults")
    ] = pydantic.Field(default=None)
    """
    TestCase results associated to this test
    """

    test_date: typing_extensions.Annotated[int, FieldMetadata(alias="testDate")] = pydantic.Field()
    """
    Timestamp of creation date of this service
    """

    test_number: typing_extensions.Annotated[float, FieldMetadata(alias="testNumber")] = pydantic.Field()
    """
    Incremental number for tracking number of tests of a service
    """

    tested_endpoint: typing_extensions.Annotated[str, FieldMetadata(alias="testedEndpoint")] = pydantic.Field()
    """
    Endpoint used during test
    """

    timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum time (in milliseconds) to wait for this test ends
    """

    version: float = pydantic.Field()
    """
    Revision number of this test
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
