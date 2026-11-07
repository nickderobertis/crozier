

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_card_output import AgentCardOutput
from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2registry import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Registry,
)
from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2source import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Source,
)
from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2state import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2State,
)
from .env_var import EnvVar
from .provider_error_message import ProviderErrorMessage
from .provider_type import ProviderType
from .version_info import VersionInfo


class AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2(UniversalBaseModel):
    source: AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Source
    id: str
    auto_stop_timeout: typing.Optional[str] = None
    origin: str
    version_info: typing.Optional[VersionInfo] = None
    registry: typing.Optional[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Registry] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    created_by: str
    last_active_at: typing.Optional[dt.datetime] = None
    agent_card: AgentCardOutput
    state: AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2State
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
