

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .check_result import CheckResult
from .comprehensive_check_response_overall_risk import ComprehensiveCheckResponseOverallRisk


class ComprehensiveCheckResponse(UniversalBaseModel):
    check_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="checkId"), pydantic.Field(alias="checkId")
    ] = None
    results: typing.Optional[typing.Dict[str, CheckResult]] = None
    overall_risk: typing_extensions.Annotated[
        typing.Optional[ComprehensiveCheckResponseOverallRisk],
        FieldMetadata(alias="overallRisk"),
        pydantic.Field(alias="overallRisk"),
    ] = None
    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
