



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .harvest import Harvest
    from .harvest_board import HarvestBoard
    from .harvest_board_harvests import HarvestBoardHarvests
    from .harvest_board_harvests_ledger_version import HarvestBoardHarvestsLedgerVersion
    from .harvest_board_harvests_pending_reason import HarvestBoardHarvestsPendingReason
    from .harvest_board_harvests_tallied_at import HarvestBoardHarvestsTalliedAt
    from .harvest_board_zero import HarvestBoardZero
    from .harvest_board_zero_ledger_version import HarvestBoardZeroLedgerVersion
    from .harvest_board_zero_pending_reason import HarvestBoardZeroPendingReason
_dynamic_imports: typing.Dict[str, str] = {
    "Harvest": ".harvest",
    "HarvestBoard": ".harvest_board",
    "HarvestBoardHarvests": ".harvest_board_harvests",
    "HarvestBoardHarvestsLedgerVersion": ".harvest_board_harvests_ledger_version",
    "HarvestBoardHarvestsPendingReason": ".harvest_board_harvests_pending_reason",
    "HarvestBoardHarvestsTalliedAt": ".harvest_board_harvests_tallied_at",
    "HarvestBoardZero": ".harvest_board_zero",
    "HarvestBoardZeroLedgerVersion": ".harvest_board_zero_ledger_version",
    "HarvestBoardZeroPendingReason": ".harvest_board_zero_pending_reason",
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
    "Harvest",
    "HarvestBoard",
    "HarvestBoardHarvests",
    "HarvestBoardHarvestsLedgerVersion",
    "HarvestBoardHarvestsPendingReason",
    "HarvestBoardHarvestsTalliedAt",
    "HarvestBoardZero",
    "HarvestBoardZeroLedgerVersion",
    "HarvestBoardZeroPendingReason",
]
