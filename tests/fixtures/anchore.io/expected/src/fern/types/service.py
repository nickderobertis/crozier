

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .status_response import StatusResponse


class Service(UniversalBaseModel):
    """
    A service status record
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url to reach the service, including port as needed
    """

    hostid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of the host on which the service is executing
    """

    service_detail: typing.Optional[StatusResponse] = None
    servicename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Registered service name
    """

    status: typing.Optional[bool] = None
    status_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A state indicating the condition of the service. Normal operation is 'registered'
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the service as reported by the service implementation on registration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
