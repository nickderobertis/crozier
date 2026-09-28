

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contract_test_report_results_item import ContractTestReportResultsItem


class ContractTestReport(UniversalBaseModel):
    """
    the result of a contract test run
    """

    base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="baseUrl"), pydantic.Field(alias="baseUrl")
    ] = None
    total_operations: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalOperations"), pydantic.Field(alias="totalOperations")
    ] = None
    passed: typing.Optional[int] = None
    failed: typing.Optional[int] = None
    all_passed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allPassed"), pydantic.Field(alias="allPassed")
    ] = None
    results: typing.Optional[typing.List[ContractTestReportResultsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
