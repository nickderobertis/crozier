



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .any_value import AnyValue
    from .default_data import DefaultData
    from .feedback import Feedback
    from .meta import Meta
    from .metric import Metric
    from .metric_type import MetricType
    from .seldon_message import SeldonMessage
    from .seldon_message_list import SeldonMessageList
    from .status import Status
    from .status_status_flag import StatusStatusFlag
    from .tensor import Tensor
    from .tensor_shape_proto_dim import TensorShapeProtoDim
    from .tensorflow_data_type import TensorflowDataType
    from .tensorflow_resource_handle_proto import TensorflowResourceHandleProto
    from .tensorflow_tensor_proto import TensorflowTensorProto
    from .tensorflow_tensor_shape_proto import TensorflowTensorShapeProto
    from .tensorflow_variant_tensor_data_proto import TensorflowVariantTensorDataProto
_dynamic_imports: typing.Dict[str, str] = {
    "AnyValue": ".any_value",
    "DefaultData": ".default_data",
    "Feedback": ".feedback",
    "Meta": ".meta",
    "Metric": ".metric",
    "MetricType": ".metric_type",
    "SeldonMessage": ".seldon_message",
    "SeldonMessageList": ".seldon_message_list",
    "Status": ".status",
    "StatusStatusFlag": ".status_status_flag",
    "Tensor": ".tensor",
    "TensorShapeProtoDim": ".tensor_shape_proto_dim",
    "TensorflowDataType": ".tensorflow_data_type",
    "TensorflowResourceHandleProto": ".tensorflow_resource_handle_proto",
    "TensorflowTensorProto": ".tensorflow_tensor_proto",
    "TensorflowTensorShapeProto": ".tensorflow_tensor_shape_proto",
    "TensorflowVariantTensorDataProto": ".tensorflow_variant_tensor_data_proto",
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
    "AnyValue",
    "DefaultData",
    "Feedback",
    "Meta",
    "Metric",
    "MetricType",
    "SeldonMessage",
    "SeldonMessageList",
    "Status",
    "StatusStatusFlag",
    "Tensor",
    "TensorShapeProtoDim",
    "TensorflowDataType",
    "TensorflowResourceHandleProto",
    "TensorflowTensorProto",
    "TensorflowTensorShapeProto",
    "TensorflowVariantTensorDataProto",
]
