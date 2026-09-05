

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_configuration_inbound_access_applications_item import (
    RemoteNetworksConfigurationInboundAccessApplicationsItem,
)


class RemoteNetworksConfigurationInboundAccess(UniversalBaseModel):
    applications: typing.Optional[typing.List[RemoteNetworksConfigurationInboundAccessApplicationsItem]] = None
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable Inbound Access
    """

    public_ip: typing.Optional[str] = None
    snat_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable source NAT
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
