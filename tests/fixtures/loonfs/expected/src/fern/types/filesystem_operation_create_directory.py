

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath


class FilesystemOperationCreateDirectory(UniversalBaseModel):
    """
    An operation that creates one directory.
    """

    parents: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the operation creates any missing ancestor directories. The final path component
    must still be new.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path of the new directory. The operation fails if the path is invalid or
    already bound.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
