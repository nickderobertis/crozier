

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BaseSliceDesDeterministicCommunication(UniversalBaseModel):
    """
    This attribute defines if the network slice supports deterministic communication for periodic user traffic. Periodic traffic refers to the type of traffic with periodic transmissions.
    """

    availability: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This parameter describes if the network slice supports deterministic communication.
    """

    periodicity: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    This parameter provides a list of periodicities supported by the network slice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
