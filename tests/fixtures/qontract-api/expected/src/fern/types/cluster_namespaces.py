

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .desired_namespace import DesiredNamespace
from .secret import Secret


class ClusterNamespaces(UniversalBaseModel):
    """
    Cluster with its desired namespaces and connection info.
    """

    automation_token: Secret = pydantic.Field()
    """
    Vault reference for the automation token (NOT the actual token)
    """

    cluster_name: str = pydantic.Field()
    """
    Cluster identifier
    """

    insecure_skip_tls_verify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Skip TLS certificate verification
    """

    namespaces: typing.Optional[typing.List[DesiredNamespace]] = pydantic.Field(default=None)
    """
    Desired namespaces for this cluster
    """

    server_url: str = pydantic.Field()
    """
    Kubernetes API server URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
