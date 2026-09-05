

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_spec import ContainerSpec
from .container_status import ContainerStatus
from .service_info import ServiceInfo


class Container(UniversalBaseModel):
    """
    Container resource representing a container instance
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the container instance
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource path identifier
    """

    spec: ContainerSpec
    status: typing.Optional[ContainerStatus] = None
    service: typing.Optional[ServiceInfo] = None
    create_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the container was created
    """

    update_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the container was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
