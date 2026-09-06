

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_links_examples_response_links_item import PostLinksExamplesResponseLinksItem


class PostLinksExamplesResponse(UniversalBaseModel):
    success: bool
    links: typing.List[PostLinksExamplesResponseLinksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
