



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_image_edit_request_model import CreateImageEditRequestModel
    from .create_image_edit_request_model_one import CreateImageEditRequestModelOne
    from .create_image_edit_request_response_format import CreateImageEditRequestResponseFormat
    from .create_image_edit_request_size import CreateImageEditRequestSize
    from .create_image_request_model import CreateImageRequestModel
    from .create_image_request_model_one import CreateImageRequestModelOne
    from .create_image_request_quality import CreateImageRequestQuality
    from .create_image_request_response_format import CreateImageRequestResponseFormat
    from .create_image_request_size import CreateImageRequestSize
    from .create_image_request_style import CreateImageRequestStyle
    from .create_image_variation_request_model import CreateImageVariationRequestModel
    from .create_image_variation_request_model_one import CreateImageVariationRequestModelOne
    from .create_image_variation_request_response_format import CreateImageVariationRequestResponseFormat
    from .create_image_variation_request_size import CreateImageVariationRequestSize
_dynamic_imports: typing.Dict[str, str] = {
    "CreateImageEditRequestModel": ".create_image_edit_request_model",
    "CreateImageEditRequestModelOne": ".create_image_edit_request_model_one",
    "CreateImageEditRequestResponseFormat": ".create_image_edit_request_response_format",
    "CreateImageEditRequestSize": ".create_image_edit_request_size",
    "CreateImageRequestModel": ".create_image_request_model",
    "CreateImageRequestModelOne": ".create_image_request_model_one",
    "CreateImageRequestQuality": ".create_image_request_quality",
    "CreateImageRequestResponseFormat": ".create_image_request_response_format",
    "CreateImageRequestSize": ".create_image_request_size",
    "CreateImageRequestStyle": ".create_image_request_style",
    "CreateImageVariationRequestModel": ".create_image_variation_request_model",
    "CreateImageVariationRequestModelOne": ".create_image_variation_request_model_one",
    "CreateImageVariationRequestResponseFormat": ".create_image_variation_request_response_format",
    "CreateImageVariationRequestSize": ".create_image_variation_request_size",
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
    "CreateImageEditRequestModel",
    "CreateImageEditRequestModelOne",
    "CreateImageEditRequestResponseFormat",
    "CreateImageEditRequestSize",
    "CreateImageRequestModel",
    "CreateImageRequestModelOne",
    "CreateImageRequestQuality",
    "CreateImageRequestResponseFormat",
    "CreateImageRequestSize",
    "CreateImageRequestStyle",
    "CreateImageVariationRequestModel",
    "CreateImageVariationRequestModelOne",
    "CreateImageVariationRequestResponseFormat",
    "CreateImageVariationRequestSize",
]
