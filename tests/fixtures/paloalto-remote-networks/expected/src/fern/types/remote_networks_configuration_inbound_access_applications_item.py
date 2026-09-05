

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_configuration_inbound_access_applications_item_protocol import (
    RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol,
)


class RemoteNetworksConfigurationInboundAccessApplicationsItem(UniversalBaseModel):
    dedicated_ip: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Dedicated IP address for this application
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    Destination port
    """

    private_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Private IP address
    """

    protocol: typing.Optional[RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol] = pydantic.Field(
        default=None
    )
    """
    Protocol used by this application
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
