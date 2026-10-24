



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .mix_batch_request import MixBatchRequest, MixBatchRequest_Recipe, MixBatchRequest_Remix
    from .mix_batch_request_recipe import MixBatchRequestRecipe
    from .mix_batch_request_remix import MixBatchRequestRemix
_dynamic_imports: typing.Dict[str, str] = {
    "MixBatchRequest": ".mix_batch_request",
    "MixBatchRequestRecipe": ".mix_batch_request_recipe",
    "MixBatchRequestRemix": ".mix_batch_request_remix",
    "MixBatchRequest_Recipe": ".mix_batch_request",
    "MixBatchRequest_Remix": ".mix_batch_request",
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
    "MixBatchRequest",
    "MixBatchRequestRecipe",
    "MixBatchRequestRemix",
    "MixBatchRequest_Recipe",
    "MixBatchRequest_Remix",
]
