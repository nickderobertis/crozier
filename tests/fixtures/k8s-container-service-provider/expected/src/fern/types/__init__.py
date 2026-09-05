



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .container import Container
    from .container_cpu import ContainerCpu
    from .container_env_var import ContainerEnvVar
    from .container_image import ContainerImage
    from .container_list import ContainerList
    from .container_memory import ContainerMemory
    from .container_metadata import ContainerMetadata
    from .container_network import ContainerNetwork
    from .container_port import ContainerPort
    from .container_port_visibility import ContainerPortVisibility
    from .container_process import ContainerProcess
    from .container_resources import ContainerResources
    from .container_spec import ContainerSpec
    from .container_spec_service_type import ContainerSpecServiceType
    from .container_status import ContainerStatus
    from .error import Error
    from .error_detail import ErrorDetail
    from .error_type import ErrorType
    from .health import Health
    from .service_info import ServiceInfo
    from .service_info_type import ServiceInfoType
    from .service_port import ServicePort
_dynamic_imports: typing.Dict[str, str] = {
    "Container": ".container",
    "ContainerCpu": ".container_cpu",
    "ContainerEnvVar": ".container_env_var",
    "ContainerImage": ".container_image",
    "ContainerList": ".container_list",
    "ContainerMemory": ".container_memory",
    "ContainerMetadata": ".container_metadata",
    "ContainerNetwork": ".container_network",
    "ContainerPort": ".container_port",
    "ContainerPortVisibility": ".container_port_visibility",
    "ContainerProcess": ".container_process",
    "ContainerResources": ".container_resources",
    "ContainerSpec": ".container_spec",
    "ContainerSpecServiceType": ".container_spec_service_type",
    "ContainerStatus": ".container_status",
    "Error": ".error",
    "ErrorDetail": ".error_detail",
    "ErrorType": ".error_type",
    "Health": ".health",
    "ServiceInfo": ".service_info",
    "ServiceInfoType": ".service_info_type",
    "ServicePort": ".service_port",
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
    "Container",
    "ContainerCpu",
    "ContainerEnvVar",
    "ContainerImage",
    "ContainerList",
    "ContainerMemory",
    "ContainerMetadata",
    "ContainerNetwork",
    "ContainerPort",
    "ContainerPortVisibility",
    "ContainerProcess",
    "ContainerResources",
    "ContainerSpec",
    "ContainerSpecServiceType",
    "ContainerStatus",
    "Error",
    "ErrorDetail",
    "ErrorType",
    "Health",
    "ServiceInfo",
    "ServiceInfoType",
    "ServicePort",
]
