



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        InternalTemplateAgentCreateModelSettings,
        InternalTemplateAgentCreateModelSettings_Anthropic,
        InternalTemplateAgentCreateModelSettings_Azure,
        InternalTemplateAgentCreateModelSettings_Bedrock,
        InternalTemplateAgentCreateModelSettings_ChatgptOauth,
        InternalTemplateAgentCreateModelSettings_Deepseek,
        InternalTemplateAgentCreateModelSettings_GoogleAi,
        InternalTemplateAgentCreateModelSettings_GoogleVertex,
        InternalTemplateAgentCreateModelSettings_Groq,
        InternalTemplateAgentCreateModelSettings_Openai,
        InternalTemplateAgentCreateModelSettings_Together,
        InternalTemplateAgentCreateModelSettings_Xai,
        InternalTemplateAgentCreateModelSettings_Zai,
        InternalTemplateAgentCreateResponseFormat,
        InternalTemplateAgentCreateResponseFormat_JsonObject,
        InternalTemplateAgentCreateResponseFormat_JsonSchema,
        InternalTemplateAgentCreateResponseFormat_Text,
        InternalTemplateAgentCreateToolRulesItem,
        InternalTemplateAgentCreateToolRulesItem_Conditional,
        InternalTemplateAgentCreateToolRulesItem_ConstrainChildTools,
        InternalTemplateAgentCreateToolRulesItem_ContinueLoop,
        InternalTemplateAgentCreateToolRulesItem_ExitLoop,
        InternalTemplateAgentCreateToolRulesItem_MaxCountPerStep,
        InternalTemplateAgentCreateToolRulesItem_ParentLastTool,
        InternalTemplateAgentCreateToolRulesItem_RequiredBeforeExit,
        InternalTemplateAgentCreateToolRulesItem_RequiresApproval,
        InternalTemplateAgentCreateToolRulesItem_RunFirst,
        InternalTemplateGroupCreateManagerConfig,
        InternalTemplateGroupCreateManagerConfig_Dynamic,
        InternalTemplateGroupCreateManagerConfig_RoundRobin,
        InternalTemplateGroupCreateManagerConfig_Sleeptime,
        InternalTemplateGroupCreateManagerConfig_Supervisor,
        InternalTemplateGroupCreateManagerConfig_VoiceSleeptime,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "InternalTemplateAgentCreateModelSettings": ".types",
    "InternalTemplateAgentCreateModelSettings_Anthropic": ".types",
    "InternalTemplateAgentCreateModelSettings_Azure": ".types",
    "InternalTemplateAgentCreateModelSettings_Bedrock": ".types",
    "InternalTemplateAgentCreateModelSettings_ChatgptOauth": ".types",
    "InternalTemplateAgentCreateModelSettings_Deepseek": ".types",
    "InternalTemplateAgentCreateModelSettings_GoogleAi": ".types",
    "InternalTemplateAgentCreateModelSettings_GoogleVertex": ".types",
    "InternalTemplateAgentCreateModelSettings_Groq": ".types",
    "InternalTemplateAgentCreateModelSettings_Openai": ".types",
    "InternalTemplateAgentCreateModelSettings_Together": ".types",
    "InternalTemplateAgentCreateModelSettings_Xai": ".types",
    "InternalTemplateAgentCreateModelSettings_Zai": ".types",
    "InternalTemplateAgentCreateResponseFormat": ".types",
    "InternalTemplateAgentCreateResponseFormat_JsonObject": ".types",
    "InternalTemplateAgentCreateResponseFormat_JsonSchema": ".types",
    "InternalTemplateAgentCreateResponseFormat_Text": ".types",
    "InternalTemplateAgentCreateToolRulesItem": ".types",
    "InternalTemplateAgentCreateToolRulesItem_Conditional": ".types",
    "InternalTemplateAgentCreateToolRulesItem_ConstrainChildTools": ".types",
    "InternalTemplateAgentCreateToolRulesItem_ContinueLoop": ".types",
    "InternalTemplateAgentCreateToolRulesItem_ExitLoop": ".types",
    "InternalTemplateAgentCreateToolRulesItem_MaxCountPerStep": ".types",
    "InternalTemplateAgentCreateToolRulesItem_ParentLastTool": ".types",
    "InternalTemplateAgentCreateToolRulesItem_RequiredBeforeExit": ".types",
    "InternalTemplateAgentCreateToolRulesItem_RequiresApproval": ".types",
    "InternalTemplateAgentCreateToolRulesItem_RunFirst": ".types",
    "InternalTemplateGroupCreateManagerConfig": ".types",
    "InternalTemplateGroupCreateManagerConfig_Dynamic": ".types",
    "InternalTemplateGroupCreateManagerConfig_RoundRobin": ".types",
    "InternalTemplateGroupCreateManagerConfig_Sleeptime": ".types",
    "InternalTemplateGroupCreateManagerConfig_Supervisor": ".types",
    "InternalTemplateGroupCreateManagerConfig_VoiceSleeptime": ".types",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "InternalTemplateAgentCreateModelSettings",
    "InternalTemplateAgentCreateModelSettings_Anthropic",
    "InternalTemplateAgentCreateModelSettings_Azure",
    "InternalTemplateAgentCreateModelSettings_Bedrock",
    "InternalTemplateAgentCreateModelSettings_ChatgptOauth",
    "InternalTemplateAgentCreateModelSettings_Deepseek",
    "InternalTemplateAgentCreateModelSettings_GoogleAi",
    "InternalTemplateAgentCreateModelSettings_GoogleVertex",
    "InternalTemplateAgentCreateModelSettings_Groq",
    "InternalTemplateAgentCreateModelSettings_Openai",
    "InternalTemplateAgentCreateModelSettings_Together",
    "InternalTemplateAgentCreateModelSettings_Xai",
    "InternalTemplateAgentCreateModelSettings_Zai",
    "InternalTemplateAgentCreateResponseFormat",
    "InternalTemplateAgentCreateResponseFormat_JsonObject",
    "InternalTemplateAgentCreateResponseFormat_JsonSchema",
    "InternalTemplateAgentCreateResponseFormat_Text",
    "InternalTemplateAgentCreateToolRulesItem",
    "InternalTemplateAgentCreateToolRulesItem_Conditional",
    "InternalTemplateAgentCreateToolRulesItem_ConstrainChildTools",
    "InternalTemplateAgentCreateToolRulesItem_ContinueLoop",
    "InternalTemplateAgentCreateToolRulesItem_ExitLoop",
    "InternalTemplateAgentCreateToolRulesItem_MaxCountPerStep",
    "InternalTemplateAgentCreateToolRulesItem_ParentLastTool",
    "InternalTemplateAgentCreateToolRulesItem_RequiredBeforeExit",
    "InternalTemplateAgentCreateToolRulesItem_RequiresApproval",
    "InternalTemplateAgentCreateToolRulesItem_RunFirst",
    "InternalTemplateGroupCreateManagerConfig",
    "InternalTemplateGroupCreateManagerConfig_Dynamic",
    "InternalTemplateGroupCreateManagerConfig_RoundRobin",
    "InternalTemplateGroupCreateManagerConfig_Sleeptime",
    "InternalTemplateGroupCreateManagerConfig_Supervisor",
    "InternalTemplateGroupCreateManagerConfig_VoiceSleeptime",
]
