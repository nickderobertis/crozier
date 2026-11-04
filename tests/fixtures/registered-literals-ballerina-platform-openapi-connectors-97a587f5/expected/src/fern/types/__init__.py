



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .capabilities import Capabilities
    from .deprecation import Deprecation
    from .error import Error
    from .error_code import ErrorCode
    from .error_response import ErrorResponse
    from .event import Event
    from .event_list import EventList
    from .file import File
    from .file_list import FileList
    from .file_statistics import FileStatistics
    from .fine_tune import FineTune
    from .fine_tune_list import FineTuneList
    from .hyper_parameters import HyperParameters
    from .inner_error import InnerError
    from .inner_error_code import InnerErrorCode
    from .life_cycle_status import LifeCycleStatus
    from .log_level import LogLevel
    from .model import Model
    from .model_list import ModelList
    from .purpose import Purpose
    from .scale_type import ScaleType
    from .state import State
    from .type_discriminator import TypeDiscriminator
_dynamic_imports: typing.Dict[str, str] = {
    "Capabilities": ".capabilities",
    "Deprecation": ".deprecation",
    "Error": ".error",
    "ErrorCode": ".error_code",
    "ErrorResponse": ".error_response",
    "Event": ".event",
    "EventList": ".event_list",
    "File": ".file",
    "FileList": ".file_list",
    "FileStatistics": ".file_statistics",
    "FineTune": ".fine_tune",
    "FineTuneList": ".fine_tune_list",
    "HyperParameters": ".hyper_parameters",
    "InnerError": ".inner_error",
    "InnerErrorCode": ".inner_error_code",
    "LifeCycleStatus": ".life_cycle_status",
    "LogLevel": ".log_level",
    "Model": ".model",
    "ModelList": ".model_list",
    "Purpose": ".purpose",
    "ScaleType": ".scale_type",
    "State": ".state",
    "TypeDiscriminator": ".type_discriminator",
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
    "Capabilities",
    "Deprecation",
    "Error",
    "ErrorCode",
    "ErrorResponse",
    "Event",
    "EventList",
    "File",
    "FileList",
    "FileStatistics",
    "FineTune",
    "FineTuneList",
    "HyperParameters",
    "InnerError",
    "InnerErrorCode",
    "LifeCycleStatus",
    "LogLevel",
    "Model",
    "ModelList",
    "Purpose",
    "ScaleType",
    "State",
    "TypeDiscriminator",
]
