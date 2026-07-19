



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .client_side_access_tokens_create_client_side_access_token_request_policy_item import (
        ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem,
    )
    from .client_side_access_tokens_create_client_side_access_token_request_policy_item_access_item import (
        ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem,
    )
    from .client_side_access_tokens_create_client_side_access_token_request_policy_item_type import (
        ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType,
    )
    from .client_side_access_tokens_create_client_side_access_token_response import (
        ClientSideAccessTokensCreateClientSideAccessTokenResponse,
    )
    from .client_side_access_tokens_create_client_side_access_token_response_policy import (
        ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicy,
    )
    from .client_side_access_tokens_create_client_side_access_token_response_policy_data_item import (
        ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItem,
    )
    from .client_side_access_tokens_create_client_side_access_token_response_policy_data_item_access_item import (
        ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem,
    )
    from .client_side_access_tokens_create_client_side_access_token_response_policy_data_item_type import (
        ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType,
    )
    from .client_side_access_tokens_create_client_side_access_token_response_policy_version import (
        ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyVersion,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response import (
        ClientSideAccessTokensListClientSideAccessTokensResponse,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item import (
        ClientSideAccessTokensListClientSideAccessTokensResponseTokensItem,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy import (
        ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicy,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item import (
        ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItem,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_access_item import (
        ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemAccessItem,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_type import (
        ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType,
    )
    from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_version import (
        ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyVersion,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem": ".client_side_access_tokens_create_client_side_access_token_request_policy_item",
    "ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem": ".client_side_access_tokens_create_client_side_access_token_request_policy_item_access_item",
    "ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType": ".client_side_access_tokens_create_client_side_access_token_request_policy_item_type",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponse": ".client_side_access_tokens_create_client_side_access_token_response",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicy": ".client_side_access_tokens_create_client_side_access_token_response_policy",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItem": ".client_side_access_tokens_create_client_side_access_token_response_policy_data_item",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem": ".client_side_access_tokens_create_client_side_access_token_response_policy_data_item_access_item",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType": ".client_side_access_tokens_create_client_side_access_token_response_policy_data_item_type",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyVersion": ".client_side_access_tokens_create_client_side_access_token_response_policy_version",
    "ClientSideAccessTokensListClientSideAccessTokensResponse": ".client_side_access_tokens_list_client_side_access_tokens_response",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItem": ".client_side_access_tokens_list_client_side_access_tokens_response_tokens_item",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicy": ".client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItem": ".client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemAccessItem": ".client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_access_item",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType": ".client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_type",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyVersion": ".client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_version",
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
    "ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem",
    "ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem",
    "ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponse",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicy",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItem",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType",
    "ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyVersion",
    "ClientSideAccessTokensListClientSideAccessTokensResponse",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItem",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicy",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItem",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemAccessItem",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType",
    "ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyVersion",
]
