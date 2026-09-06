

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_links_opengraph_debug_response_og_tags_item import PostLinksOpengraphDebugResponseOgTagsItem


class PostLinksOpengraphDebugResponse(UniversalBaseModel):
    title: typing.Optional[str] = None
    og_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[PostLinksOpengraphDebugResponseOgTagsItem]],
        FieldMetadata(alias="ogTags"),
        pydantic.Field(alias="ogTags"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
