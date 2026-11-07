

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_document_estimated_order_duration import CaseDocumentEstimatedOrderDuration
from .case_document_source_data_status import CaseDocumentSourceDataStatus
from .preview_document import PreviewDocument


class CaseDocument(UniversalBaseModel):
    added_to_library_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addedToLibraryDate"),
        pydantic.Field(
            alias="addedToLibraryDate",
            description="Date and time when the document was downloaded and added to the UniCourt Crowd Source Library.",
        ),
    ] = None
    """
    Date and time when the document was downloaded and added to the UniCourt Crowd Source Library.
    """

    case_document_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseDocumentId"),
        pydantic.Field(alias="caseDocumentId", description="UniCourt's Case Document ID."),
    ]
    """
    UniCourt's Case Document ID.
    """

    child_document_id_array: typing_extensions.Annotated[
        typing.List[typing.Optional[str]],
        FieldMetadata(alias="childDocumentIdArray"),
        pydantic.Field(
            alias="childDocumentIdArray",
            description="List of child document ID's if exists or else it will be an empty lsit.",
        ),
    ]
    """
    List of child document ID's if exists or else it will be an empty lsit.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the document.
    """

    document_filed_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentFiledDate"),
        pydantic.Field(
            alias="documentFiledDate",
            description="Document Date when it was filed. The document date will be either explicitly provided byt the court or if the document is associatated to a docket entry then the document date will be of docket entry date.",
        ),
    ] = None
    """
    Document Date when it was filed. The document date will be either explicitly provided byt the court or if the document is associatated to a docket entry then the document date will be of docket entry date.
    """

    download_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="downloadAPI"),
        pydantic.Field(
            alias="downloadAPI",
            description="Link to either view the document if it is downloaded and already present in the UniCourt CrowdSourced Library.",
        ),
    ] = None
    """
    Link to either view the document if it is downloaded and already present in the UniCourt CrowdSourced Library.
    """

    estimated_order_duration: typing_extensions.Annotated[
        CaseDocumentEstimatedOrderDuration,
        FieldMetadata(alias="estimatedOrderDuration"),
        pydantic.Field(alias="estimatedOrderDuration", description="Estimated duration of a Order."),
    ]
    """
    Estimated duration of a Order.
    """

    first_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(
            alias="firstFetchDate", description="Is the date when the document was first fetched from the court site."
        ),
    ]
    """
    Is the date when the document was first fetched from the court site.
    """

    in_library: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="inLibrary"),
        pydantic.Field(
            alias="inLibrary", description="Determines if the document is present in the UniCourt Library or not."
        ),
    ]
    """
    Determines if the document is present in the UniCourt Library or not.
    """

    is_preview_available: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isPreviewAvailable"),
        pydantic.Field(
            alias="isPreviewAvailable", description="Determines if a preview is available for the case document."
        ),
    ]
    """
    Determines if a preview is available for the case document.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document name.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    pages: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of pages in the document.
    """

    parent_document_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentDocumentId"),
        pydantic.Field(
            alias="parentDocumentId",
            description="Document ID which is the parent document for the current document. This will be null if the current document is a parent document.",
        ),
    ] = None
    """
    Document ID which is the parent document for the current document. This will be null if the current document is a parent document.
    """

    preview_document: typing_extensions.Annotated[
        typing.Optional[PreviewDocument],
        FieldMetadata(alias="previewDocument"),
        pydantic.Field(alias="previewDocument"),
    ] = None
    price: typing.Optional[float] = pydantic.Field(default=None)
    """
    Price of the document.
    """

    sort_order: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder", description="Order of documents how it is being stored in UniCourt."),
    ] = None
    """
    Order of documents how it is being stored in UniCourt.
    """

    source_data_status: typing_extensions.Annotated[
        typing.Optional[CaseDocumentSourceDataStatus],
        FieldMetadata(alias="sourceDataStatus"),
        pydantic.Field(
            alias="sourceDataStatus",
            description="The status of source data of document. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Document has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site.",
        ),
    ] = None
    """
    The status of source data of document. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Document has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
