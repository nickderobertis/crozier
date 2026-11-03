



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .course import Course
    from .create_plan_body_course import CreatePlanBodyCourse
    from .create_plan_body_diet import CreatePlanBodyDiet
    from .diet import Diet
    from .garnish import Garnish
    from .grain import Grain
    from .herb import Herb
    from .herb_kind import HerbKind
    from .pairing import Pairing
    from .plan import Plan
    from .plan_course import PlanCourse
    from .plan_extras import PlanExtras
    from .plan_sides import PlanSides, PlanSides_Grain, PlanSides_Herb
    from .side import Side, Side_Grain, Side_Herb
_dynamic_imports: typing.Dict[str, str] = {
    "Course": ".course",
    "CreatePlanBodyCourse": ".create_plan_body_course",
    "CreatePlanBodyDiet": ".create_plan_body_diet",
    "Diet": ".diet",
    "Garnish": ".garnish",
    "Grain": ".grain",
    "Herb": ".herb",
    "HerbKind": ".herb_kind",
    "Pairing": ".pairing",
    "Plan": ".plan",
    "PlanCourse": ".plan_course",
    "PlanExtras": ".plan_extras",
    "PlanSides": ".plan_sides",
    "PlanSides_Grain": ".plan_sides",
    "PlanSides_Herb": ".plan_sides",
    "Side": ".side",
    "Side_Grain": ".side",
    "Side_Herb": ".side",
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
    "Course",
    "CreatePlanBodyCourse",
    "CreatePlanBodyDiet",
    "Diet",
    "Garnish",
    "Grain",
    "Herb",
    "HerbKind",
    "Pairing",
    "Plan",
    "PlanCourse",
    "PlanExtras",
    "PlanSides",
    "PlanSides_Grain",
    "PlanSides_Herb",
    "Side",
    "Side_Grain",
    "Side_Herb",
]
