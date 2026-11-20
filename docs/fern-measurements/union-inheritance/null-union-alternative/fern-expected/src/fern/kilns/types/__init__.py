



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .adjust_kiln_settings_request_changes_item import AdjustKilnSettingsRequestChangesItem
    from .adjust_kiln_settings_request_changes_item_reading import AdjustKilnSettingsRequestChangesItemReading
    from .adjust_kiln_settings_request_changes_item_reading_one_item import (
        AdjustKilnSettingsRequestChangesItemReadingOneItem,
    )
    from .adjust_kiln_settings_request_changes_item_reading_zero import AdjustKilnSettingsRequestChangesItemReadingZero
    from .register_kiln_request_settings_value import RegisterKilnRequestSettingsValue
    from .register_kiln_request_settings_value_one_item import RegisterKilnRequestSettingsValueOneItem
    from .register_kiln_request_settings_value_zero import RegisterKilnRequestSettingsValueZero
_dynamic_imports: typing.Dict[str, str] = {
    "AdjustKilnSettingsRequestChangesItem": ".adjust_kiln_settings_request_changes_item",
    "AdjustKilnSettingsRequestChangesItemReading": ".adjust_kiln_settings_request_changes_item_reading",
    "AdjustKilnSettingsRequestChangesItemReadingOneItem": ".adjust_kiln_settings_request_changes_item_reading_one_item",
    "AdjustKilnSettingsRequestChangesItemReadingZero": ".adjust_kiln_settings_request_changes_item_reading_zero",
    "RegisterKilnRequestSettingsValue": ".register_kiln_request_settings_value",
    "RegisterKilnRequestSettingsValueOneItem": ".register_kiln_request_settings_value_one_item",
    "RegisterKilnRequestSettingsValueZero": ".register_kiln_request_settings_value_zero",
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
    "AdjustKilnSettingsRequestChangesItem",
    "AdjustKilnSettingsRequestChangesItemReading",
    "AdjustKilnSettingsRequestChangesItemReadingOneItem",
    "AdjustKilnSettingsRequestChangesItemReadingZero",
    "RegisterKilnRequestSettingsValue",
    "RegisterKilnRequestSettingsValueOneItem",
    "RegisterKilnRequestSettingsValueZero",
]
