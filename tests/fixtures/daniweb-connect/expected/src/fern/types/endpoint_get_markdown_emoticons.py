

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_get_markdown_emoticons_data_item import EndpointGetMarkdownEmoticonsDataItem


class EndpointGetMarkdownEmoticons(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointGetMarkdownEmoticonsDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
