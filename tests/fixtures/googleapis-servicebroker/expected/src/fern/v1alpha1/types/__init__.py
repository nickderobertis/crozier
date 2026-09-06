



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .servicebroker_get_iam_policy_request_alt import ServicebrokerGetIamPolicyRequestAlt
    from .servicebroker_get_iam_policy_request_xgafv import ServicebrokerGetIamPolicyRequestXgafv
    from .servicebroker_set_iam_policy_request_alt import ServicebrokerSetIamPolicyRequestAlt
    from .servicebroker_set_iam_policy_request_xgafv import ServicebrokerSetIamPolicyRequestXgafv
    from .servicebroker_test_iam_permissions_request_alt import ServicebrokerTestIamPermissionsRequestAlt
    from .servicebroker_test_iam_permissions_request_xgafv import ServicebrokerTestIamPermissionsRequestXgafv
_dynamic_imports: typing.Dict[str, str] = {
    "ServicebrokerGetIamPolicyRequestAlt": ".servicebroker_get_iam_policy_request_alt",
    "ServicebrokerGetIamPolicyRequestXgafv": ".servicebroker_get_iam_policy_request_xgafv",
    "ServicebrokerSetIamPolicyRequestAlt": ".servicebroker_set_iam_policy_request_alt",
    "ServicebrokerSetIamPolicyRequestXgafv": ".servicebroker_set_iam_policy_request_xgafv",
    "ServicebrokerTestIamPermissionsRequestAlt": ".servicebroker_test_iam_permissions_request_alt",
    "ServicebrokerTestIamPermissionsRequestXgafv": ".servicebroker_test_iam_permissions_request_xgafv",
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
    "ServicebrokerGetIamPolicyRequestAlt",
    "ServicebrokerGetIamPolicyRequestXgafv",
    "ServicebrokerSetIamPolicyRequestAlt",
    "ServicebrokerSetIamPolicyRequestXgafv",
    "ServicebrokerTestIamPermissionsRequestAlt",
    "ServicebrokerTestIamPermissionsRequestXgafv",
]
