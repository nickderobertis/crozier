

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VersionInfo(UniversalBaseModel):
    """
    Version information.
    """

    git_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The git version (including git commit hash)
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of Airflow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
