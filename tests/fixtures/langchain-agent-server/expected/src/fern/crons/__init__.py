



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CronCreateConfig,
        CronCreateDurability,
        CronCreateInput,
        CronCreateInterruptAfter,
        CronCreateInterruptAfterZero,
        CronCreateInterruptBefore,
        CronCreateInterruptBeforeZero,
        CronCreateOnRunCompleted,
        CronCreateStreamMode,
        CronCreateStreamModeOne,
        CronCreateStreamModeZeroItem,
        CronPatchConfig,
        CronPatchDurability,
        CronPatchInput,
        CronPatchInterruptAfter,
        CronPatchInterruptAfterZero,
        CronPatchInterruptBefore,
        CronPatchInterruptBeforeZero,
        CronPatchOnRunCompleted,
        CronPatchStreamMode,
        CronPatchStreamModeOne,
        CronPatchStreamModeZeroItem,
        CronSearchSelectItem,
        CronSearchSortBy,
        CronSearchSortOrder,
        ThreadCronCreateConfig,
        ThreadCronCreateDurability,
        ThreadCronCreateInput,
        ThreadCronCreateInterruptAfter,
        ThreadCronCreateInterruptAfterZero,
        ThreadCronCreateInterruptBefore,
        ThreadCronCreateInterruptBeforeZero,
        ThreadCronCreateMultitaskStrategy,
        ThreadCronCreateStreamMode,
        ThreadCronCreateStreamModeOne,
        ThreadCronCreateStreamModeZeroItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CronCreateConfig": ".types",
    "CronCreateDurability": ".types",
    "CronCreateInput": ".types",
    "CronCreateInterruptAfter": ".types",
    "CronCreateInterruptAfterZero": ".types",
    "CronCreateInterruptBefore": ".types",
    "CronCreateInterruptBeforeZero": ".types",
    "CronCreateOnRunCompleted": ".types",
    "CronCreateStreamMode": ".types",
    "CronCreateStreamModeOne": ".types",
    "CronCreateStreamModeZeroItem": ".types",
    "CronPatchConfig": ".types",
    "CronPatchDurability": ".types",
    "CronPatchInput": ".types",
    "CronPatchInterruptAfter": ".types",
    "CronPatchInterruptAfterZero": ".types",
    "CronPatchInterruptBefore": ".types",
    "CronPatchInterruptBeforeZero": ".types",
    "CronPatchOnRunCompleted": ".types",
    "CronPatchStreamMode": ".types",
    "CronPatchStreamModeOne": ".types",
    "CronPatchStreamModeZeroItem": ".types",
    "CronSearchSelectItem": ".types",
    "CronSearchSortBy": ".types",
    "CronSearchSortOrder": ".types",
    "ThreadCronCreateConfig": ".types",
    "ThreadCronCreateDurability": ".types",
    "ThreadCronCreateInput": ".types",
    "ThreadCronCreateInterruptAfter": ".types",
    "ThreadCronCreateInterruptAfterZero": ".types",
    "ThreadCronCreateInterruptBefore": ".types",
    "ThreadCronCreateInterruptBeforeZero": ".types",
    "ThreadCronCreateMultitaskStrategy": ".types",
    "ThreadCronCreateStreamMode": ".types",
    "ThreadCronCreateStreamModeOne": ".types",
    "ThreadCronCreateStreamModeZeroItem": ".types",
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
    "CronCreateConfig",
    "CronCreateDurability",
    "CronCreateInput",
    "CronCreateInterruptAfter",
    "CronCreateInterruptAfterZero",
    "CronCreateInterruptBefore",
    "CronCreateInterruptBeforeZero",
    "CronCreateOnRunCompleted",
    "CronCreateStreamMode",
    "CronCreateStreamModeOne",
    "CronCreateStreamModeZeroItem",
    "CronPatchConfig",
    "CronPatchDurability",
    "CronPatchInput",
    "CronPatchInterruptAfter",
    "CronPatchInterruptAfterZero",
    "CronPatchInterruptBefore",
    "CronPatchInterruptBeforeZero",
    "CronPatchOnRunCompleted",
    "CronPatchStreamMode",
    "CronPatchStreamModeOne",
    "CronPatchStreamModeZeroItem",
    "CronSearchSelectItem",
    "CronSearchSortBy",
    "CronSearchSortOrder",
    "ThreadCronCreateConfig",
    "ThreadCronCreateDurability",
    "ThreadCronCreateInput",
    "ThreadCronCreateInterruptAfter",
    "ThreadCronCreateInterruptAfterZero",
    "ThreadCronCreateInterruptBefore",
    "ThreadCronCreateInterruptBeforeZero",
    "ThreadCronCreateMultitaskStrategy",
    "ThreadCronCreateStreamMode",
    "ThreadCronCreateStreamModeOne",
    "ThreadCronCreateStreamModeZeroItem",
]
