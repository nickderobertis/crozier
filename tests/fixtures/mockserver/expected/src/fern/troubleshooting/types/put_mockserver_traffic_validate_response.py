

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .put_mockserver_traffic_validate_response_results_item import PutMockserverTrafficValidateResponseResultsItem


class PutMockserverTrafficValidateResponse(UniversalBaseModel):
    total_requests: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalRequests"), pydantic.Field(alias="totalRequests")
    ] = None
    passed: typing.Optional[int] = None
    failed: typing.Optional[int] = None
    all_passed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allPassed"), pydantic.Field(alias="allPassed")
    ] = None
    results: typing.Optional[typing.List[PutMockserverTrafficValidateResponseResultsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
