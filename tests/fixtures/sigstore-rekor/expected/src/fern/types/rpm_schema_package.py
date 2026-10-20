

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rpm_schema_package_hash import RpmSchemaPackageHash


class RpmSchemaPackage(UniversalBaseModel):
    """
    Information about the package associated with the entry
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Values of the RPM headers
    """

    hash: typing.Optional[RpmSchemaPackageHash] = pydantic.Field(default=None)
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
