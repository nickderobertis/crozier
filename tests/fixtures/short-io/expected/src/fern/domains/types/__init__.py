



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_domains_response_item import GetApiDomainsResponseItem
    from .get_api_domains_response_item_https_level import GetApiDomainsResponseItemHttpsLevel
    from .get_api_domains_response_item_link_type import GetApiDomainsResponseItemLinkType
    from .get_api_domains_response_item_robots import GetApiDomainsResponseItemRobots
    from .get_api_domains_response_item_state import GetApiDomainsResponseItemState
    from .get_domains_domain_id_response import GetDomainsDomainIdResponse
    from .get_domains_domain_id_response_https_level import GetDomainsDomainIdResponseHttpsLevel
    from .get_domains_domain_id_response_link_type import GetDomainsDomainIdResponseLinkType
    from .get_domains_domain_id_response_robots import GetDomainsDomainIdResponseRobots
    from .get_domains_domain_id_response_state import GetDomainsDomainIdResponseState
    from .get_domains_domain_id_response_user_plan import GetDomainsDomainIdResponseUserPlan
    from .post_domains_request_link_type import PostDomainsRequestLinkType
    from .post_domains_response import PostDomainsResponse
    from .post_domains_response_https_level import PostDomainsResponseHttpsLevel
    from .post_domains_response_link_type import PostDomainsResponseLinkType
    from .post_domains_response_robots import PostDomainsResponseRobots
    from .post_domains_response_state import PostDomainsResponseState
    from .post_domains_settings_domain_id_request_https_level import PostDomainsSettingsDomainIdRequestHttpsLevel
    from .post_domains_settings_domain_id_request_link_type import PostDomainsSettingsDomainIdRequestLinkType
    from .post_domains_settings_domain_id_request_robots import PostDomainsSettingsDomainIdRequestRobots
    from .post_domains_settings_domain_id_request_webhook_url import PostDomainsSettingsDomainIdRequestWebhookUrl
    from .post_domains_settings_domain_id_request_webhook_url_one import PostDomainsSettingsDomainIdRequestWebhookUrlOne
    from .post_domains_settings_domain_id_response import PostDomainsSettingsDomainIdResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiDomainsResponseItem": ".get_api_domains_response_item",
    "GetApiDomainsResponseItemHttpsLevel": ".get_api_domains_response_item_https_level",
    "GetApiDomainsResponseItemLinkType": ".get_api_domains_response_item_link_type",
    "GetApiDomainsResponseItemRobots": ".get_api_domains_response_item_robots",
    "GetApiDomainsResponseItemState": ".get_api_domains_response_item_state",
    "GetDomainsDomainIdResponse": ".get_domains_domain_id_response",
    "GetDomainsDomainIdResponseHttpsLevel": ".get_domains_domain_id_response_https_level",
    "GetDomainsDomainIdResponseLinkType": ".get_domains_domain_id_response_link_type",
    "GetDomainsDomainIdResponseRobots": ".get_domains_domain_id_response_robots",
    "GetDomainsDomainIdResponseState": ".get_domains_domain_id_response_state",
    "GetDomainsDomainIdResponseUserPlan": ".get_domains_domain_id_response_user_plan",
    "PostDomainsRequestLinkType": ".post_domains_request_link_type",
    "PostDomainsResponse": ".post_domains_response",
    "PostDomainsResponseHttpsLevel": ".post_domains_response_https_level",
    "PostDomainsResponseLinkType": ".post_domains_response_link_type",
    "PostDomainsResponseRobots": ".post_domains_response_robots",
    "PostDomainsResponseState": ".post_domains_response_state",
    "PostDomainsSettingsDomainIdRequestHttpsLevel": ".post_domains_settings_domain_id_request_https_level",
    "PostDomainsSettingsDomainIdRequestLinkType": ".post_domains_settings_domain_id_request_link_type",
    "PostDomainsSettingsDomainIdRequestRobots": ".post_domains_settings_domain_id_request_robots",
    "PostDomainsSettingsDomainIdRequestWebhookUrl": ".post_domains_settings_domain_id_request_webhook_url",
    "PostDomainsSettingsDomainIdRequestWebhookUrlOne": ".post_domains_settings_domain_id_request_webhook_url_one",
    "PostDomainsSettingsDomainIdResponse": ".post_domains_settings_domain_id_response",
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
    "GetApiDomainsResponseItem",
    "GetApiDomainsResponseItemHttpsLevel",
    "GetApiDomainsResponseItemLinkType",
    "GetApiDomainsResponseItemRobots",
    "GetApiDomainsResponseItemState",
    "GetDomainsDomainIdResponse",
    "GetDomainsDomainIdResponseHttpsLevel",
    "GetDomainsDomainIdResponseLinkType",
    "GetDomainsDomainIdResponseRobots",
    "GetDomainsDomainIdResponseState",
    "GetDomainsDomainIdResponseUserPlan",
    "PostDomainsRequestLinkType",
    "PostDomainsResponse",
    "PostDomainsResponseHttpsLevel",
    "PostDomainsResponseLinkType",
    "PostDomainsResponseRobots",
    "PostDomainsResponseState",
    "PostDomainsSettingsDomainIdRequestHttpsLevel",
    "PostDomainsSettingsDomainIdRequestLinkType",
    "PostDomainsSettingsDomainIdRequestRobots",
    "PostDomainsSettingsDomainIdRequestWebhookUrl",
    "PostDomainsSettingsDomainIdRequestWebhookUrlOne",
    "PostDomainsSettingsDomainIdResponse",
]
