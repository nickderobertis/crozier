



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        FourHundredFourNotFound,
        FourHundredOneResponse,
        NineThousandNineHundredNinetyNineStock,
        OneHundredTenCrew,
        OneThousandCone,
        OneThousandTwoHundredThirtyFourPlan,
        SevenAgent,
        ThreeDKilnModel,
        TwelveHourCycle,
        TwentyOneClub,
        TwoFaStatus,
        UndefinedBricks,
        UndefinedPixels,
        UndefinedSeats,
        UndefinedSteps,
        UndefinedViewers,
    )
    from .errors import NotFoundError, UnauthorizedError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FourHundredFourNotFound": ".types",
    "FourHundredOneResponse": ".types",
    "NineThousandNineHundredNinetyNineStock": ".types",
    "NotFoundError": ".errors",
    "OneHundredTenCrew": ".types",
    "OneThousandCone": ".types",
    "OneThousandTwoHundredThirtyFourPlan": ".types",
    "SevenAgent": ".types",
    "ThreeDKilnModel": ".types",
    "TwelveHourCycle": ".types",
    "TwentyOneClub": ".types",
    "TwoFaStatus": ".types",
    "UnauthorizedError": ".errors",
    "UndefinedBricks": ".types",
    "UndefinedPixels": ".types",
    "UndefinedSeats": ".types",
    "UndefinedSteps": ".types",
    "UndefinedViewers": ".types",
    "__version__": ".version",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FourHundredFourNotFound",
    "FourHundredOneResponse",
    "NineThousandNineHundredNinetyNineStock",
    "NotFoundError",
    "OneHundredTenCrew",
    "OneThousandCone",
    "OneThousandTwoHundredThirtyFourPlan",
    "SevenAgent",
    "ThreeDKilnModel",
    "TwelveHourCycle",
    "TwentyOneClub",
    "TwoFaStatus",
    "UnauthorizedError",
    "UndefinedBricks",
    "UndefinedPixels",
    "UndefinedSeats",
    "UndefinedSteps",
    "UndefinedViewers",
    "__version__",
]
