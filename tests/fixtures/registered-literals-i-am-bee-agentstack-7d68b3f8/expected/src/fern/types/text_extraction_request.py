

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_extraction_settings import TextExtractionSettings


class TextExtractionRequest(UniversalBaseModel):
    """
    Request schema for text extraction.
    """

    settings: typing.Optional[TextExtractionSettings] = pydantic.Field(default=None)
    """
    Additional options for text extraction
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
