

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_port import ContainerPort


class ContainerNetwork(UniversalBaseModel):
    """
    Network configuration
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pod IP address
    """

    ports: typing.Optional[typing.List[ContainerPort]] = pydantic.Field(default=None)
    """
    Container ports to expose
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
