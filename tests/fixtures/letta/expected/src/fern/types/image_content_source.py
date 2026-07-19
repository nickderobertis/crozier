

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImageContentSource_Base64(UniversalBaseModel):
    """
    The source of the image.
    """

    type: typing.Literal["base64"] = "base64"
    media_type: str
    data: str
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ImageContentSource_Letta(UniversalBaseModel):
    """
    The source of the image.
    """

    type: typing.Literal["letta"] = "letta"
    file_id: str
    media_type: typing.Optional[str] = None
    data: typing.Optional[str] = None
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ImageContentSource_Url(UniversalBaseModel):
    """
    The source of the image.
    """

    type: typing.Literal["url"] = "url"
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ImageContentSource = typing_extensions.Annotated[
    typing.Union[ImageContentSource_Base64, ImageContentSource_Letta, ImageContentSource_Url],
    pydantic.Field(discriminator="type"),
]
