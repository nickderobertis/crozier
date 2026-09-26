



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CnStatistics,
        CnStatisticsHlen,
        CnStatisticsKeys,
        CnStatisticsKlen,
        CnStatisticsPtombs,
        CnStatisticsTombs,
        CnStatisticsVgarb,
        CnStatisticsVlen,
        Error,
        ErrorOrigin,
        Events,
        EventsItem,
        EventsItemLevel,
        Mclass,
        PerformanceCounter,
        PerformanceCounterType,
        PerformanceCounters,
        PerformanceCountersItem,
        PerformanceCountersItemCountersItem,
        PerformanceCountersItemCountersItemFour,
        PerformanceCountersItemCountersItemFourHistogramItem,
        PerformanceCountersItemCountersItemOne,
        PerformanceCountersItemCountersItemThree,
        PerformanceCountersItemCountersItemTwo,
    )
    from .errors import BadRequestError, LockedError, NotFoundError
    from . import global_, kvdb, kvs
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .global_ import (
        KmcVmstatGetResponseItem,
        ParamGetResponse,
        ParamSetRequestBody,
        ParamsGetResponse,
        WorkqueuesGetResponseItem,
        WorkqueuesGetResponseItemState,
    )
    from .kvdb import (
        KvdbCompactStatusGetResponse,
        KvdbCschedGetResponseItem,
        KvdbMediaClassGetResponse,
        KvdbParamGetResponse,
        KvdbParamSetRequestBody,
        KvdbParamsGetResponse,
    )
    from .kvs import (
        KvsCnTreeGetResponse,
        KvsCnTreeGetResponseNodesItem,
        KvsCnTreeGetResponseNodesItemKvsets,
        KvsCnTreeGetResponseNodesItemKvsetsOneItem,
        KvsCnTreeGetResponseNodesItemKvsetsOneItemJob,
        KvsParamGetResponse,
        KvsParamSetRequestBody,
        KvsParamsGetResponse,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CnStatistics": ".types",
    "CnStatisticsHlen": ".types",
    "CnStatisticsKeys": ".types",
    "CnStatisticsKlen": ".types",
    "CnStatisticsPtombs": ".types",
    "CnStatisticsTombs": ".types",
    "CnStatisticsVgarb": ".types",
    "CnStatisticsVlen": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "ErrorOrigin": ".types",
    "Events": ".types",
    "EventsItem": ".types",
    "EventsItemLevel": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "KmcVmstatGetResponseItem": ".global_",
    "KvdbCompactStatusGetResponse": ".kvdb",
    "KvdbCschedGetResponseItem": ".kvdb",
    "KvdbMediaClassGetResponse": ".kvdb",
    "KvdbParamGetResponse": ".kvdb",
    "KvdbParamSetRequestBody": ".kvdb",
    "KvdbParamsGetResponse": ".kvdb",
    "KvsCnTreeGetResponse": ".kvs",
    "KvsCnTreeGetResponseNodesItem": ".kvs",
    "KvsCnTreeGetResponseNodesItemKvsets": ".kvs",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItem": ".kvs",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItemJob": ".kvs",
    "KvsParamGetResponse": ".kvs",
    "KvsParamSetRequestBody": ".kvs",
    "KvsParamsGetResponse": ".kvs",
    "LockedError": ".errors",
    "Mclass": ".types",
    "NotFoundError": ".errors",
    "ParamGetResponse": ".global_",
    "ParamSetRequestBody": ".global_",
    "ParamsGetResponse": ".global_",
    "PerformanceCounter": ".types",
    "PerformanceCounterType": ".types",
    "PerformanceCounters": ".types",
    "PerformanceCountersItem": ".types",
    "PerformanceCountersItemCountersItem": ".types",
    "PerformanceCountersItemCountersItemFour": ".types",
    "PerformanceCountersItemCountersItemFourHistogramItem": ".types",
    "PerformanceCountersItemCountersItemOne": ".types",
    "PerformanceCountersItemCountersItemThree": ".types",
    "PerformanceCountersItemCountersItemTwo": ".types",
    "WorkqueuesGetResponseItem": ".global_",
    "WorkqueuesGetResponseItemState": ".global_",
    "__version__": ".version",
    "global_": ".global_",
    "kvdb": ".kvdb",
    "kvs": ".kvs",
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
    "AsyncFernApi",
    "BadRequestError",
    "CnStatistics",
    "CnStatisticsHlen",
    "CnStatisticsKeys",
    "CnStatisticsKlen",
    "CnStatisticsPtombs",
    "CnStatisticsTombs",
    "CnStatisticsVgarb",
    "CnStatisticsVlen",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "ErrorOrigin",
    "Events",
    "EventsItem",
    "EventsItemLevel",
    "FernApi",
    "FernApiEnvironment",
    "KmcVmstatGetResponseItem",
    "KvdbCompactStatusGetResponse",
    "KvdbCschedGetResponseItem",
    "KvdbMediaClassGetResponse",
    "KvdbParamGetResponse",
    "KvdbParamSetRequestBody",
    "KvdbParamsGetResponse",
    "KvsCnTreeGetResponse",
    "KvsCnTreeGetResponseNodesItem",
    "KvsCnTreeGetResponseNodesItemKvsets",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItem",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItemJob",
    "KvsParamGetResponse",
    "KvsParamSetRequestBody",
    "KvsParamsGetResponse",
    "LockedError",
    "Mclass",
    "NotFoundError",
    "ParamGetResponse",
    "ParamSetRequestBody",
    "ParamsGetResponse",
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
    "WorkqueuesGetResponseItem",
    "WorkqueuesGetResponseItemState",
    "__version__",
    "global_",
    "kvdb",
    "kvs",
]
