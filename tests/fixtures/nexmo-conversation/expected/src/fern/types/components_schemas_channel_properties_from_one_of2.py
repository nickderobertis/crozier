

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ComponentsSchemasChannelPropertiesFromOneOf2(UniversalBaseModel):
    """
    Connect to a SIP Endpoint
    """

    type: str = pydantic.Field()
    """
    The type of connection. Must be `sip`
    """

    uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SIP URI to connect to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
