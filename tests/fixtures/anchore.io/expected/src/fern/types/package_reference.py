

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PackageReference(UniversalBaseModel):
    """
    A record of a software item which is vulnerable or carries a fix for a vulnerability
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Package name
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Package type (e.g. package, rpm, deb, apk, jar, npm, gem, ...)
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    A version for the package. If null, then references all versions
    """

    will_not_fix: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a vendor will or will not fix a vulnerabitlity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
