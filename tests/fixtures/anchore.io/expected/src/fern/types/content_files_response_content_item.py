

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContentFilesResponseContentItem(UniversalBaseModel):
    filename: typing.Optional[str] = None
    gid: typing.Optional[int] = None
    linkdest: typing.Optional[str] = None
    mode: typing.Optional[str] = None
    sha256: typing.Optional[str] = None
    size: typing.Optional[int] = None
    type: typing.Optional[str] = None
    uid: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
