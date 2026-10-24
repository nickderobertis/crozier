

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_platform_relation_members_endpoint_output import GetPlatformRelationMembersEndpointOutput


class GetPlatformRelationMembersEndpointCursorPagedResultOfOutput(UniversalBaseModel):
    """
    A page of results identified by an opaque cursor rather than an offset. Used where the
    underlying store pages by continuation token and a total count is unavailable or expensive.
    string? CursorPagedResult&lt;T&gt;.NextCursor is null on the last page.
    """

    items: typing.List[GetPlatformRelationMembersEndpointOutput]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextCursor"), pydantic.Field(alias="nextCursor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
