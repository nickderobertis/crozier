

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_user_search_response_detail import UserUserSearchResponseDetail


class UserUserSearchResponse(UniversalBaseModel):
    has_more: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasMore"), pydantic.Field(alias="hasMore")
    ] = None
    page: typing.Optional[int] = None
    search_results: typing_extensions.Annotated[
        typing.Optional[typing.List[UserUserSearchResponseDetail]],
        FieldMetadata(alias="searchResults"),
        pydantic.Field(alias="searchResults"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
