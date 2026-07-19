



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .internal_template_agent_create_model_settings import (
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
    )
    from .internal_template_agent_create_response_format import (
        InternalTemplateAgentCreateResponseFormat,
        InternalTemplateAgentCreateResponseFormat_JsonObject,
        InternalTemplateAgentCreateResponseFormat_JsonSchema,
        InternalTemplateAgentCreateResponseFormat_Text,
    )
    from .internal_template_agent_create_tool_rules_item import (
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
    )
    from .internal_template_group_create_manager_config import (
        InternalTemplateGroupCreateManagerConfig,
        InternalTemplateGroupCreateManagerConfig_Dynamic,
        InternalTemplateGroupCreateManagerConfig_RoundRobin,
        InternalTemplateGroupCreateManagerConfig_Sleeptime,
        InternalTemplateGroupCreateManagerConfig_Supervisor,
        InternalTemplateGroupCreateManagerConfig_VoiceSleeptime,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "InternalTemplateAgentCreateModelSettings": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Anthropic": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Azure": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Bedrock": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_ChatgptOauth": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Deepseek": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_GoogleAi": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_GoogleVertex": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Groq": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Openai": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Together": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Xai": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateModelSettings_Zai": ".internal_template_agent_create_model_settings",
    "InternalTemplateAgentCreateResponseFormat": ".internal_template_agent_create_response_format",
    "InternalTemplateAgentCreateResponseFormat_JsonObject": ".internal_template_agent_create_response_format",
    "InternalTemplateAgentCreateResponseFormat_JsonSchema": ".internal_template_agent_create_response_format",
    "InternalTemplateAgentCreateResponseFormat_Text": ".internal_template_agent_create_response_format",
    "InternalTemplateAgentCreateToolRulesItem": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_Conditional": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_ConstrainChildTools": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_ContinueLoop": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_ExitLoop": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_MaxCountPerStep": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_ParentLastTool": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_RequiredBeforeExit": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_RequiresApproval": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateAgentCreateToolRulesItem_RunFirst": ".internal_template_agent_create_tool_rules_item",
    "InternalTemplateGroupCreateManagerConfig": ".internal_template_group_create_manager_config",
    "InternalTemplateGroupCreateManagerConfig_Dynamic": ".internal_template_group_create_manager_config",
    "InternalTemplateGroupCreateManagerConfig_RoundRobin": ".internal_template_group_create_manager_config",
    "InternalTemplateGroupCreateManagerConfig_Sleeptime": ".internal_template_group_create_manager_config",
    "InternalTemplateGroupCreateManagerConfig_Supervisor": ".internal_template_group_create_manager_config",
    "InternalTemplateGroupCreateManagerConfig_VoiceSleeptime": ".internal_template_group_create_manager_config",
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
