



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cost_center_input import CostCenterInput
    from .error_response import ErrorResponse
    from .payable import Payable
    from .settlement import Settlement
    from .settlements_response import SettlementsResponse
    from .snapshot_response import SnapshotResponse
    from .supplier_input import SupplierInput
    from .token_response import TokenResponse
    from .webhook_input import WebhookInput
_dynamic_imports: typing.Dict[str, str] = {
    "CostCenterInput": ".cost_center_input",
    "ErrorResponse": ".error_response",
    "Payable": ".payable",
    "Settlement": ".settlement",
    "SettlementsResponse": ".settlements_response",
    "SnapshotResponse": ".snapshot_response",
    "SupplierInput": ".supplier_input",
    "TokenResponse": ".token_response",
    "WebhookInput": ".webhook_input",
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
    "CostCenterInput",
    "ErrorResponse",
    "Payable",
    "Settlement",
    "SettlementsResponse",
    "SnapshotResponse",
    "SupplierInput",
    "TokenResponse",
    "WebhookInput",
]
