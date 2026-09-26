



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ListProjectsRequestFilter,
        ListProjectsRequestRelation,
        ListProjectsRequestState,
        V1ProjectsCreateProject,
        V1ProjectsCreateProjectBudgetRecurrenceItem,
        V1ProjectsCreateProjectBudgetRecurrenceItemRecur,
        V1ProjectsCreateProjectBudgetRecurrenceItemRecurUntil,
        V1ProjectsCreateProjectBudgetScope,
        V1ProjectsCreateProjectBudgetType,
        V1ProjectsCreateProjectLabelsItem,
        V1ProjectsCreateProjectRateType,
        V1ProjectsCreateProjectUsersItem,
        V1ProjectsUpdateProject,
        V1ProjectsUpdateProjectBudgetRecurrenceItem,
        V1ProjectsUpdateProjectBudgetRecurrenceItemRecur,
        V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil,
        V1ProjectsUpdateProjectBudgetScope,
        V1ProjectsUpdateProjectBudgetType,
        V1ProjectsUpdateProjectLabelsItem,
        V1ProjectsUpdateProjectRateType,
        V1ProjectsUpdateProjectUsersItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ListProjectsRequestFilter": ".types",
    "ListProjectsRequestRelation": ".types",
    "ListProjectsRequestState": ".types",
    "V1ProjectsCreateProject": ".types",
    "V1ProjectsCreateProjectBudgetRecurrenceItem": ".types",
    "V1ProjectsCreateProjectBudgetRecurrenceItemRecur": ".types",
    "V1ProjectsCreateProjectBudgetRecurrenceItemRecurUntil": ".types",
    "V1ProjectsCreateProjectBudgetScope": ".types",
    "V1ProjectsCreateProjectBudgetType": ".types",
    "V1ProjectsCreateProjectLabelsItem": ".types",
    "V1ProjectsCreateProjectRateType": ".types",
    "V1ProjectsCreateProjectUsersItem": ".types",
    "V1ProjectsUpdateProject": ".types",
    "V1ProjectsUpdateProjectBudgetRecurrenceItem": ".types",
    "V1ProjectsUpdateProjectBudgetRecurrenceItemRecur": ".types",
    "V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil": ".types",
    "V1ProjectsUpdateProjectBudgetScope": ".types",
    "V1ProjectsUpdateProjectBudgetType": ".types",
    "V1ProjectsUpdateProjectLabelsItem": ".types",
    "V1ProjectsUpdateProjectRateType": ".types",
    "V1ProjectsUpdateProjectUsersItem": ".types",
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
