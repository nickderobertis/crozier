

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Hash(UniversalBaseModel):
    """
    Hash information of a file
    """

    sha1: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA1 checksum of the file
    """

    md5: typing.Optional[str] = pydantic.Field(default=None)
    """
    MD5 checksum of the file
    """

    sha256: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA256 checksum of the file
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the file in bytes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
