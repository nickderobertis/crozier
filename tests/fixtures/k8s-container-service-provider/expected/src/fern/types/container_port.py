

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_port_visibility import ContainerPortVisibility


class ContainerPort(UniversalBaseModel):
    """
    Container port definition
    """

    container_port: int = pydantic.Field()
    """
    Port number inside container
    """

    visibility: ContainerPortVisibility = pydantic.Field()
    """
    How this port is exposed to consumers.
    - none: Port is not exposed outside the container process
    - internal: Exposed to the host or cluster network
      (e.g., Docker -p, Kubernetes ClusterIP Service)
    - external: Reachable from outside the host/cluster
      (e.g., OpenShift Route, Kubernetes Ingress/LoadBalancer)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
