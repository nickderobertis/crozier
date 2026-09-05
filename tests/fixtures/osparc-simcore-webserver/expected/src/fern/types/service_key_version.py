

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServiceKeyVersion(UniversalBaseModel):
    """
    Service `key-version` pair uniquely identifies a service
    """

    key: str = pydantic.Field()
    """
    distinctive name for the node based on the docker registry path
    """

    version: str = pydantic.Field()
    """
    service version number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
