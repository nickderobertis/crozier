

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_card_input import AgentCardInput
from .create_provider_request_location import CreateProviderRequestLocation


class CreateProviderRequest(UniversalBaseModel):
    location: CreateProviderRequestLocation
    agent_card: typing.Optional[AgentCardInput] = None
    variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    origin: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.
    """

    auto_stop_timeout_sec: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
