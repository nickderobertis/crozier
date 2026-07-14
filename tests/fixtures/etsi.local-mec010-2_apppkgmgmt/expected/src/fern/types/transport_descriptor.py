

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .security_info import SecurityInfo
from .transport_types import TransportTypes


class TransportDescriptor(UniversalBaseModel):
    protocol: str = pydantic.Field()
    """
    The name of the protocol used. Shall be set to HTTP for a REST API.
    """

    security: SecurityInfo
    type: TransportTypes
    version: str = pydantic.Field()
    """
    The version of the protocol used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
