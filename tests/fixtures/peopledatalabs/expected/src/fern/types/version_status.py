

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .version_status_status import VersionStatusStatus


class VersionStatus(UniversalBaseModel):
    contains: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of IDs merged into this record since the last release
    """

    current_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current version of the data
    """

    previous_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Previous version of the data
    """

    status: typing.Optional[VersionStatusStatus] = pydantic.Field(default=None)
    """
    Explains what happened to this record between the previous release and the current release
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
