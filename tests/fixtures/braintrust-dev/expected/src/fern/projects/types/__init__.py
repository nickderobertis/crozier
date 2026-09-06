



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_project_response import GetProjectResponse
    from .patch_project_settings import PatchProjectSettings
    from .patch_project_settings_remote_eval_sources_item import PatchProjectSettingsRemoteEvalSourcesItem
    from .patch_project_settings_span_field_order_item import PatchProjectSettingsSpanFieldOrderItem
    from .patch_project_settings_span_field_order_item_layout import PatchProjectSettingsSpanFieldOrderItemLayout
    from .patch_project_settings_span_field_order_item_layout_one import PatchProjectSettingsSpanFieldOrderItemLayoutOne
    from .patch_project_settings_span_field_order_item_layout_zero import (
        PatchProjectSettingsSpanFieldOrderItemLayoutZero,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetProjectResponse": ".get_project_response",
    "PatchProjectSettings": ".patch_project_settings",
    "PatchProjectSettingsRemoteEvalSourcesItem": ".patch_project_settings_remote_eval_sources_item",
    "PatchProjectSettingsSpanFieldOrderItem": ".patch_project_settings_span_field_order_item",
    "PatchProjectSettingsSpanFieldOrderItemLayout": ".patch_project_settings_span_field_order_item_layout",
    "PatchProjectSettingsSpanFieldOrderItemLayoutOne": ".patch_project_settings_span_field_order_item_layout_one",
    "PatchProjectSettingsSpanFieldOrderItemLayoutZero": ".patch_project_settings_span_field_order_item_layout_zero",
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
    "GetProjectResponse",
    "PatchProjectSettings",
    "PatchProjectSettingsRemoteEvalSourcesItem",
    "PatchProjectSettingsSpanFieldOrderItem",
    "PatchProjectSettingsSpanFieldOrderItemLayout",
    "PatchProjectSettingsSpanFieldOrderItemLayoutOne",
    "PatchProjectSettingsSpanFieldOrderItemLayoutZero",
]
