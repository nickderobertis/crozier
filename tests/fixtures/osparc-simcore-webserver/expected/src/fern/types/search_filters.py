

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_timerange_filter import SearchTimerangeFilter


class SearchFilters(UniversalBaseModel):
    name_pattern: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="namePattern"),
        pydantic.Field(
            alias="namePattern",
            description="Name pattern with wildcard support (*, ?). Minimum of 3 non-wildcard characters required.",
        ),
    ]
    """
    Name pattern with wildcard support (*, ?). Minimum of 3 non-wildcard characters required.
    """

    modified_at: typing_extensions.Annotated[
        typing.Optional[SearchTimerangeFilter],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(alias="modifiedAt", description="Filter results based on modification date range"),
    ] = None
    """
    Filter results based on modification date range
    """

    project_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="projectId"),
        pydantic.Field(alias="projectId", description="If provided, only files within this project are searched"),
    ] = None
    """
    If provided, only files within this project are searched
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
