



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .column_config import ColumnConfig
    from .export_response import ExportResponse
    from .export_response_tables_item import ExportResponseTablesItem
    from .export_response_tables_item_configuration import ExportResponseTablesItemConfiguration
    from .font_assignments import FontAssignments
    from .table_config import TableConfig
    from .theme import Theme
    from .theme_fonts import ThemeFonts
_dynamic_imports: typing.Dict[str, str] = {
    "ColumnConfig": ".column_config",
    "ExportResponse": ".export_response",
    "ExportResponseTablesItem": ".export_response_tables_item",
    "ExportResponseTablesItemConfiguration": ".export_response_tables_item_configuration",
    "FontAssignments": ".font_assignments",
    "TableConfig": ".table_config",
    "Theme": ".theme",
    "ThemeFonts": ".theme_fonts",
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
    "ColumnConfig",
    "ExportResponse",
    "ExportResponseTablesItem",
    "ExportResponseTablesItemConfiguration",
    "FontAssignments",
    "TableConfig",
    "Theme",
    "ThemeFonts",
]
