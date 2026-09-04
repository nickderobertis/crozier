

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PaginationDetails(UniversalBaseModel):
    has_next: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasNext"),
        pydantic.Field(
            alias="hasNext",
            description="A flag indicating whether there is another page of results to fetch.\n\nWhen `hasNext` is `true`, `nextPageToken` MUST be present.\nWhen `hasNext` is `false`, `nextPageToken` MUST NOT be included.",
        ),
    ]
    """
    A flag indicating whether there is another page of results to fetch.
    
    When `hasNext` is `true`, `nextPageToken` MUST be present.
    When `hasNext` is `false`, `nextPageToken` MUST NOT be included.
    """

    next_page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageToken"),
        pydantic.Field(
            alias="nextPageToken",
            description="An opaque token that can be used in a following request to retrieve the next page of results.\n\nThis field MUST be present when `hasNext` is `true`.\nThis field MUST NOT be included when `hasNext` is `false`.",
        ),
    ] = None
    """
    An opaque token that can be used in a following request to retrieve the next page of results.
    
    This field MUST be present when `hasNext` is `true`.
    This field MUST NOT be included when `hasNext` is `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
