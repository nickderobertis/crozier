



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        TrustRuleCreateRequestRisk,
        TrustRuleCreateRequestScope,
        TrustRuleCreateResponse,
        TrustRuleCreateResponseRule,
        TrustRuleCreateResponseRuleOrigin,
        TrustRuleCreateResponseRuleRisk,
        TrustRuleDeleteResponse,
        TrustRuleResetResponse,
        TrustRuleResetResponseRule,
        TrustRuleResetResponseRuleOrigin,
        TrustRuleResetResponseRuleRisk,
        TrustRuleSuggestRequestDirectoryScopeOptionsItem,
        TrustRuleSuggestRequestExistingRule,
        TrustRuleSuggestRequestIntent,
        TrustRuleSuggestRequestRiskAssessment,
        TrustRuleSuggestRequestScopeOptionsItem,
        TrustRuleSuggestResponse,
        TrustRuleSuggestResponseSuggestion,
        TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem,
        TrustRuleSuggestResponseSuggestionScopeOptionsItem,
        TrustRuleUpdateRequestRisk,
        TrustRuleUpdateResponse,
        TrustRuleUpdateResponseRule,
        TrustRuleUpdateResponseRuleOrigin,
        TrustRuleUpdateResponseRuleRisk,
        TrustRulesListResponse,
        TrustRulesListResponseRulesItem,
        TrustRulesListResponseRulesItemOrigin,
        TrustRulesListResponseRulesItemRisk,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "TrustRuleCreateRequestRisk": ".types",
    "TrustRuleCreateRequestScope": ".types",
    "TrustRuleCreateResponse": ".types",
    "TrustRuleCreateResponseRule": ".types",
    "TrustRuleCreateResponseRuleOrigin": ".types",
    "TrustRuleCreateResponseRuleRisk": ".types",
    "TrustRuleDeleteResponse": ".types",
    "TrustRuleResetResponse": ".types",
    "TrustRuleResetResponseRule": ".types",
    "TrustRuleResetResponseRuleOrigin": ".types",
    "TrustRuleResetResponseRuleRisk": ".types",
    "TrustRuleSuggestRequestDirectoryScopeOptionsItem": ".types",
    "TrustRuleSuggestRequestExistingRule": ".types",
    "TrustRuleSuggestRequestIntent": ".types",
    "TrustRuleSuggestRequestRiskAssessment": ".types",
    "TrustRuleSuggestRequestScopeOptionsItem": ".types",
    "TrustRuleSuggestResponse": ".types",
    "TrustRuleSuggestResponseSuggestion": ".types",
    "TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem": ".types",
    "TrustRuleSuggestResponseSuggestionScopeOptionsItem": ".types",
    "TrustRuleUpdateRequestRisk": ".types",
    "TrustRuleUpdateResponse": ".types",
    "TrustRuleUpdateResponseRule": ".types",
    "TrustRuleUpdateResponseRuleOrigin": ".types",
    "TrustRuleUpdateResponseRuleRisk": ".types",
    "TrustRulesListResponse": ".types",
    "TrustRulesListResponseRulesItem": ".types",
    "TrustRulesListResponseRulesItemOrigin": ".types",
    "TrustRulesListResponseRulesItemRisk": ".types",
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
