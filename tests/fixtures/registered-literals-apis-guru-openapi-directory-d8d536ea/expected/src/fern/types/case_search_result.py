

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_status import CaseStatus
from .case_type import CaseType
from .court import Court
from .court_location import CourtLocation
from .matched_object import MatchedObject


class CaseSearchResult(UniversalBaseModel):
    case_api: typing_extensions.Annotated[str, FieldMetadata(alias="caseAPI"), pydantic.Field(alias="caseAPI")]
    case_id: typing_extensions.Annotated[str, FieldMetadata(alias="caseId"), pydantic.Field(alias="caseId")]
    case_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caseName"), pydantic.Field(alias="caseName")
    ] = None
    case_number: typing_extensions.Annotated[str, FieldMetadata(alias="caseNumber"), pydantic.Field(alias="caseNumber")]
    case_status: typing_extensions.Annotated[
        typing.Optional[CaseStatus], FieldMetadata(alias="caseStatus"), pydantic.Field(alias="caseStatus")
    ] = None
    case_type: typing_extensions.Annotated[
        typing.Optional[CaseType], FieldMetadata(alias="caseType"), pydantic.Field(alias="caseType")
    ] = None
    court: typing.Optional[Court] = None
    court_location: typing_extensions.Annotated[
        typing.Optional[CourtLocation], FieldMetadata(alias="courtLocation"), pydantic.Field(alias="courtLocation")
    ] = None
    filed_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="filedDate"), pydantic.Field(alias="filedDate")
    ]
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstFetchDate"), pydantic.Field(alias="firstFetchDate")
    ]
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastFetchDate"), pydantic.Field(alias="lastFetchDate")
    ]
    last_fetch_date_with_updates: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastFetchDateWithUpdates"), pydantic.Field(alias="lastFetchDateWithUpdates")
    ]
    matched_object_array: typing_extensions.Annotated[
        typing.List[typing.Optional[MatchedObject]],
        FieldMetadata(alias="matchedObjectArray"),
        pydantic.Field(alias="matchedObjectArray"),
    ]
    object: str
    participants_last_fetch_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="participantsLastFetchDate"),
        pydantic.Field(alias="participantsLastFetchDate"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
