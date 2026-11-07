

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_card_output import AgentCardOutput
from .discovery_state import DiscoveryState


class ProviderDiscovery(UniversalBaseModel):
    id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    status: DiscoveryState
    docker_image: str
    created_by: str
    agent_card: typing.Optional[AgentCardOutput] = None
    error_message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
