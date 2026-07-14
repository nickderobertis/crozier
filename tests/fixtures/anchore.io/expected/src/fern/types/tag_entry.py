

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TagEntry(UniversalBaseModel):
    """
    A docker-pullable tag value as well as deconstructed components
    """

    detected_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp at which the Anchore Engine detected this tag was mapped to the image digest. Does not necessarily indicate when the tag was actually pushed to the registry.
    """

    pullstring: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pullable string for the tag. E.g. "docker.io/library/node:latest"
    """

    registry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The registry hostname:port section of the pull string
    """

    repository: typing.Optional[str] = pydantic.Field(default=None)
    """
    The repository section of the pull string
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag-only section of the pull string
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
