

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodeScreenshot(UniversalBaseModel):
    thumbnail_url: str
    file_url: str
    mimetype: typing.Optional[str] = pydantic.Field(default=None)
    """
    File's media type or None if unknown. SEE https://www.iana.org/assignments/media-types/media-types.xhtml
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
