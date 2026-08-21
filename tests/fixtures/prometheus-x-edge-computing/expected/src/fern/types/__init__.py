



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_token import AccessToken
    from .consent_id import ConsentId
    from .contract_id import ContractId
    from .data_id import DataId
    from .data_provider_id import DataProviderId
    from .execution_result import ExecutionResult
    from .execution_result_metrics import ExecutionResultMetrics
    from .function import Function
    from .function_id import FunctionId
    from .function_provider_id import FunctionProviderId
    from .privacy_zone_data import PrivacyZoneData
    from .privacy_zone_id import PrivacyZoneId
    from .private_data import PrivateData
    from .private_execution_result import PrivateExecutionResult
    from .private_execution_result_metrics import PrivateExecutionResultMetrics
_dynamic_imports: typing.Dict[str, str] = {
    "AccessToken": ".access_token",
    "ConsentId": ".consent_id",
    "ContractId": ".contract_id",
    "DataId": ".data_id",
    "DataProviderId": ".data_provider_id",
    "ExecutionResult": ".execution_result",
    "ExecutionResultMetrics": ".execution_result_metrics",
    "Function": ".function",
    "FunctionId": ".function_id",
    "FunctionProviderId": ".function_provider_id",
    "PrivacyZoneData": ".privacy_zone_data",
    "PrivacyZoneId": ".privacy_zone_id",
    "PrivateData": ".private_data",
    "PrivateExecutionResult": ".private_execution_result",
    "PrivateExecutionResultMetrics": ".private_execution_result_metrics",
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
    "AccessToken",
    "ConsentId",
    "ContractId",
    "DataId",
    "DataProviderId",
    "ExecutionResult",
    "ExecutionResultMetrics",
    "Function",
    "FunctionId",
    "FunctionProviderId",
    "PrivacyZoneData",
    "PrivacyZoneId",
    "PrivateData",
    "PrivateExecutionResult",
    "PrivateExecutionResultMetrics",
]
