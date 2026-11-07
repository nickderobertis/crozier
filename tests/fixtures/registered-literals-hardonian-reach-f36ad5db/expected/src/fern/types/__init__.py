



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .capsule import Capsule
    from .capsule_manifest import CapsuleManifest
    from .event import Event
    from .events_response import EventsResponse
    from .federation_node import FederationNode
    from .federation_node_status import FederationNodeStatus
    from .federation_status import FederationStatus
    from .health_response import HealthResponse
    from .health_response_status import HealthResponseStatus
    from .install_pack_response import InstallPackResponse
    from .pack import Pack
    from .pack_reproducibility import PackReproducibility
    from .packs_response import PacksResponse
    from .reach_error import ReachError
    from .replay_response import ReplayResponse
    from .run import Run
    from .run_status import RunStatus
    from .run_tier import RunTier
    from .verification_result import VerificationResult
    from .version_response import VersionResponse
    from .version_response_compatibility_policy import VersionResponseCompatibilityPolicy
_dynamic_imports: typing.Dict[str, str] = {
    "Capsule": ".capsule",
    "CapsuleManifest": ".capsule_manifest",
    "Event": ".event",
    "EventsResponse": ".events_response",
    "FederationNode": ".federation_node",
    "FederationNodeStatus": ".federation_node_status",
    "FederationStatus": ".federation_status",
    "HealthResponse": ".health_response",
    "HealthResponseStatus": ".health_response_status",
    "InstallPackResponse": ".install_pack_response",
    "Pack": ".pack",
    "PackReproducibility": ".pack_reproducibility",
    "PacksResponse": ".packs_response",
    "ReachError": ".reach_error",
    "ReplayResponse": ".replay_response",
    "Run": ".run",
    "RunStatus": ".run_status",
    "RunTier": ".run_tier",
    "VerificationResult": ".verification_result",
    "VersionResponse": ".version_response",
    "VersionResponseCompatibilityPolicy": ".version_response_compatibility_policy",
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
    "Capsule",
    "CapsuleManifest",
    "Event",
    "EventsResponse",
    "FederationNode",
    "FederationNodeStatus",
    "FederationStatus",
    "HealthResponse",
    "HealthResponseStatus",
    "InstallPackResponse",
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
]
