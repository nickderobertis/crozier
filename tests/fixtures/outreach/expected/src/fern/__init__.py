



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Account,
        AccountAttributes,
        AccountListResponse,
        AccountListResponseLinks,
        AccountListResponseMeta,
        AccountResponse,
        ErrorResponse,
        ErrorResponseErrorsItem,
        ErrorResponseErrorsItemSource,
        JsonApiResource,
        JsonApiResourceLinks,
        Prospect,
        ProspectAttributes,
        ProspectListResponse,
        ProspectResponse,
        SequenceListResponse,
        SequenceResponse,
        SequenceResponseData,
    )
    from .errors import BadRequestError, UnauthorizedError
    from . import (
        accounts,
        prospects,
        rulesets,
        sequence_states,
        sequence_steps,
        sequence_templates,
        sequences,
        snippets,
        templates,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .accounts import (
        AccountCreateRequestData,
        AccountCreateRequestDataAttributes,
        AccountUpdateRequestData,
        AccountUpdateRequestDataAttributes,
    )
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .prospects import ProspectCreateRequestData, ProspectCreateRequestDataAttributes, ProspectUpdateRequestData
    from .rulesets import RulesetCreateRequestData
    from .sequence_states import SequenceStateCreateRequestData
    from .sequence_steps import SequenceStepCreateRequestData
    from .sequence_templates import SequenceTemplateCreateRequestData
    from .sequences import SequenceCreateRequestData, SequenceCreateRequestDataAttributes
    from .snippets import SnippetCreateRequestData, SnippetCreateRequestDataAttributes
    from .templates import TemplateCreateRequestData, TemplateCreateRequestDataAttributes, TemplateUpdateRequestData
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".types",
    "AccountAttributes": ".types",
    "AccountCreateRequestData": ".accounts",
    "AccountCreateRequestDataAttributes": ".accounts",
    "AccountListResponse": ".types",
    "AccountListResponseLinks": ".types",
    "AccountListResponseMeta": ".types",
    "AccountResponse": ".types",
    "AccountUpdateRequestData": ".accounts",
    "AccountUpdateRequestDataAttributes": ".accounts",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "ErrorResponseErrorsItem": ".types",
    "ErrorResponseErrorsItemSource": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "JsonApiResource": ".types",
    "JsonApiResourceLinks": ".types",
    "Prospect": ".types",
    "ProspectAttributes": ".types",
    "ProspectCreateRequestData": ".prospects",
    "ProspectCreateRequestDataAttributes": ".prospects",
    "ProspectListResponse": ".types",
    "ProspectResponse": ".types",
    "ProspectUpdateRequestData": ".prospects",
    "RulesetCreateRequestData": ".rulesets",
    "SequenceCreateRequestData": ".sequences",
    "SequenceCreateRequestDataAttributes": ".sequences",
    "SequenceListResponse": ".types",
    "SequenceResponse": ".types",
    "SequenceResponseData": ".types",
    "SequenceStateCreateRequestData": ".sequence_states",
    "SequenceStepCreateRequestData": ".sequence_steps",
    "SequenceTemplateCreateRequestData": ".sequence_templates",
    "SnippetCreateRequestData": ".snippets",
    "SnippetCreateRequestDataAttributes": ".snippets",
    "TemplateCreateRequestData": ".templates",
    "TemplateCreateRequestDataAttributes": ".templates",
    "TemplateUpdateRequestData": ".templates",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "accounts": ".accounts",
    "prospects": ".prospects",
    "rulesets": ".rulesets",
    "sequence_states": ".sequence_states",
    "sequence_steps": ".sequence_steps",
    "sequence_templates": ".sequence_templates",
    "sequences": ".sequences",
    "snippets": ".snippets",
    "templates": ".templates",
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
    "Account",
    "AccountAttributes",
    "AccountCreateRequestData",
    "AccountCreateRequestDataAttributes",
    "AccountListResponse",
    "AccountListResponseLinks",
    "AccountListResponseMeta",
    "AccountResponse",
    "AccountUpdateRequestData",
    "AccountUpdateRequestDataAttributes",
    "AsyncFernApi",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "ErrorResponseErrorsItem",
    "ErrorResponseErrorsItemSource",
    "FernApi",
    "FernApiEnvironment",
    "JsonApiResource",
    "JsonApiResourceLinks",
    "Prospect",
    "ProspectAttributes",
    "ProspectCreateRequestData",
    "ProspectCreateRequestDataAttributes",
    "ProspectListResponse",
    "ProspectResponse",
    "ProspectUpdateRequestData",
    "RulesetCreateRequestData",
    "SequenceCreateRequestData",
    "SequenceCreateRequestDataAttributes",
    "SequenceListResponse",
    "SequenceResponse",
    "SequenceResponseData",
    "SequenceStateCreateRequestData",
    "SequenceStepCreateRequestData",
    "SequenceTemplateCreateRequestData",
    "SnippetCreateRequestData",
    "SnippetCreateRequestDataAttributes",
    "TemplateCreateRequestData",
    "TemplateCreateRequestDataAttributes",
    "TemplateUpdateRequestData",
    "UnauthorizedError",
    "__version__",
    "accounts",
    "prospects",
    "rulesets",
    "sequence_states",
    "sequence_steps",
    "sequence_templates",
    "sequences",
    "snippets",
    "templates",
]
