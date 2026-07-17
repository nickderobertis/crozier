

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegistryConfiguration(UniversalBaseModel):
    """
    A registry entry describing the endpoint and credentials for a registry to pull images from
    """

    created_at: typing.Optional[dt.datetime] = None
    last_upated: typing.Optional[dt.datetime] = None
    registry: typing.Optional[str] = pydantic.Field(default=None)
    """
    hostname:port string for accessing the registry, as would be used in a docker pull operation
    """

    registry_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    human readable name associated with registry record
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

    user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="Engine user that owns this registry entry"),
    ] = None
    """
    Engine user that owns this registry entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
