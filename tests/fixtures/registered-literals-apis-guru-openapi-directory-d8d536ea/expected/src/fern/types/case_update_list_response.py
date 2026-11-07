

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_update_preview import CaseUpdatePreview


class CaseUpdateListResponse(UniversalBaseModel):
    case_update_preview_array: typing_extensions.Annotated[
        typing.List[CaseUpdatePreview],
        FieldMetadata(alias="caseUpdatePreviewArray"),
        pydantic.Field(alias="caseUpdatePreviewArray", description="Array of case update objects."),
    ]
    """
    Array of case update objects.
    """

    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Link for the next page."),
    ] = None
    """
    Link for the next page.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    page_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber", description="Current page number.")
    ]
    """
    Current page number.
    """

    previous_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousPageAPI"),
        pydantic.Field(alias="previousPageAPI", description="Link for the previous page."),
    ] = None
    """
    Link for the previous page.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total number of case update objects available."),
    ]
    """
    Total number of case update objects available.
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Total number of pages available."),
    ]
    """
    Total number of pages available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
