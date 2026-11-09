

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BridgeName(UniversalBaseModel):
    """
    Info about the network that the bridge is bridging to.
    """

    displayname: str = pydantic.Field()
    """
    The displayname of the network.
    """

    network_url: str = pydantic.Field()
    """
    The URL to the website of the network.
    """

    network_icon: str = pydantic.Field()
    """
    The icon of the network as a `mxc://` URI.
    """

    network_id: str = pydantic.Field()
    """
    An identifier uniquely identifying the network.
    """

    beeper_bridge_type: str = pydantic.Field()
    """
    An identifier uniquely identifying the bridge software.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
