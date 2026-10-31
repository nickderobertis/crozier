

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fault_type_dto import FaultTypeDto
from .proxy_dto import ProxyDto


class FaultSimulationDto(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    type: typing.Optional[FaultTypeDto] = pydantic.Field(default=None)
    """
    Describes the expected impact of the fault simulation.
    """

    proxy: typing.Optional[ProxyDto] = pydantic.Field(default=None)
    """
    The details of how to connect to the proxy created for this fault simulation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
