

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_create2request_body_zero_type import FilesCreate2RequestBodyZeroType


class FilesCreate2RequestBodyZero(UniversalBaseModel):
    type: FilesCreate2RequestBodyZeroType
    content: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
