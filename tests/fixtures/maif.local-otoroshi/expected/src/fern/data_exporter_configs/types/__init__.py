



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_bulk_data_exporter_configs_response_item import CreateBulkDataExporterConfigsResponseItem
    from .create_bulk_data_exporter_configs_response_item_status import CreateBulkDataExporterConfigsResponseItemStatus
    from .deletebulk_data_exporter_config_response_item import DeletebulkDataExporterConfigResponseItem
    from .deletebulk_data_exporter_config_response_item_status import DeletebulkDataExporterConfigResponseItemStatus
    from .patch_bulk_data_exporter_config_response_item import PatchBulkDataExporterConfigResponseItem
    from .patch_bulk_data_exporter_config_response_item_status import PatchBulkDataExporterConfigResponseItemStatus
    from .update_bulk_data_exporter_config_response_item import UpdateBulkDataExporterConfigResponseItem
    from .update_bulk_data_exporter_config_response_item_status import UpdateBulkDataExporterConfigResponseItemStatus
_dynamic_imports: typing.Dict[str, str] = {
    "CreateBulkDataExporterConfigsResponseItem": ".create_bulk_data_exporter_configs_response_item",
    "CreateBulkDataExporterConfigsResponseItemStatus": ".create_bulk_data_exporter_configs_response_item_status",
    "DeletebulkDataExporterConfigResponseItem": ".deletebulk_data_exporter_config_response_item",
    "DeletebulkDataExporterConfigResponseItemStatus": ".deletebulk_data_exporter_config_response_item_status",
    "PatchBulkDataExporterConfigResponseItem": ".patch_bulk_data_exporter_config_response_item",
    "PatchBulkDataExporterConfigResponseItemStatus": ".patch_bulk_data_exporter_config_response_item_status",
    "UpdateBulkDataExporterConfigResponseItem": ".update_bulk_data_exporter_config_response_item",
    "UpdateBulkDataExporterConfigResponseItemStatus": ".update_bulk_data_exporter_config_response_item_status",
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
    "CreateBulkDataExporterConfigsResponseItem",
    "CreateBulkDataExporterConfigsResponseItemStatus",
    "DeletebulkDataExporterConfigResponseItem",
    "DeletebulkDataExporterConfigResponseItemStatus",
    "PatchBulkDataExporterConfigResponseItem",
    "PatchBulkDataExporterConfigResponseItemStatus",
    "UpdateBulkDataExporterConfigResponseItem",
    "UpdateBulkDataExporterConfigResponseItemStatus",
]
