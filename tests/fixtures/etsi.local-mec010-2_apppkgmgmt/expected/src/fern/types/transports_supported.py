

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .serializers import Serializers
from .transport_descriptor import TransportDescriptor


class TransportsSupported(UniversalBaseModel):
    """
    'Indicates transports and serialization formats supported made available to the service-consuming application. Defaults to REST + JSON if absent.'
    """

    serializers: typing.Optional[Serializers] = None
    transport: typing.Optional[TransportDescriptor] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
