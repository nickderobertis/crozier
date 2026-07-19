

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerMappingMxfContainer(UniversalBaseModel):
    """
    Mapping to Material Exchange Format containers, SMPTE ST 377-1
    """

    package_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The package UID. Either a SMPTE UMID URN or UUID URN
    """

    track_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The track ID in the package
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
