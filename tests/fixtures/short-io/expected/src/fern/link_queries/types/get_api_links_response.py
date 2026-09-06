

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_api_links_response_links_item import GetApiLinksResponseLinksItem


class GetApiLinksResponse(UniversalBaseModel):
    count: int
    links: typing.List[GetApiLinksResponseLinksItem]
    next_page_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextPageToken"), pydantic.Field(alias="nextPageToken")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
