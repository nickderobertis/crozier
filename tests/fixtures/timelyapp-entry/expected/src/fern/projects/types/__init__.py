



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_projects_request_filter import ListProjectsRequestFilter
    from .list_projects_request_relation import ListProjectsRequestRelation
    from .list_projects_request_state import ListProjectsRequestState
    from .v1projects_create_project import V1ProjectsCreateProject
    from .v1projects_create_project_budget_recurrence_item import V1ProjectsCreateProjectBudgetRecurrenceItem
    from .v1projects_create_project_budget_recurrence_item_recur import V1ProjectsCreateProjectBudgetRecurrenceItemRecur
    from .v1projects_create_project_budget_recurrence_item_recur_until import (
        V1ProjectsCreateProjectBudgetRecurrenceItemRecurUntil,
    )
    from .v1projects_create_project_budget_scope import V1ProjectsCreateProjectBudgetScope
    from .v1projects_create_project_budget_type import V1ProjectsCreateProjectBudgetType
    from .v1projects_create_project_labels_item import V1ProjectsCreateProjectLabelsItem
    from .v1projects_create_project_rate_type import V1ProjectsCreateProjectRateType
    from .v1projects_create_project_users_item import V1ProjectsCreateProjectUsersItem
    from .v1projects_update_project import V1ProjectsUpdateProject
    from .v1projects_update_project_budget_recurrence_item import V1ProjectsUpdateProjectBudgetRecurrenceItem
    from .v1projects_update_project_budget_recurrence_item_recur import V1ProjectsUpdateProjectBudgetRecurrenceItemRecur
    from .v1projects_update_project_budget_recurrence_item_recur_until import (
        V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil,
    )
    from .v1projects_update_project_budget_scope import V1ProjectsUpdateProjectBudgetScope
    from .v1projects_update_project_budget_type import V1ProjectsUpdateProjectBudgetType
    from .v1projects_update_project_labels_item import V1ProjectsUpdateProjectLabelsItem
    from .v1projects_update_project_rate_type import V1ProjectsUpdateProjectRateType
    from .v1projects_update_project_users_item import V1ProjectsUpdateProjectUsersItem
_dynamic_imports: typing.Dict[str, str] = {
    "ListProjectsRequestFilter": ".list_projects_request_filter",
    "ListProjectsRequestRelation": ".list_projects_request_relation",
    "ListProjectsRequestState": ".list_projects_request_state",
    "V1ProjectsCreateProject": ".v1projects_create_project",
    "V1ProjectsCreateProjectBudgetRecurrenceItem": ".v1projects_create_project_budget_recurrence_item",
    "V1ProjectsCreateProjectBudgetRecurrenceItemRecur": ".v1projects_create_project_budget_recurrence_item_recur",
    "V1ProjectsCreateProjectBudgetRecurrenceItemRecurUntil": ".v1projects_create_project_budget_recurrence_item_recur_until",
    "V1ProjectsCreateProjectBudgetScope": ".v1projects_create_project_budget_scope",
    "V1ProjectsCreateProjectBudgetType": ".v1projects_create_project_budget_type",
    "V1ProjectsCreateProjectLabelsItem": ".v1projects_create_project_labels_item",
    "V1ProjectsCreateProjectRateType": ".v1projects_create_project_rate_type",
    "V1ProjectsCreateProjectUsersItem": ".v1projects_create_project_users_item",
    "V1ProjectsUpdateProject": ".v1projects_update_project",
    "V1ProjectsUpdateProjectBudgetRecurrenceItem": ".v1projects_update_project_budget_recurrence_item",
    "V1ProjectsUpdateProjectBudgetRecurrenceItemRecur": ".v1projects_update_project_budget_recurrence_item_recur",
    "V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil": ".v1projects_update_project_budget_recurrence_item_recur_until",
    "V1ProjectsUpdateProjectBudgetScope": ".v1projects_update_project_budget_scope",
    "V1ProjectsUpdateProjectBudgetType": ".v1projects_update_project_budget_type",
    "V1ProjectsUpdateProjectLabelsItem": ".v1projects_update_project_labels_item",
    "V1ProjectsUpdateProjectRateType": ".v1projects_update_project_rate_type",
    "V1ProjectsUpdateProjectUsersItem": ".v1projects_update_project_users_item",
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
    "ListProjectsRequestFilter",
    "ListProjectsRequestRelation",
    "ListProjectsRequestState",
    "V1ProjectsCreateProject",
    "V1ProjectsCreateProjectBudgetRecurrenceItem",
    "V1ProjectsCreateProjectBudgetRecurrenceItemRecur",
    "V1ProjectsCreateProjectBudgetRecurrenceItemRecurUntil",
    "V1ProjectsCreateProjectBudgetScope",
    "V1ProjectsCreateProjectBudgetType",
    "V1ProjectsCreateProjectLabelsItem",
    "V1ProjectsCreateProjectRateType",
    "V1ProjectsCreateProjectUsersItem",
    "V1ProjectsUpdateProject",
    "V1ProjectsUpdateProjectBudgetRecurrenceItem",
    "V1ProjectsUpdateProjectBudgetRecurrenceItemRecur",
    "V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil",
    "V1ProjectsUpdateProjectBudgetScope",
    "V1ProjectsUpdateProjectBudgetType",
    "V1ProjectsUpdateProjectLabelsItem",
    "V1ProjectsUpdateProjectRateType",
    "V1ProjectsUpdateProjectUsersItem",
]
