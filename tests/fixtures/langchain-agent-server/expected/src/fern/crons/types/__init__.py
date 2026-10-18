



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cron_create_config import CronCreateConfig
    from .cron_create_durability import CronCreateDurability
    from .cron_create_input import CronCreateInput
    from .cron_create_interrupt_after import CronCreateInterruptAfter
    from .cron_create_interrupt_after_zero import CronCreateInterruptAfterZero
    from .cron_create_interrupt_before import CronCreateInterruptBefore
    from .cron_create_interrupt_before_zero import CronCreateInterruptBeforeZero
    from .cron_create_on_run_completed import CronCreateOnRunCompleted
    from .cron_create_stream_mode import CronCreateStreamMode
    from .cron_create_stream_mode_one import CronCreateStreamModeOne
    from .cron_create_stream_mode_zero_item import CronCreateStreamModeZeroItem
    from .cron_patch_config import CronPatchConfig
    from .cron_patch_durability import CronPatchDurability
    from .cron_patch_input import CronPatchInput
    from .cron_patch_interrupt_after import CronPatchInterruptAfter
    from .cron_patch_interrupt_after_zero import CronPatchInterruptAfterZero
    from .cron_patch_interrupt_before import CronPatchInterruptBefore
    from .cron_patch_interrupt_before_zero import CronPatchInterruptBeforeZero
    from .cron_patch_on_run_completed import CronPatchOnRunCompleted
    from .cron_patch_stream_mode import CronPatchStreamMode
    from .cron_patch_stream_mode_one import CronPatchStreamModeOne
    from .cron_patch_stream_mode_zero_item import CronPatchStreamModeZeroItem
    from .cron_search_select_item import CronSearchSelectItem
    from .cron_search_sort_by import CronSearchSortBy
    from .cron_search_sort_order import CronSearchSortOrder
    from .thread_cron_create_config import ThreadCronCreateConfig
    from .thread_cron_create_durability import ThreadCronCreateDurability
    from .thread_cron_create_input import ThreadCronCreateInput
    from .thread_cron_create_interrupt_after import ThreadCronCreateInterruptAfter
    from .thread_cron_create_interrupt_after_zero import ThreadCronCreateInterruptAfterZero
    from .thread_cron_create_interrupt_before import ThreadCronCreateInterruptBefore
    from .thread_cron_create_interrupt_before_zero import ThreadCronCreateInterruptBeforeZero
    from .thread_cron_create_multitask_strategy import ThreadCronCreateMultitaskStrategy
    from .thread_cron_create_stream_mode import ThreadCronCreateStreamMode
    from .thread_cron_create_stream_mode_one import ThreadCronCreateStreamModeOne
    from .thread_cron_create_stream_mode_zero_item import ThreadCronCreateStreamModeZeroItem
_dynamic_imports: typing.Dict[str, str] = {
    "CronCreateConfig": ".cron_create_config",
    "CronCreateDurability": ".cron_create_durability",
    "CronCreateInput": ".cron_create_input",
    "CronCreateInterruptAfter": ".cron_create_interrupt_after",
    "CronCreateInterruptAfterZero": ".cron_create_interrupt_after_zero",
    "CronCreateInterruptBefore": ".cron_create_interrupt_before",
    "CronCreateInterruptBeforeZero": ".cron_create_interrupt_before_zero",
    "CronCreateOnRunCompleted": ".cron_create_on_run_completed",
    "CronCreateStreamMode": ".cron_create_stream_mode",
    "CronCreateStreamModeOne": ".cron_create_stream_mode_one",
    "CronCreateStreamModeZeroItem": ".cron_create_stream_mode_zero_item",
    "CronPatchConfig": ".cron_patch_config",
    "CronPatchDurability": ".cron_patch_durability",
    "CronPatchInput": ".cron_patch_input",
    "CronPatchInterruptAfter": ".cron_patch_interrupt_after",
    "CronPatchInterruptAfterZero": ".cron_patch_interrupt_after_zero",
    "CronPatchInterruptBefore": ".cron_patch_interrupt_before",
    "CronPatchInterruptBeforeZero": ".cron_patch_interrupt_before_zero",
    "CronPatchOnRunCompleted": ".cron_patch_on_run_completed",
    "CronPatchStreamMode": ".cron_patch_stream_mode",
    "CronPatchStreamModeOne": ".cron_patch_stream_mode_one",
    "CronPatchStreamModeZeroItem": ".cron_patch_stream_mode_zero_item",
    "CronSearchSelectItem": ".cron_search_select_item",
    "CronSearchSortBy": ".cron_search_sort_by",
    "CronSearchSortOrder": ".cron_search_sort_order",
    "ThreadCronCreateConfig": ".thread_cron_create_config",
    "ThreadCronCreateDurability": ".thread_cron_create_durability",
    "ThreadCronCreateInput": ".thread_cron_create_input",
    "ThreadCronCreateInterruptAfter": ".thread_cron_create_interrupt_after",
    "ThreadCronCreateInterruptAfterZero": ".thread_cron_create_interrupt_after_zero",
    "ThreadCronCreateInterruptBefore": ".thread_cron_create_interrupt_before",
    "ThreadCronCreateInterruptBeforeZero": ".thread_cron_create_interrupt_before_zero",
    "ThreadCronCreateMultitaskStrategy": ".thread_cron_create_multitask_strategy",
    "ThreadCronCreateStreamMode": ".thread_cron_create_stream_mode",
    "ThreadCronCreateStreamModeOne": ".thread_cron_create_stream_mode_one",
    "ThreadCronCreateStreamModeZeroItem": ".thread_cron_create_stream_mode_zero_item",
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
