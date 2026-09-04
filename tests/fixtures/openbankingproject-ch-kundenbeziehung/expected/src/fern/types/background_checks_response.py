

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .background_checks_response_overall_risk import BackgroundChecksResponseOverallRisk
from .check_result import CheckResult


class BackgroundChecksResponse(UniversalBaseModel):
    check_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="checkId"), pydantic.Field(alias="checkId")
    ] = None
    results: typing.Optional[typing.Dict[str, CheckResult]] = None
    overall_risk: typing_extensions.Annotated[
        typing.Optional[BackgroundChecksResponseOverallRisk],
        FieldMetadata(alias="overallRisk"),
        pydantic.Field(alias="overallRisk"),
    ] = None
    new_findings: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="newFindings"), pydantic.Field(alias="newFindings")
    ] = None
    recommended_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="recommendedActions"),
        pydantic.Field(alias="recommendedActions"),
    ] = None
    next_review_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="nextReviewDate"), pydantic.Field(alias="nextReviewDate")
    ] = None
    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
