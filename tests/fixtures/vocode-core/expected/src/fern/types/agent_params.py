

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_params_actions_item import AgentParamsActionsItem
from .agent_params_deepgram_keywords_value import AgentParamsDeepgramKeywordsValue
from .agent_params_endpointing_sensitivity import AgentParamsEndpointingSensitivity
from .agent_params_ivr_navigation_mode import AgentParamsIvrNavigationMode
from .agent_params_openai_account_connection import AgentParamsOpenaiAccountConnection
from .agent_params_prompt import AgentParamsPrompt
from .agent_params_vector_database import AgentParamsVectorDatabase
from .agent_params_voice import AgentParamsVoice
from .agent_params_webhook import AgentParamsWebhook
from .internal_llm_fallback import InternalLlmFallback
from .interrupt_sensitivity import InterruptSensitivity
from .language import Language


class AgentParams(UniversalBaseModel):
    name: typing.Optional[str] = None
    prompt: AgentParamsPrompt
    language: typing.Optional[Language] = None
    actions: typing.Optional[typing.List[AgentParamsActionsItem]] = None
    voice: AgentParamsVoice
    initial_message: typing.Optional[str] = None
    webhook: typing.Optional[AgentParamsWebhook] = None
    vector_database: typing.Optional[AgentParamsVectorDatabase] = None
    interrupt_sensitivity: typing.Optional[InterruptSensitivity] = None
    context_endpoint: typing.Optional[str] = None
    noise_suppression: typing.Optional[bool] = None
    endpointing_sensitivity: typing.Optional[AgentParamsEndpointingSensitivity] = None
    ivr_navigation_mode: typing.Optional[AgentParamsIvrNavigationMode] = None
    conversation_speed: typing.Optional[float] = None
    initial_message_delay: typing.Optional[float] = None
    openai_model_name_override: typing.Optional[str] = None
    ask_if_human_present_on_idle: typing.Optional[bool] = None
    openai_account_connection: typing.Optional[AgentParamsOpenaiAccountConnection] = None
    run_do_not_call_detection: typing.Optional[bool] = None
    llm_fallback: typing.Optional[InternalLlmFallback] = None
    deepgram_keywords: typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]] = None
    idle_time_seconds: typing.Optional[int] = None
    llm_temperature: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
