



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .workflow import Workflow
    from .workflow_dto import WorkflowDto
    from .workflows_filter import WorkflowsFilter
    from .workflows_filter_fields import WorkflowsFilterFields
    from .workflows_filter_fields_created_by import WorkflowsFilterFieldsCreatedBy
    from .workflows_filter_fields_one_item import WorkflowsFilterFieldsOneItem
    from .workflows_filter_include_item import WorkflowsFilterIncludeItem
    from .workflows_filter_order import WorkflowsFilterOrder
    from .workflows_include_filter_items import WorkflowsIncludeFilterItems
    from .workflows_include_filter_items_relation import WorkflowsIncludeFilterItemsRelation
    from .workflows_scope_filter import WorkflowsScopeFilter
    from .workflows_scope_filter_fields import WorkflowsScopeFilterFields
    from .workflows_scope_filter_order import WorkflowsScopeFilterOrder
_dynamic_imports: typing.Dict[str, str] = {
    "Workflow": ".workflow",
    "WorkflowDto": ".workflow_dto",
    "WorkflowsFilter": ".workflows_filter",
    "WorkflowsFilterFields": ".workflows_filter_fields",
    "WorkflowsFilterFieldsCreatedBy": ".workflows_filter_fields_created_by",
    "WorkflowsFilterFieldsOneItem": ".workflows_filter_fields_one_item",
    "WorkflowsFilterIncludeItem": ".workflows_filter_include_item",
    "WorkflowsFilterOrder": ".workflows_filter_order",
    "WorkflowsIncludeFilterItems": ".workflows_include_filter_items",
    "WorkflowsIncludeFilterItemsRelation": ".workflows_include_filter_items_relation",
    "WorkflowsScopeFilter": ".workflows_scope_filter",
    "WorkflowsScopeFilterFields": ".workflows_scope_filter_fields",
    "WorkflowsScopeFilterOrder": ".workflows_scope_filter_order",
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
    "Workflow",
    "WorkflowDto",
    "WorkflowsFilter",
    "WorkflowsFilterFields",
    "WorkflowsFilterFieldsCreatedBy",
    "WorkflowsFilterFieldsOneItem",
    "WorkflowsFilterIncludeItem",
    "WorkflowsFilterOrder",
    "WorkflowsIncludeFilterItems",
    "WorkflowsIncludeFilterItemsRelation",
    "WorkflowsScopeFilter",
    "WorkflowsScopeFilterFields",
    "WorkflowsScopeFilterOrder",
]
