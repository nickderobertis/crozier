



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_wizard_policy_id_config_response import PostWizardPolicyIdConfigResponse
    from .post_wizard_policy_response import PostWizardPolicyResponse
    from .wizard_api_set_policy_async_request_wizard_config import WizardApiSetPolicyAsyncRequestWizardConfig
    from .wizard_api_set_policy_async_request_wizard_config_policy import (
        WizardApiSetPolicyAsyncRequestWizardConfigPolicy,
    )
    from .wizard_api_set_policy_async_request_wizard_config_schemas_item import (
        WizardApiSetPolicyAsyncRequestWizardConfigSchemasItem,
    )
    from .wizard_api_set_policy_async_request_wizard_config_schemas_item_mint_options import (
        WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemMintOptions,
    )
    from .wizard_api_set_policy_async_request_wizard_config_schemas_item_roles_config_item import (
        WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItem,
    )
    from .wizard_api_set_policy_async_request_wizard_config_schemas_item_roles_config_item_grid_columns_item import (
        WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItemGridColumnsItem,
    )
    from .wizard_api_set_policy_async_request_wizard_config_trust_chain_item import (
        WizardApiSetPolicyAsyncRequestWizardConfigTrustChainItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostWizardPolicyIdConfigResponse": ".post_wizard_policy_id_config_response",
    "PostWizardPolicyResponse": ".post_wizard_policy_response",
    "WizardApiSetPolicyAsyncRequestWizardConfig": ".wizard_api_set_policy_async_request_wizard_config",
    "WizardApiSetPolicyAsyncRequestWizardConfigPolicy": ".wizard_api_set_policy_async_request_wizard_config_policy",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItem": ".wizard_api_set_policy_async_request_wizard_config_schemas_item",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemMintOptions": ".wizard_api_set_policy_async_request_wizard_config_schemas_item_mint_options",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItem": ".wizard_api_set_policy_async_request_wizard_config_schemas_item_roles_config_item",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItemGridColumnsItem": ".wizard_api_set_policy_async_request_wizard_config_schemas_item_roles_config_item_grid_columns_item",
    "WizardApiSetPolicyAsyncRequestWizardConfigTrustChainItem": ".wizard_api_set_policy_async_request_wizard_config_trust_chain_item",
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
    "PostWizardPolicyIdConfigResponse",
    "PostWizardPolicyResponse",
    "WizardApiSetPolicyAsyncRequestWizardConfig",
    "WizardApiSetPolicyAsyncRequestWizardConfigPolicy",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItem",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemMintOptions",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItem",
    "WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItemGridColumnsItem",
    "WizardApiSetPolicyAsyncRequestWizardConfigTrustChainItem",
]
