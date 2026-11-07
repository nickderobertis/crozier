



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .pipeline_check_request_only import PipelineCheckRequestOnly
    from .pipeline_setup_request_only import PipelineSetupRequestOnly
    from .pipeline_teardown_request_only import PipelineTeardownRequestOnly
    from .source_discover_request_source import SourceDiscoverRequestSource
_dynamic_imports: typing.Dict[str, str] = {
    "PipelineCheckRequestOnly": ".pipeline_check_request_only",
    "PipelineSetupRequestOnly": ".pipeline_setup_request_only",
    "PipelineTeardownRequestOnly": ".pipeline_teardown_request_only",
    "SourceDiscoverRequestSource": ".source_discover_request_source",
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
    "PipelineCheckRequestOnly",
    "PipelineSetupRequestOnly",
    "PipelineTeardownRequestOnly",
    "SourceDiscoverRequestSource",
]
