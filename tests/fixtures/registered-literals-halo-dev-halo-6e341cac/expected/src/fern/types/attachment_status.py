

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AttachmentStatus(UniversalBaseModel):
    """
    Observed attachment access state.
    """

    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Public permalink for the attachment. Local storage usually exposes a public URL, while object storage may
     expose the object URL.
    """

    thumbnails: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Generated thumbnail URLs keyed by thumbnail size name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
