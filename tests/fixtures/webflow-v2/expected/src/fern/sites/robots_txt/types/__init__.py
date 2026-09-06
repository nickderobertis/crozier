



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_robots_txt_request_rules_item import DeleteRobotsTxtRequestRulesItem
    from .delete_robots_txt_response import DeleteRobotsTxtResponse
    from .delete_robots_txt_response_rules_item import DeleteRobotsTxtResponseRulesItem
    from .get_robots_txt_response import GetRobotsTxtResponse
    from .get_robots_txt_response_rules_item import GetRobotsTxtResponseRulesItem
    from .patch_robots_txt_request_rules_item import PatchRobotsTxtRequestRulesItem
    from .patch_robots_txt_response import PatchRobotsTxtResponse
    from .patch_robots_txt_response_rules_item import PatchRobotsTxtResponseRulesItem
    from .put_robots_txt_request_rules_item import PutRobotsTxtRequestRulesItem
    from .put_robots_txt_response import PutRobotsTxtResponse
    from .put_robots_txt_response_rules_item import PutRobotsTxtResponseRulesItem
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteRobotsTxtRequestRulesItem": ".delete_robots_txt_request_rules_item",
    "DeleteRobotsTxtResponse": ".delete_robots_txt_response",
    "DeleteRobotsTxtResponseRulesItem": ".delete_robots_txt_response_rules_item",
    "GetRobotsTxtResponse": ".get_robots_txt_response",
    "GetRobotsTxtResponseRulesItem": ".get_robots_txt_response_rules_item",
    "PatchRobotsTxtRequestRulesItem": ".patch_robots_txt_request_rules_item",
    "PatchRobotsTxtResponse": ".patch_robots_txt_response",
    "PatchRobotsTxtResponseRulesItem": ".patch_robots_txt_response_rules_item",
    "PutRobotsTxtRequestRulesItem": ".put_robots_txt_request_rules_item",
    "PutRobotsTxtResponse": ".put_robots_txt_response",
    "PutRobotsTxtResponseRulesItem": ".put_robots_txt_response_rules_item",
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
    "DeleteRobotsTxtRequestRulesItem",
    "DeleteRobotsTxtResponse",
    "DeleteRobotsTxtResponseRulesItem",
    "GetRobotsTxtResponse",
    "GetRobotsTxtResponseRulesItem",
    "PatchRobotsTxtRequestRulesItem",
    "PatchRobotsTxtResponse",
    "PatchRobotsTxtResponseRulesItem",
    "PutRobotsTxtRequestRulesItem",
    "PutRobotsTxtResponse",
    "PutRobotsTxtResponseRulesItem",
]
