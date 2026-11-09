

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .associated_norm_judge import AssociatedNormJudge


class AssociatedNormJudgeResponse(UniversalBaseModel):
    associated_norm_judge_array: typing_extensions.Annotated[
        typing.List[AssociatedNormJudge],
        FieldMetadata(alias="associatedNormJudgeArray"),
        pydantic.Field(alias="associatedNormJudgeArray"),
    ]
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Next page of results if applicable."),
    ] = None
    """
    Next page of results if applicable.
    """

    previous_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousPageAPI"),
        pydantic.Field(alias="previousPageAPI", description="Previous page of results if applicable."),
    ] = None
    """
    Previous page of results if applicable.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total no. of results for this criteria."),
    ]
    """
    Total no. of results for this criteria.
    """

    total_pages: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages", description="Total no. of pages.")
    ]
    """
    Total no. of pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
