



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .four_hundred_four_not_found import FourHundredFourNotFound
    from .four_hundred_one_response import FourHundredOneResponse
    from .one_hundred_ten_crew import OneHundredTenCrew
    from .one_thousand_cone import OneThousandCone
    from .one_thousand_two_hundred_thirty_four_plan import OneThousandTwoHundredThirtyFourPlan
    from .seven_agent import SevenAgent
    from .three_d_kiln_model import ThreeDKilnModel
    from .twelve_hour_cycle import TwelveHourCycle
    from .twenty_one_club import TwentyOneClub
    from .two_fa_status import TwoFaStatus
    from .undefined_pixels import UndefinedPixels
    from .undefined_seats import UndefinedSeats
    from .undefined_viewers import UndefinedViewers
_dynamic_imports: typing.Dict[str, str] = {
    "FourHundredFourNotFound": ".four_hundred_four_not_found",
    "FourHundredOneResponse": ".four_hundred_one_response",
    "OneHundredTenCrew": ".one_hundred_ten_crew",
    "OneThousandCone": ".one_thousand_cone",
    "OneThousandTwoHundredThirtyFourPlan": ".one_thousand_two_hundred_thirty_four_plan",
    "SevenAgent": ".seven_agent",
    "ThreeDKilnModel": ".three_d_kiln_model",
    "TwelveHourCycle": ".twelve_hour_cycle",
    "TwentyOneClub": ".twenty_one_club",
    "TwoFaStatus": ".two_fa_status",
    "UndefinedPixels": ".undefined_pixels",
    "UndefinedSeats": ".undefined_seats",
    "UndefinedViewers": ".undefined_viewers",
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
    "FourHundredFourNotFound",
    "FourHundredOneResponse",
    "OneHundredTenCrew",
    "OneThousandCone",
    "OneThousandTwoHundredThirtyFourPlan",
    "SevenAgent",
    "ThreeDKilnModel",
    "TwelveHourCycle",
    "TwentyOneClub",
    "TwoFaStatus",
    "UndefinedPixels",
    "UndefinedSeats",
    "UndefinedViewers",
]
