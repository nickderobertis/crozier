

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_create2request_body_one_type import FilesCreate2RequestBodyOneType


class FilesCreate2RequestBodyOne(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    File and val content. An empty string will create an empty file. When creating a directory, the content should be null or undefined.
    """

    type: FilesCreate2RequestBodyOneType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
