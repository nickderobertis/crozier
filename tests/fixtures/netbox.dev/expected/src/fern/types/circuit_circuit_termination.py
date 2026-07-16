

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_provider_network import NestedProviderNetwork
from .nested_site import NestedSite


class CircuitCircuitTermination(UniversalBaseModel):
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    port_speed: typing.Optional[int] = None
    provider_network: typing.Optional[NestedProviderNetwork] = None
    site: typing.Optional[NestedSite] = None
    upstream_speed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Upstream speed, if different from port speed
    """

    url: typing.Optional[str] = None
    xconnect_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
