



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bounding_box import BoundingBox
    from .connected_symbols_connection_item import ConnectedSymbolsConnectionItem
    from .connected_symbols_item import ConnectedSymbolsItem
    from .flow_direction import FlowDirection
    from .graph_construction_inference_response import GraphConstructionInferenceResponse
    from .http_validation_error import HttpValidationError
    from .image_details import ImageDetails
    from .inference_result import InferenceResult
    from .label import Label
    from .line_detection_inference_response import LineDetectionInferenceResponse
    from .line_segment import LineSegment
    from .symbol_and_text_associated import SymbolAndTextAssociated
    from .symbol_detection_inference_response import SymbolDetectionInferenceResponse
    from .text_detection_inference_response import TextDetectionInferenceResponse
    from .text_recognized import TextRecognized
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "BoundingBox": ".bounding_box",
    "ConnectedSymbolsConnectionItem": ".connected_symbols_connection_item",
    "ConnectedSymbolsItem": ".connected_symbols_item",
    "FlowDirection": ".flow_direction",
    "GraphConstructionInferenceResponse": ".graph_construction_inference_response",
    "HttpValidationError": ".http_validation_error",
    "ImageDetails": ".image_details",
    "InferenceResult": ".inference_result",
    "Label": ".label",
    "LineDetectionInferenceResponse": ".line_detection_inference_response",
    "LineSegment": ".line_segment",
    "SymbolAndTextAssociated": ".symbol_and_text_associated",
    "SymbolDetectionInferenceResponse": ".symbol_detection_inference_response",
    "TextDetectionInferenceResponse": ".text_detection_inference_response",
    "TextRecognized": ".text_recognized",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "BoundingBox",
    "ConnectedSymbolsConnectionItem",
    "ConnectedSymbolsItem",
    "FlowDirection",
    "GraphConstructionInferenceResponse",
    "HttpValidationError",
    "ImageDetails",
    "InferenceResult",
    "Label",
    "LineDetectionInferenceResponse",
    "LineSegment",
    "SymbolAndTextAssociated",
    "SymbolDetectionInferenceResponse",
    "TextDetectionInferenceResponse",
    "TextRecognized",
    "ValidationError",
    "ValidationErrorLocItem",
]
