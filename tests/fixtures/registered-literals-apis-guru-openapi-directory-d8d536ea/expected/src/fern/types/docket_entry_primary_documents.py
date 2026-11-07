

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_document import CaseDocument


class DocketEntryPrimaryDocuments(UniversalBaseModel):
    """
    Primary Documents refers to documents that are directly related to a docket entry. Primary Documents could be specific to a courts or case type in courts. For isntance the below example is in PACER. PACER District Courts - Here the primary document is one which is attached to the docket number. Because in district for a primary document it can have many attachments associatated to it. PACER Appeal Courts - Here the attachments for a docket entry are the primary documents. Because in appeal for those attachments there is no primary documents.
    """

    case_document_array: typing_extensions.Annotated[
        typing.List[typing.Optional[CaseDocument]],
        FieldMetadata(alias="caseDocumentArray"),
        pydantic.Field(alias="caseDocumentArray"),
    ]
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Link to next page of a particular entity in a Case."),
    ] = None
    """
    Link to next page of a particular entity in a Case.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    page_number: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pageNumber"),
        pydantic.Field(alias="pageNumber", description="Page number for which results where obtained."),
    ]
    """
    Page number for which results where obtained.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total number of parties of the Case. entity in a Case."),
    ]
    """
    Total number of parties of the Case. entity in a Case.
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(
            alias="totalPages", description="Total number of pages to obtain all the objects of a party in the Case."
        ),
    ]
    """
    Total number of pages to obtain all the objects of a party in the Case.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
