



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chisel_tool import ChiselTool
    from .chisel_tool_kind import ChiselToolKind
    from .kit import Kit
    from .label_map import LabelMap
    from .plane_tool import PlaneTool
    from .toolbox import Toolbox
    from .toolbox_racks import ToolboxRacks
    from .toolbox_sets_item import ToolboxSetsItem, ToolboxSetsItem_Chisel, ToolboxSetsItem_Plane
_dynamic_imports: typing.Dict[str, str] = {
    "ChiselTool": ".chisel_tool",
    "ChiselToolKind": ".chisel_tool_kind",
    "Kit": ".kit",
    "LabelMap": ".label_map",
    "PlaneTool": ".plane_tool",
    "Toolbox": ".toolbox",
    "ToolboxRacks": ".toolbox_racks",
    "ToolboxSetsItem": ".toolbox_sets_item",
    "ToolboxSetsItem_Chisel": ".toolbox_sets_item",
    "ToolboxSetsItem_Plane": ".toolbox_sets_item",
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
    "ChiselTool",
    "ChiselToolKind",
    "Kit",
    "LabelMap",
    "PlaneTool",
    "Toolbox",
    "ToolboxRacks",
    "ToolboxSetsItem",
    "ToolboxSetsItem_Chisel",
    "ToolboxSetsItem_Plane",
]
