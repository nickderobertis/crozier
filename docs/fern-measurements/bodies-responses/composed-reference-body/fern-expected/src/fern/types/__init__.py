



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bead_ref import BeadRef, BeadRef_Glass, BeadRef_Wood
    from .blend_dye import BlendDye
    from .blend_yarn import BlendYarn
    from .glass_bead import GlassBead
    from .knot import Knot
    from .plain_pattern import PlainPattern
    from .twill_pattern import TwillPattern
    from .warp_thread import WarpThread
    from .weave import Weave
    from .weave_finish import WeaveFinish
    from .weave_finish_delivery import WeaveFinishDelivery
    from .weave_plan import WeavePlan
    from .weave_plan_finish import WeavePlanFinish
    from .weave_plan_pattern import WeavePlanPattern, WeavePlanPattern_Plain, WeavePlanPattern_Twill
    from .weave_plan_threads_item import WeavePlanThreadsItem, WeavePlanThreadsItem_Warp, WeavePlanThreadsItem_Weft
    from .weft_thread import WeftThread
    from .wood_bead import WoodBead
_dynamic_imports: typing.Dict[str, str] = {
    "BeadRef": ".bead_ref",
    "BeadRef_Glass": ".bead_ref",
    "BeadRef_Wood": ".bead_ref",
    "BlendDye": ".blend_dye",
    "BlendYarn": ".blend_yarn",
    "GlassBead": ".glass_bead",
    "Knot": ".knot",
    "PlainPattern": ".plain_pattern",
    "TwillPattern": ".twill_pattern",
    "WarpThread": ".warp_thread",
    "Weave": ".weave",
    "WeaveFinish": ".weave_finish",
    "WeaveFinishDelivery": ".weave_finish_delivery",
    "WeavePlan": ".weave_plan",
    "WeavePlanFinish": ".weave_plan_finish",
    "WeavePlanPattern": ".weave_plan_pattern",
    "WeavePlanPattern_Plain": ".weave_plan_pattern",
    "WeavePlanPattern_Twill": ".weave_plan_pattern",
    "WeavePlanThreadsItem": ".weave_plan_threads_item",
    "WeavePlanThreadsItem_Warp": ".weave_plan_threads_item",
    "WeavePlanThreadsItem_Weft": ".weave_plan_threads_item",
    "WeftThread": ".weft_thread",
    "WoodBead": ".wood_bead",
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
    "BeadRef",
    "BeadRef_Glass",
    "BeadRef_Wood",
    "BlendDye",
    "BlendYarn",
    "GlassBead",
    "Knot",
    "PlainPattern",
    "TwillPattern",
    "WarpThread",
    "Weave",
    "WeaveFinish",
    "WeaveFinishDelivery",
    "WeavePlan",
    "WeavePlanFinish",
    "WeavePlanPattern",
    "WeavePlanPattern_Plain",
    "WeavePlanPattern_Twill",
    "WeavePlanThreadsItem",
    "WeavePlanThreadsItem_Warp",
    "WeavePlanThreadsItem_Weft",
    "WeftThread",
    "WoodBead",
]
