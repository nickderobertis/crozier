

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetImageOembedResponse(UniversalBaseModel):
    version: typing.Optional[str] = None
    type: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    title: typing.Optional[str] = None
    author_name: typing.Optional[str] = None
    author_url: typing.Optional[str] = None
    license_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
