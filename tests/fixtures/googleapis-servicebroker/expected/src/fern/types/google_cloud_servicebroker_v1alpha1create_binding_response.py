

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleCloudServicebrokerV1Alpha1CreateBindingResponse(UniversalBaseModel):
    """
    Response for the `CreateBinding()` method.
    """

    credentials: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Credentials to use the binding.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used to communicate description of the response. Usually for non-standard
    error codes.
    https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors
    """

    operation: typing.Optional[str] = pydantic.Field(default=None)
    """
    If broker executes operation asynchronously, this is the operation ID that
    can be polled to check the completion status of said operation.
    This broker always executes all create/delete operations asynchronously.
    """

    route_service_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URL to which the platform may proxy requests for the address sent with
    bind_resource.route
    """

    syslog_drain_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    From where to read system logs.
    """

    volume_mounts: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    An array of configuration for mounting volumes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
