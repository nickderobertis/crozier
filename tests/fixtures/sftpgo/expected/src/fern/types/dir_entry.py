

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DirEntry(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the file (or subdirectory) described by the entry. This name is the final element of the path (the base name), not the entire path
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    file size, omitted for folders and non regular files
    """

    mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    File mode and permission bits. More details here: https://golang.org/pkg/io/fs/#FileMode.
    Let's see some examples:
    - for a directory mode&2147483648 != 0
    - for a symlink mode&134217728 != 0
    - for a regular file mode&2401763328 == 0
    """

    last_modified: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
