



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetProjectIntegrationConfigGenaiResponse,
        GetProjectIntegrationConfigGenaiResponse_AwsBedrock,
        GetProjectIntegrationConfigGenaiResponse_Bam,
        GetProjectIntegrationConfigGenaiResponse_Cpd,
        GetProjectIntegrationConfigGenaiResponse_HfApi,
        GetProjectIntegrationConfigGenaiResponse_Openai,
        GetProjectIntegrationConfigGenaiResponse_Watsonx,
        UpdateProjectIntegrationConfigGenaiRequestBody,
        UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock,
        UpdateProjectIntegrationConfigGenaiRequestBody_Bam,
        UpdateProjectIntegrationConfigGenaiRequestBody_Cpd,
        UpdateProjectIntegrationConfigGenaiRequestBody_HfApi,
        UpdateProjectIntegrationConfigGenaiRequestBody_Openai,
        UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetProjectIntegrationConfigGenaiResponse": ".types",
    "GetProjectIntegrationConfigGenaiResponse_AwsBedrock": ".types",
    "GetProjectIntegrationConfigGenaiResponse_Bam": ".types",
    "GetProjectIntegrationConfigGenaiResponse_Cpd": ".types",
    "GetProjectIntegrationConfigGenaiResponse_HfApi": ".types",
    "GetProjectIntegrationConfigGenaiResponse_Openai": ".types",
    "GetProjectIntegrationConfigGenaiResponse_Watsonx": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Bam": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Cpd": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody_HfApi": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Openai": ".types",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx": ".types",
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
    "GetProjectIntegrationConfigGenaiResponse",
    "GetProjectIntegrationConfigGenaiResponse_AwsBedrock",
    "GetProjectIntegrationConfigGenaiResponse_Bam",
    "GetProjectIntegrationConfigGenaiResponse_Cpd",
    "GetProjectIntegrationConfigGenaiResponse_HfApi",
    "GetProjectIntegrationConfigGenaiResponse_Openai",
    "GetProjectIntegrationConfigGenaiResponse_Watsonx",
    "UpdateProjectIntegrationConfigGenaiRequestBody",
    "UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Bam",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Cpd",
    "UpdateProjectIntegrationConfigGenaiRequestBody_HfApi",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Openai",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx",
]
