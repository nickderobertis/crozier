



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_project_integration_config_genai_response import (
        GetProjectIntegrationConfigGenaiResponse,
        GetProjectIntegrationConfigGenaiResponse_AwsBedrock,
        GetProjectIntegrationConfigGenaiResponse_Bam,
        GetProjectIntegrationConfigGenaiResponse_Cpd,
        GetProjectIntegrationConfigGenaiResponse_HfApi,
        GetProjectIntegrationConfigGenaiResponse_Openai,
        GetProjectIntegrationConfigGenaiResponse_Watsonx,
    )
    from .update_project_integration_config_genai_request_body import (
        UpdateProjectIntegrationConfigGenaiRequestBody,
        UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock,
        UpdateProjectIntegrationConfigGenaiRequestBody_Bam,
        UpdateProjectIntegrationConfigGenaiRequestBody_Cpd,
        UpdateProjectIntegrationConfigGenaiRequestBody_HfApi,
        UpdateProjectIntegrationConfigGenaiRequestBody_Openai,
        UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetProjectIntegrationConfigGenaiResponse": ".get_project_integration_config_genai_response",
    "GetProjectIntegrationConfigGenaiResponse_AwsBedrock": ".get_project_integration_config_genai_response",
    "GetProjectIntegrationConfigGenaiResponse_Bam": ".get_project_integration_config_genai_response",
    "GetProjectIntegrationConfigGenaiResponse_Cpd": ".get_project_integration_config_genai_response",
    "GetProjectIntegrationConfigGenaiResponse_HfApi": ".get_project_integration_config_genai_response",
    "GetProjectIntegrationConfigGenaiResponse_Openai": ".get_project_integration_config_genai_response",
    "GetProjectIntegrationConfigGenaiResponse_Watsonx": ".get_project_integration_config_genai_response",
    "UpdateProjectIntegrationConfigGenaiRequestBody": ".update_project_integration_config_genai_request_body",
    "UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock": ".update_project_integration_config_genai_request_body",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Bam": ".update_project_integration_config_genai_request_body",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Cpd": ".update_project_integration_config_genai_request_body",
    "UpdateProjectIntegrationConfigGenaiRequestBody_HfApi": ".update_project_integration_config_genai_request_body",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Openai": ".update_project_integration_config_genai_request_body",
    "UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx": ".update_project_integration_config_genai_request_body",
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
