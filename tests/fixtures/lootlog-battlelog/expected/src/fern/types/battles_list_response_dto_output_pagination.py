

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BattlesListResponseDtoOutputPagination(UniversalBaseModel):
    size: float
    has_next: typing_extensions.Annotated[bool, FieldMetadata(alias="hasNext"), pydantic.Field(alias="hasNext")]
    has_prev: typing_extensions.Annotated[bool, FieldMetadata(alias="hasPrev"), pydantic.Field(alias="hasPrev")]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextCursor"), pydantic.Field(alias="nextCursor")
    ] = None
    previous_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="previousCursor"), pydantic.Field(alias="previousCursor")
    ] = None
    total: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
