



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_agent_webhook_request_webhook_type import CreateAgentWebhookRequestWebhookType
    from .create_agent_webhook_response import CreateAgentWebhookResponse
    from .delete_agent_webhook_response import DeleteAgentWebhookResponse
    from .get_agent_webhook_response import GetAgentWebhookResponse
    from .list_agent_webhooks_response import ListAgentWebhooksResponse
    from .update_agent_webhook_response import UpdateAgentWebhookResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAgentWebhookRequestWebhookType": ".create_agent_webhook_request_webhook_type",
    "CreateAgentWebhookResponse": ".create_agent_webhook_response",
    "DeleteAgentWebhookResponse": ".delete_agent_webhook_response",
    "GetAgentWebhookResponse": ".get_agent_webhook_response",
    "ListAgentWebhooksResponse": ".list_agent_webhooks_response",
    "UpdateAgentWebhookResponse": ".update_agent_webhook_response",
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
    "CreateAgentWebhookRequestWebhookType",
    "CreateAgentWebhookResponse",
    "DeleteAgentWebhookResponse",
    "GetAgentWebhookResponse",
    "ListAgentWebhooksResponse",
    "UpdateAgentWebhookResponse",
]
