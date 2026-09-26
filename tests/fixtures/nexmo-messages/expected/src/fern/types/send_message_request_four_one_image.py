

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageRequestFourOneImage(UniversalBaseModel):
    caption: typing.Optional[str] = pydantic.Field(default=None)
    """
    A caption to accompany the image. Required if the message includes an action button.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the image attachment.
    
    Supports `.jpg`, `.jpeg`, and `.png`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
