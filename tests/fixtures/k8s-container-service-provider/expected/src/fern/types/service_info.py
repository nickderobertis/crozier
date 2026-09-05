

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_info_type import ServiceInfoType
from .service_port import ServicePort


class ServiceInfo(UniversalBaseModel):
    """
    Kubernetes Service details
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Kubernetes Service
    """

    cluster_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cluster-internal IP address
    """

    type: typing.Optional[ServiceInfoType] = pydantic.Field(default=None)
    """
    Service type
    """

    external_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    External IP address (for LoadBalancer type)
    """

    ports: typing.Optional[typing.List[ServicePort]] = pydantic.Field(default=None)
    """
    Service ports
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
