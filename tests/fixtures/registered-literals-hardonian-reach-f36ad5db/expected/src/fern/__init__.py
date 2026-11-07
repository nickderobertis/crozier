



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Capsule,
        CapsuleManifest,
        Event,
        EventsResponse,
        FederationNode,
        FederationNodeStatus,
        FederationStatus,
        HealthResponse,
        HealthResponseStatus,
        InstallPackResponse,
        Pack,
        PackReproducibility,
        PacksResponse,
        ReachError,
        ReplayResponse,
        Run,
        RunStatus,
        RunTier,
        VerificationResult,
        VersionResponse,
        VersionResponseCompatibilityPolicy,
    )
    from .errors import BadRequestError, InternalServerError, NotFoundError
    from . import capsules, federation, packs, runs, system
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .runs import CreateRunRequestPlanTier
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Capsule": ".types",
    "CapsuleManifest": ".types",
    "CreateRunRequestPlanTier": ".runs",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Event": ".types",
    "EventsResponse": ".types",
    "FederationNode": ".types",
    "FederationNodeStatus": ".types",
    "FederationStatus": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "HealthResponse": ".types",
    "HealthResponseStatus": ".types",
    "InstallPackResponse": ".types",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "Pack": ".types",
    "PackReproducibility": ".types",
    "PacksResponse": ".types",
    "ReachError": ".types",
    "ReplayResponse": ".types",
    "Run": ".types",
    "RunStatus": ".types",
    "RunTier": ".types",
    "VerificationResult": ".types",
    "VersionResponse": ".types",
    "VersionResponseCompatibilityPolicy": ".types",
    "__version__": ".version",
    "capsules": ".capsules",
    "federation": ".federation",
    "packs": ".packs",
    "runs": ".runs",
    "system": ".system",
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
    "Capsule",
    "CapsuleManifest",
    "CreateRunRequestPlanTier",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Event",
    "EventsResponse",
    "FederationNode",
    "FederationNodeStatus",
    "FederationStatus",
    "FernApi",
    "FernApiEnvironment",
    "HealthResponse",
    "HealthResponseStatus",
    "InstallPackResponse",
    "InternalServerError",
    "NotFoundError",
    "Pack",
    "PackReproducibility",
    "PacksResponse",
    "ReachError",
    "ReplayResponse",
    "Run",
    "RunStatus",
    "RunTier",
    "VerificationResult",
    "VersionResponse",
    "VersionResponseCompatibilityPolicy",
    "__version__",
    "capsules",
    "federation",
    "packs",
    "runs",
    "system",
]
