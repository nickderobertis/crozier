

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CursorPaginationInfoDto(UniversalBaseModel):
    has_next: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasNext"),
        pydantic.Field(alias="hasNext", description="Indicates whether there are more results available"),
    ]
    """
    Indicates whether there are more results available
    """

    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor",
            description="Cursor to use for fetching the next page of results. Can be omit when hasNext is false. ",
        ),
    ] = None
    """
    Cursor to use for fetching the next page of results. Can be omit when hasNext is false. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
