

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseStats(UniversalBaseModel):
    """
    Count of each entitiy of a case is mentioned here so that you can calculate the number of requests needs to be done to obtain each entity results completely.
    """

    all_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="allCaseDocumentCount"),
        pydantic.Field(
            alias="allCaseDocumentCount",
            description="Count which includes the freeCaseDocumentCount and paidCaseDocumentCount.",
        ),
    ]
    """
    Count which includes the freeCaseDocumentCount and paidCaseDocumentCount.
    """

    attorney_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="attorneyCount"),
        pydantic.Field(
            alias="attorneyCount", description="Count of number of attornies available in the case being requested for."
        ),
    ]
    """
    Count of number of attornies available in the case being requested for.
    """

    case_document_in_library_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="caseDocumentInLibraryCount"),
        pydantic.Field(
            alias="caseDocumentInLibraryCount",
            description="Count of number of documents that are available in the UniCourt CrowdSourced Library for the case being requested for.",
        ),
    ]
    """
    Count of number of documents that are available in the UniCourt CrowdSourced Library for the case being requested for.
    """

    docket_entry_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="docketEntryCount"),
        pydantic.Field(
            alias="docketEntryCount",
            description="Count of number of docket entries available in the case being requested for.",
        ),
    ]
    """
    Count of number of docket entries available in the case being requested for.
    """

    free_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="freeCaseDocumentCount"),
        pydantic.Field(
            alias="freeCaseDocumentCount",
            description="Count of number of free documents available in the case being requested for.",
        ),
    ]
    """
    Count of number of free documents available in the case being requested for.
    """

    hearing_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="hearingCount"),
        pydantic.Field(
            alias="hearingCount", description="Count of number of hearings available in the case being requested for."
        ),
    ]
    """
    Count of number of hearings available in the case being requested for.
    """

    judge_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="judgeCount"),
        pydantic.Field(
            alias="judgeCount", description="Count of number of judges available in the case being requested for."
        ),
    ]
    """
    Count of number of judges available in the case being requested for.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    paid_case_document_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="paidCaseDocumentCount"),
        pydantic.Field(
            alias="paidCaseDocumentCount",
            description="Count of number of paid documents available in the case being requested for.",
        ),
    ]
    """
    Count of number of paid documents available in the case being requested for.
    """

    party_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="partyCount"),
        pydantic.Field(
            alias="partyCount", description="Count of number of parties available in the case being requested for."
        ),
    ]
    """
    Count of number of parties available in the case being requested for.
    """

    related_case_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="relatedCaseCount"),
        pydantic.Field(
            alias="relatedCaseCount",
            description="Count of related cases that are available in the case being requested.",
        ),
    ]
    """
    Count of related cases that are available in the case being requested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
