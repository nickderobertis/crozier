



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cn_statistics import CnStatistics
    from .cn_statistics_hlen import CnStatisticsHlen
    from .cn_statistics_keys import CnStatisticsKeys
    from .cn_statistics_klen import CnStatisticsKlen
    from .cn_statistics_ptombs import CnStatisticsPtombs
    from .cn_statistics_tombs import CnStatisticsTombs
    from .cn_statistics_vgarb import CnStatisticsVgarb
    from .cn_statistics_vlen import CnStatisticsVlen
    from .error import Error
    from .error_origin import ErrorOrigin
    from .events import Events
    from .events_item import EventsItem
    from .events_item_level import EventsItemLevel
    from .mclass import Mclass
    from .performance_counter import PerformanceCounter
    from .performance_counter_type import PerformanceCounterType
    from .performance_counters import PerformanceCounters
    from .performance_counters_item import PerformanceCountersItem
    from .performance_counters_item_counters_item import PerformanceCountersItemCountersItem
    from .performance_counters_item_counters_item_four import PerformanceCountersItemCountersItemFour
    from .performance_counters_item_counters_item_four_histogram_item import (
        PerformanceCountersItemCountersItemFourHistogramItem,
    )
    from .performance_counters_item_counters_item_one import PerformanceCountersItemCountersItemOne
    from .performance_counters_item_counters_item_three import PerformanceCountersItemCountersItemThree
    from .performance_counters_item_counters_item_two import PerformanceCountersItemCountersItemTwo
_dynamic_imports: typing.Dict[str, str] = {
    "CnStatistics": ".cn_statistics",
    "CnStatisticsHlen": ".cn_statistics_hlen",
    "CnStatisticsKeys": ".cn_statistics_keys",
    "CnStatisticsKlen": ".cn_statistics_klen",
    "CnStatisticsPtombs": ".cn_statistics_ptombs",
    "CnStatisticsTombs": ".cn_statistics_tombs",
    "CnStatisticsVgarb": ".cn_statistics_vgarb",
    "CnStatisticsVlen": ".cn_statistics_vlen",
    "Error": ".error",
    "ErrorOrigin": ".error_origin",
    "Events": ".events",
    "EventsItem": ".events_item",
    "EventsItemLevel": ".events_item_level",
    "Mclass": ".mclass",
    "PerformanceCounter": ".performance_counter",
    "PerformanceCounterType": ".performance_counter_type",
    "PerformanceCounters": ".performance_counters",
    "PerformanceCountersItem": ".performance_counters_item",
    "PerformanceCountersItemCountersItem": ".performance_counters_item_counters_item",
    "PerformanceCountersItemCountersItemFour": ".performance_counters_item_counters_item_four",
    "PerformanceCountersItemCountersItemFourHistogramItem": ".performance_counters_item_counters_item_four_histogram_item",
    "PerformanceCountersItemCountersItemOne": ".performance_counters_item_counters_item_one",
    "PerformanceCountersItemCountersItemThree": ".performance_counters_item_counters_item_three",
    "PerformanceCountersItemCountersItemTwo": ".performance_counters_item_counters_item_two",
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
    "CnStatistics",
    "CnStatisticsHlen",
    "CnStatisticsKeys",
    "CnStatisticsKlen",
    "CnStatisticsPtombs",
    "CnStatisticsTombs",
    "CnStatisticsVgarb",
    "CnStatisticsVlen",
    "Error",
    "ErrorOrigin",
    "Events",
    "EventsItem",
    "EventsItemLevel",
    "Mclass",
    "PerformanceCounter",
    "PerformanceCounterType",
    "PerformanceCounters",
    "PerformanceCountersItem",
    "PerformanceCountersItemCountersItem",
    "PerformanceCountersItemCountersItemFour",
    "PerformanceCountersItemCountersItemFourHistogramItem",
    "PerformanceCountersItemCountersItemOne",
    "PerformanceCountersItemCountersItemThree",
    "PerformanceCountersItemCountersItemTwo",
]
