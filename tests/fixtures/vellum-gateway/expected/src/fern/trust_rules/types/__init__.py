



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .trust_rule_create_request_risk import TrustRuleCreateRequestRisk
    from .trust_rule_create_request_scope import TrustRuleCreateRequestScope
    from .trust_rule_create_response import TrustRuleCreateResponse
    from .trust_rule_create_response_rule import TrustRuleCreateResponseRule
    from .trust_rule_create_response_rule_origin import TrustRuleCreateResponseRuleOrigin
    from .trust_rule_create_response_rule_risk import TrustRuleCreateResponseRuleRisk
    from .trust_rule_delete_response import TrustRuleDeleteResponse
    from .trust_rule_reset_response import TrustRuleResetResponse
    from .trust_rule_reset_response_rule import TrustRuleResetResponseRule
    from .trust_rule_reset_response_rule_origin import TrustRuleResetResponseRuleOrigin
    from .trust_rule_reset_response_rule_risk import TrustRuleResetResponseRuleRisk
    from .trust_rule_suggest_request_directory_scope_options_item import (
        TrustRuleSuggestRequestDirectoryScopeOptionsItem,
    )
    from .trust_rule_suggest_request_existing_rule import TrustRuleSuggestRequestExistingRule
    from .trust_rule_suggest_request_intent import TrustRuleSuggestRequestIntent
    from .trust_rule_suggest_request_risk_assessment import TrustRuleSuggestRequestRiskAssessment
    from .trust_rule_suggest_request_scope_options_item import TrustRuleSuggestRequestScopeOptionsItem
    from .trust_rule_suggest_response import TrustRuleSuggestResponse
    from .trust_rule_suggest_response_suggestion import TrustRuleSuggestResponseSuggestion
    from .trust_rule_suggest_response_suggestion_directory_scope_options_item import (
        TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem,
    )
    from .trust_rule_suggest_response_suggestion_scope_options_item import (
        TrustRuleSuggestResponseSuggestionScopeOptionsItem,
    )
    from .trust_rule_update_request_risk import TrustRuleUpdateRequestRisk
    from .trust_rule_update_response import TrustRuleUpdateResponse
    from .trust_rule_update_response_rule import TrustRuleUpdateResponseRule
    from .trust_rule_update_response_rule_origin import TrustRuleUpdateResponseRuleOrigin
    from .trust_rule_update_response_rule_risk import TrustRuleUpdateResponseRuleRisk
    from .trust_rules_list_response import TrustRulesListResponse
    from .trust_rules_list_response_rules_item import TrustRulesListResponseRulesItem
    from .trust_rules_list_response_rules_item_origin import TrustRulesListResponseRulesItemOrigin
    from .trust_rules_list_response_rules_item_risk import TrustRulesListResponseRulesItemRisk
_dynamic_imports: typing.Dict[str, str] = {
    "TrustRuleCreateRequestRisk": ".trust_rule_create_request_risk",
    "TrustRuleCreateRequestScope": ".trust_rule_create_request_scope",
    "TrustRuleCreateResponse": ".trust_rule_create_response",
    "TrustRuleCreateResponseRule": ".trust_rule_create_response_rule",
    "TrustRuleCreateResponseRuleOrigin": ".trust_rule_create_response_rule_origin",
    "TrustRuleCreateResponseRuleRisk": ".trust_rule_create_response_rule_risk",
    "TrustRuleDeleteResponse": ".trust_rule_delete_response",
    "TrustRuleResetResponse": ".trust_rule_reset_response",
    "TrustRuleResetResponseRule": ".trust_rule_reset_response_rule",
    "TrustRuleResetResponseRuleOrigin": ".trust_rule_reset_response_rule_origin",
    "TrustRuleResetResponseRuleRisk": ".trust_rule_reset_response_rule_risk",
    "TrustRuleSuggestRequestDirectoryScopeOptionsItem": ".trust_rule_suggest_request_directory_scope_options_item",
    "TrustRuleSuggestRequestExistingRule": ".trust_rule_suggest_request_existing_rule",
    "TrustRuleSuggestRequestIntent": ".trust_rule_suggest_request_intent",
    "TrustRuleSuggestRequestRiskAssessment": ".trust_rule_suggest_request_risk_assessment",
    "TrustRuleSuggestRequestScopeOptionsItem": ".trust_rule_suggest_request_scope_options_item",
    "TrustRuleSuggestResponse": ".trust_rule_suggest_response",
    "TrustRuleSuggestResponseSuggestion": ".trust_rule_suggest_response_suggestion",
    "TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem": ".trust_rule_suggest_response_suggestion_directory_scope_options_item",
    "TrustRuleSuggestResponseSuggestionScopeOptionsItem": ".trust_rule_suggest_response_suggestion_scope_options_item",
    "TrustRuleUpdateRequestRisk": ".trust_rule_update_request_risk",
    "TrustRuleUpdateResponse": ".trust_rule_update_response",
    "TrustRuleUpdateResponseRule": ".trust_rule_update_response_rule",
    "TrustRuleUpdateResponseRuleOrigin": ".trust_rule_update_response_rule_origin",
    "TrustRuleUpdateResponseRuleRisk": ".trust_rule_update_response_rule_risk",
    "TrustRulesListResponse": ".trust_rules_list_response",
    "TrustRulesListResponseRulesItem": ".trust_rules_list_response_rules_item",
    "TrustRulesListResponseRulesItemOrigin": ".trust_rules_list_response_rules_item_origin",
    "TrustRulesListResponseRulesItemRisk": ".trust_rules_list_response_rules_item_risk",
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
    "TrustRuleCreateRequestRisk",
    "TrustRuleCreateRequestScope",
    "TrustRuleCreateResponse",
    "TrustRuleCreateResponseRule",
    "TrustRuleCreateResponseRuleOrigin",
    "TrustRuleCreateResponseRuleRisk",
    "TrustRuleDeleteResponse",
    "TrustRuleResetResponse",
    "TrustRuleResetResponseRule",
    "TrustRuleResetResponseRuleOrigin",
    "TrustRuleResetResponseRuleRisk",
    "TrustRuleSuggestRequestDirectoryScopeOptionsItem",
    "TrustRuleSuggestRequestExistingRule",
    "TrustRuleSuggestRequestIntent",
    "TrustRuleSuggestRequestRiskAssessment",
    "TrustRuleSuggestRequestScopeOptionsItem",
    "TrustRuleSuggestResponse",
    "TrustRuleSuggestResponseSuggestion",
    "TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem",
    "TrustRuleSuggestResponseSuggestionScopeOptionsItem",
    "TrustRuleUpdateRequestRisk",
    "TrustRuleUpdateResponse",
    "TrustRuleUpdateResponseRule",
    "TrustRuleUpdateResponseRuleOrigin",
    "TrustRuleUpdateResponseRuleRisk",
    "TrustRulesListResponse",
    "TrustRulesListResponseRulesItem",
    "TrustRulesListResponseRulesItemOrigin",
    "TrustRulesListResponseRulesItemRisk",
]
