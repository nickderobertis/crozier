

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_part_file import FilePartFile


class FilePart(UniversalBaseModel):
    """
    Represents a file segment within a message or artifact. The file content can be
    provided either directly as bytes or as a URI.
    """

    file: FilePartFile
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
