

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .norm_judge_search_result import NormJudgeSearchResult


class NormJudgeSearchResponse(UniversalBaseModel):
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Link to next page."),
    ] = None
    """
    Link to next page.
    """

    norm_judge_search_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normJudgeSearchId"),
        pydantic.Field(alias="normJudgeSearchId", description="Query been sent by client"),
    ]
    """
    Query been sent by client
    """

    norm_judge_search_result_array: typing_extensions.Annotated[
        typing.List[NormJudgeSearchResult],
        FieldMetadata(alias="normJudgeSearchResultArray"),
        pydantic.Field(alias="normJudgeSearchResultArray"),
    ]
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
