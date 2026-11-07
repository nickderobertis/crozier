



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .worker_all_response_item import WorkerAllResponseItem
    from .worker_all_response_item_visibility import WorkerAllResponseItemVisibility
    from .worker_delete_response import WorkerDeleteResponse
    from .worker_delete_response_visibility import WorkerDeleteResponseVisibility
    from .worker_get_response import WorkerGetResponse
    from .worker_get_response_visibility import WorkerGetResponseVisibility
    from .worker_get_revisions_response_item import WorkerGetRevisionsResponseItem
    from .worker_toggle_active_response import WorkerToggleActiveResponse
    from .worker_toggle_active_response_visibility import WorkerToggleActiveResponseVisibility
    from .worker_upsert_response import WorkerUpsertResponse
    from .worker_upsert_response_visibility import WorkerUpsertResponseVisibility
_dynamic_imports: typing.Dict[str, str] = {
    "WorkerAllResponseItem": ".worker_all_response_item",
    "WorkerAllResponseItemVisibility": ".worker_all_response_item_visibility",
    "WorkerDeleteResponse": ".worker_delete_response",
    "WorkerDeleteResponseVisibility": ".worker_delete_response_visibility",
    "WorkerGetResponse": ".worker_get_response",
    "WorkerGetResponseVisibility": ".worker_get_response_visibility",
    "WorkerGetRevisionsResponseItem": ".worker_get_revisions_response_item",
    "WorkerToggleActiveResponse": ".worker_toggle_active_response",
    "WorkerToggleActiveResponseVisibility": ".worker_toggle_active_response_visibility",
    "WorkerUpsertResponse": ".worker_upsert_response",
    "WorkerUpsertResponseVisibility": ".worker_upsert_response_visibility",
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
    "WorkerAllResponseItem",
    "WorkerAllResponseItemVisibility",
    "WorkerDeleteResponse",
    "WorkerDeleteResponseVisibility",
    "WorkerGetResponse",
    "WorkerGetResponseVisibility",
    "WorkerGetRevisionsResponseItem",
    "WorkerToggleActiveResponse",
    "WorkerToggleActiveResponseVisibility",
    "WorkerUpsertResponse",
    "WorkerUpsertResponseVisibility",
]
