

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ask_user_questions_config import AskUserQuestionsConfig
from .context_management_config import ContextManagementConfig
from .dynamic_sub_agents_config import DynamicSubAgentsConfig
from .generative_ui_config import GenerativeUiConfig
from .sandbox_config import SandboxConfig


class RuntimeConfig(UniversalBaseModel):
    ask_user_questions: typing.Optional[AskUserQuestionsConfig] = None
    context_management: typing.Optional[ContextManagementConfig] = None
    dynamic_sub_agents: typing.Optional[DynamicSubAgentsConfig] = None
    generative_ui: typing.Optional[GenerativeUiConfig] = None
    iteration_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max agent-loop iterations per turn (1–1024). Default: 100.
    """

    sandbox: typing.Optional[SandboxConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
