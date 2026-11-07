

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_search_result import CaseSearchResult


class CaseSearchResponse(UniversalBaseModel):
    case_search_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseSearchId"),
        pydantic.Field(alias="caseSearchId", description="Query been sent by client"),
    ]
    """
    Query been sent by client
    """

    case_search_result_array: typing_extensions.Annotated[
        typing.List[CaseSearchResult],
        FieldMetadata(alias="caseSearchResultArray"),
        pydantic.Field(alias="caseSearchResultArray"),
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
    page_number: typing_extensions.Annotated[int, FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber")]
    previous_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousPageAPI"),
        pydantic.Field(alias="previousPageAPI", description="Link to previous page."),
    ] = None
    """
    Link to previous page.
    """

    q: str = pydantic.Field()
    """
    Query been sent by client
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="The number of matches that were found in the index."),
    ]
    """
    The number of matches that were found in the index.
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Total pages for matches that were found in the index."),
    ]
    """
    Total pages for matches that were found in the index.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
