

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_class_coverage import CaseClassCoverage
from .court import Court


class CourtCoverage(UniversalBaseModel):
    case_class_coverage_array: typing_extensions.Annotated[
        typing.List[typing.Optional[CaseClassCoverage]],
        FieldMetadata(alias="caseClassCoverageArray"),
        pydantic.Field(alias="caseClassCoverageArray"),
    ]
    court: typing.Optional[Court] = None
    last_update_count_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastUpdateCountDate"),
        pydantic.Field(alias="lastUpdateCountDate", description="Date when it was last updated."),
    ]
    """
    Date when it was last updated.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    total_case_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCaseCount"),
        pydantic.Field(alias="totalCaseCount", description="Total Cases for a specific court."),
    ]
    """
    Total Cases for a specific court.
    """

    total_case_document_in_library_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCaseDocumentInLibraryCount"),
        pydantic.Field(
            alias="totalCaseDocumentInLibraryCount",
            description="Count of total Case Documents added in UniCourt Library.",
        ),
    ]
    """
    Count of total Case Documents added in UniCourt Library.
    """

    total_case_document_in_library_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCaseDocumentInLibraryInLastThirtyDaysCount"),
        pydantic.Field(
            alias="totalCaseDocumentInLibraryInLastThirtyDaysCount",
            description="Count of total Case Documents added in UniCourt Library in last 30 days",
        ),
    ]
    """
    Count of total Case Documents added in UniCourt Library in last 30 days
    """

    total_cases_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCasesInLastThirtyDaysCount"),
        pydantic.Field(
            alias="totalCasesInLastThirtyDaysCount",
            description="Total Cases in last 30 days that were added to UniCourt",
        ),
    ]
    """
    Total Cases in last 30 days that were added to UniCourt
    """

    total_free_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalFreeCaseDocumentCount"),
        pydantic.Field(
            alias="totalFreeCaseDocumentCount", description="Total Free Case Documents for a specific court."
        ),
    ]
    """
    Total Free Case Documents for a specific court.
    """

    total_free_case_documents_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalFreeCaseDocumentsInLastThirtyDaysCount"),
        pydantic.Field(
            alias="totalFreeCaseDocumentsInLastThirtyDaysCount",
            description="Total Free Case Documents in last 30 days that were added to UniCourt",
        ),
    ]
    """
    Total Free Case Documents in last 30 days that were added to UniCourt
    """

    total_paid_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPaidCaseDocumentCount"),
        pydantic.Field(
            alias="totalPaidCaseDocumentCount", description="Total Paid Case Documents for a specific court."
        ),
    ]
    """
    Total Paid Case Documents for a specific court.
    """

    total_paid_case_documents_in_last_thirty_days_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPaidCaseDocumentsInLastThirtyDaysCount"),
        pydantic.Field(
            alias="totalPaidCaseDocumentsInLastThirtyDaysCount",
            description="Total Paid Case Documents in last 30 days that were added to UniCourt",
        ),
    ]
    """
    Total Paid Case Documents in last 30 days that were added to UniCourt
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
