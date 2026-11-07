

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_class import CaseClass


class CaseClassResponse(UniversalBaseModel):
    case_class_array: typing_extensions.Annotated[
        typing.List[CaseClass], FieldMetadata(alias="caseClassArray"), pydantic.Field(alias="caseClassArray")
    ]
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Link to next page."),
    ] = None
    """
    Link to next page.
    """

    object: str
    page_number: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pageNumber"),
        pydantic.Field(alias="pageNumber", description="Page number for which results where obtained."),
    ]
    """
    Page number for which results where obtained.
    """

    previous_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousPageAPI"),
        pydantic.Field(alias="previousPageAPI", description="Link to previous page."),
    ] = None
    """
    Link to previous page.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total number of matches found."),
    ]
    """
    Total number of matches found.
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Total number of pages to obtain all the objects."),
    ]
    """
    Total number of pages to obtain all the objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
