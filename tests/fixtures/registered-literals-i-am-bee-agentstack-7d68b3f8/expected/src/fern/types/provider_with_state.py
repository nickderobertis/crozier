

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_card_output import AgentCardOutput
from .env_var import EnvVar
from .provider_error_message import ProviderErrorMessage
from .provider_type import ProviderType
from .provider_with_state_registry import ProviderWithStateRegistry
from .provider_with_state_source import ProviderWithStateSource
from .provider_with_state_state import ProviderWithStateState
from .version_info import VersionInfo


class ProviderWithState(UniversalBaseModel):
    source: ProviderWithStateSource
    id: typing.Optional[str] = None
    auto_stop_timeout: typing.Optional[str] = None
    origin: str
    version_info: typing.Optional[VersionInfo] = None
    registry: typing.Optional[ProviderWithStateRegistry] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    created_by: str
    last_active_at: typing.Optional[dt.datetime] = None
    agent_card: AgentCardOutput
    state: ProviderWithStateState
    last_error: typing.Optional[ProviderErrorMessage] = None
    missing_configuration: typing.Optional[typing.List[EnvVar]] = None
    type: typing.Optional[ProviderType] = None
    managed: typing.Optional[bool] = None
    env: typing.Optional[typing.List[EnvVar]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
