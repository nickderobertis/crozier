

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_meta_data_get import FileMetaDataGet


class PathMetaDataGet(UniversalBaseModel):
    path: str = pydantic.Field()
    """
    the path to the current path
    """

    display_path: str = pydantic.Field()
    """
    the path to display with UUID replaced (URL Encoded by parts as names may contain '/')
    """

    file_meta_data: typing.Optional[FileMetaDataGet] = pydantic.Field(default=None)
    """
    if filled, this is the file meta data of the s3 object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
