

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alpine_package_schema_package_hash import AlpinePackageSchemaPackageHash


class AlpinePackageSchemaPackage(UniversalBaseModel):
    """
    Information about the package associated with the entry
    """

    pkginfo: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Values of the .PKGINFO key / value pairs
    """

    hash: typing.Optional[AlpinePackageSchemaPackageHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value for the package
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the package inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
