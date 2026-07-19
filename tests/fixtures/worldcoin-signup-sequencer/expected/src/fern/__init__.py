



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CompressedSemaphoreProof,
        Error,
        FieldElement,
        G1,
        G2,
        Identity,
        InclusionProof,
        InclusionProofProofItem,
        InclusionProofProofItemLeft,
        InclusionProofProofItemRight,
        SemaphoreProof,
        SemaphoreProofVerificationResult,
    )
    from .errors import BadRequestError, ConflictError, GoneError, InternalServerError, NotFoundError
    from . import identities, semaphore_proof
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .identities import GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CompressedSemaphoreProof": ".types",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FieldElement": ".types",
    "G1": ".types",
    "G2": ".types",
    "GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType": ".identities",
    "GoneError": ".errors",
    "Identity": ".types",
    "InclusionProof": ".types",
    "InclusionProofProofItem": ".types",
    "InclusionProofProofItemLeft": ".types",
    "InclusionProofProofItemRight": ".types",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "SemaphoreProof": ".types",
    "SemaphoreProofVerificationResult": ".types",
    "__version__": ".version",
    "identities": ".identities",
    "semaphore_proof": ".semaphore_proof",
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
    "CompressedSemaphoreProof",
    "ConflictError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "FieldElement",
    "G1",
    "G2",
    "GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType",
    "GoneError",
    "Identity",
    "InclusionProof",
    "InclusionProofProofItem",
    "InclusionProofProofItemLeft",
    "InclusionProofProofItemRight",
    "InternalServerError",
    "NotFoundError",
    "SemaphoreProof",
    "SemaphoreProofVerificationResult",
    "__version__",
    "identities",
    "semaphore_proof",
]
