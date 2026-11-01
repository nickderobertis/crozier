

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paragraph_block_request_paragraph import ParagraphBlockRequestParagraph


class ParagraphBlockRequest(UniversalBaseModel):
    paragraph: typing.Optional[ParagraphBlockRequestParagraph] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
