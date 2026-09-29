

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Pagination(UniversalBaseModel):
    has_more: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasMore"), pydantic.Field(alias="hasMore", description="Whether more results exist")
    ]
    """
    Whether more results exist
    """

    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(alias="nextCursor", description="Cursor for next page"),
    ] = None
    """
    Cursor for next page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
