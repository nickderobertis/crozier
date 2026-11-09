



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .all_courts_pacer_case_locator_case_search_request_case_status import (
        AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
    )
    from .all_courts_pacer_case_locator_party_search_request_case_status import (
        AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
    )
    from .appeal_courts_pacer_case_locator_case_search_request_case_status import (
        AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
    )
    from .appeal_courts_pacer_case_locator_party_search_request_case_status import (
        AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
    )
    from .bankruptcy_courts_pacer_case_locator_case_search_request_case_status import (
        BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
    )
    from .bankruptcy_courts_pacer_case_locator_party_search_request_case_status import (
        BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
    )
    from .civil_courts_pacer_case_locator_case_search_request_case_status import (
        CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
    )
    from .civil_courts_pacer_case_locator_party_search_request_case_status import (
        CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
    )
    from .criminal_courts_pacer_case_locator_case_search_request_case_status import (
        CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
    )
    from .criminal_courts_pacer_case_locator_party_search_request_case_status import (
        CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
    )
    from .multi_district_courts_pacer_case_locator_case_search_request_case_status import (
        MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
    )
    from .multi_district_courts_pacer_case_locator_party_search_request_case_status import (
        MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus": ".all_courts_pacer_case_locator_case_search_request_case_status",
    "AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus": ".all_courts_pacer_case_locator_party_search_request_case_status",
    "AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus": ".appeal_courts_pacer_case_locator_case_search_request_case_status",
    "AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus": ".appeal_courts_pacer_case_locator_party_search_request_case_status",
    "BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus": ".bankruptcy_courts_pacer_case_locator_case_search_request_case_status",
    "BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus": ".bankruptcy_courts_pacer_case_locator_party_search_request_case_status",
    "CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus": ".civil_courts_pacer_case_locator_case_search_request_case_status",
    "CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus": ".civil_courts_pacer_case_locator_party_search_request_case_status",
    "CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus": ".criminal_courts_pacer_case_locator_case_search_request_case_status",
    "CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus": ".criminal_courts_pacer_case_locator_party_search_request_case_status",
    "MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus": ".multi_district_courts_pacer_case_locator_case_search_request_case_status",
    "MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus": ".multi_district_courts_pacer_case_locator_party_search_request_case_status",
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
    "AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus",
    "AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus",
    "AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus",
    "AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus",
    "BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus",
    "BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus",
    "CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus",
    "CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus",
    "CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus",
    "CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus",
    "MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus",
    "MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus",
]
