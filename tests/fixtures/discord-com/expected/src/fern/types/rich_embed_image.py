

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RichEmbedImage(UniversalBaseModel):
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    placeholder: typing.Optional[str] = None
    placeholder_version: typing.Optional[int] = None
    is_animated: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
