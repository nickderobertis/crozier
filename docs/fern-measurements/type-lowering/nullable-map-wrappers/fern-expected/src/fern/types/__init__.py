



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .git_script import GitScript
    from .inline_script import InlineScript
    from .job_results import JobResults
    from .link import Link
    from .plan import Plan
    from .plan_activities_value import PlanActivitiesValue, PlanActivitiesValue_Git, PlanActivitiesValue_Inline
    from .result_value import ResultValue
_dynamic_imports: typing.Dict[str, str] = {
    "GitScript": ".git_script",
    "InlineScript": ".inline_script",
    "JobResults": ".job_results",
    "Link": ".link",
    "Plan": ".plan",
    "PlanActivitiesValue": ".plan_activities_value",
    "PlanActivitiesValue_Git": ".plan_activities_value",
    "PlanActivitiesValue_Inline": ".plan_activities_value",
    "ResultValue": ".result_value",
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
    "GitScript",
    "InlineScript",
    "JobResults",
    "Link",
    "Plan",
    "PlanActivitiesValue",
    "PlanActivitiesValue_Git",
    "PlanActivitiesValue_Inline",
    "ResultValue",
]
