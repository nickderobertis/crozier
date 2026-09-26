



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_withdrawal_tracker_v3request_ems_student_status import GetWithdrawalTrackerV3RequestEmsStudentStatus
    from .get_withdrawal_tracker_v3request_sort_by import GetWithdrawalTrackerV3RequestSortBy
    from .get_withdrawal_tracker_v3request_withdrawal_date_filter import (
        GetWithdrawalTrackerV3RequestWithdrawalDateFilter,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetWithdrawalTrackerV3RequestEmsStudentStatus": ".get_withdrawal_tracker_v3request_ems_student_status",
    "GetWithdrawalTrackerV3RequestSortBy": ".get_withdrawal_tracker_v3request_sort_by",
    "GetWithdrawalTrackerV3RequestWithdrawalDateFilter": ".get_withdrawal_tracker_v3request_withdrawal_date_filter",
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
    "GetWithdrawalTrackerV3RequestEmsStudentStatus",
    "GetWithdrawalTrackerV3RequestSortBy",
    "GetWithdrawalTrackerV3RequestWithdrawalDateFilter",
]
