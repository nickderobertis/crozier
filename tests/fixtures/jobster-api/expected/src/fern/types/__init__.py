



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .error import Error
    from .job_input import JobInput
    from .job_input_job_type import JobInputJobType
    from .job_input_status import JobInputStatus
    from .user_profile import UserProfile
_dynamic_imports: typing.Dict[str, str] = {
    "Error": ".error",
    "JobInput": ".job_input",
    "JobInputJobType": ".job_input_job_type",
    "JobInputStatus": ".job_input_status",
    "UserProfile": ".user_profile",
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


__all__ = ["Error", "JobInput", "JobInputJobType", "JobInputStatus", "UserProfile"]
