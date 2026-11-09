

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_class import CaseClass


class CaseClassCoverage(UniversalBaseModel):
    case_class: typing_extensions.Annotated[
        CaseClass, FieldMetadata(alias="caseClass"), pydantic.Field(alias="caseClass")
    ]
    case_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="caseCount"),
        pydantic.Field(alias="caseCount", description="Total Cases for a specific CourtLocation."),
    ]
    """
    Total Cases for a specific CourtLocation.
    """

    case_document_in_library_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="caseDocumentInLibraryCount"),
        pydantic.Field(
            alias="caseDocumentInLibraryCount",
            description="Case Documents that were added to UniCourt Crowd Source Library for a specific CourtLocationy.",
        ),
    ]
    """
    Case Documents that were added to UniCourt Crowd Source Library for a specific CourtLocationy.
    """

    case_document_in_library_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="caseDocumentInLibraryInLastThirtyDaysCount"),
        pydantic.Field(
            alias="caseDocumentInLibraryInLastThirtyDaysCount",
            description="Case Documents that were added to UniCourt Crowd Source Library for a specific CourtLocation in last 30 days.",
        ),
    ]
    """
    Case Documents that were added to UniCourt Crowd Source Library for a specific CourtLocation in last 30 days.
    """

    cases_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="casesInLastThirtyDaysCount"),
        pydantic.Field(
            alias="casesInLastThirtyDaysCount",
            description="Cases in last 30 days that were added to UniCourt for a specific CourtLocation",
        ),
    ]
    """
    Cases in last 30 days that were added to UniCourt for a specific CourtLocation
    """

    court_service_status_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="courtServiceStatusAPI"),
        pydantic.Field(
            alias="courtServiceStatusAPI",
            description="API Link to the Court Service status with filters of court and case class",
        ),
    ]
    """
    API Link to the Court Service status with filters of court and case class
    """

    free_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="freeCaseDocumentCount"),
        pydantic.Field(alias="freeCaseDocumentCount", description="Free Case Documents for a specific CourtLocation."),
    ]
    """
    Free Case Documents for a specific CourtLocation.
    """

    free_case_documents_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="freeCaseDocumentsInLastThirtyDaysCount"),
        pydantic.Field(
            alias="freeCaseDocumentsInLastThirtyDaysCount",
            description="Free Case Documents in last 30 days that were added to UniCourt for a specific CourtLocation.",
        ),
    ]
    """
    Free Case Documents in last 30 days that were added to UniCourt for a specific CourtLocation.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    paid_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="paidCaseDocumentCount"),
        pydantic.Field(alias="paidCaseDocumentCount", description="Paid Case Documents for a specific CourtLocation."),
    ]
    """
    Paid Case Documents for a specific CourtLocation.
    """

    paid_case_documents_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="paidCaseDocumentsInLastThirtyDaysCount"),
        pydantic.Field(
            alias="paidCaseDocumentsInLastThirtyDaysCount",
            description="Paid Case Documents in last 30 days that were added to UniCourt for a specific CourtLocation.",
        ),
    ]
    """
    Paid Case Documents in last 30 days that were added to UniCourt for a specific CourtLocation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
