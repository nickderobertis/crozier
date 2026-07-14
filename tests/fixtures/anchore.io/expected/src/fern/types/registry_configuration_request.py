

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistryConfigurationRequest(UniversalBaseModel):
    """
    A registry record describing the endpoint and credentials for a registry
    """

    registry: typing.Optional[str] = pydantic.Field(default=None)
    """
    hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)
    """

    registry_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    human readable name associated with registry record
    """

    registry_pass: typing.Optional[str] = pydantic.Field(default=None)
    """
    Password portion of credential to use for this registry
    """

    registry_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of registry
    """

    registry_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    Username portion of credential to use for this registry
    """

    registry_verify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Use TLS/SSL verification for the registry URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
