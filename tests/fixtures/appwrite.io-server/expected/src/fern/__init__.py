



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Collection,
        CollectionList,
        Continent,
        ContinentList,
        Country,
        CountryList,
        Currency,
        CurrencyList,
        Document,
        DocumentList,
        Error,
        Execution,
        ExecutionList,
        File,
        FileList,
        Function,
        FunctionList,
        Language,
        LanguageList,
        Locale,
        Log,
        LogList,
        Membership,
        MembershipList,
        Permissions,
        Phone,
        PhoneList,
        Preferences,
        Rule,
        Session,
        SessionList,
        Tag,
        TagList,
        Team,
        TeamList,
        Token,
        User,
        UserList,
    )
    from .errors import InternalServerError
    from . import account, avatars, database, functions, health, locale, storage, teams, users
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Collection": ".types",
    "CollectionList": ".types",
    "Continent": ".types",
    "ContinentList": ".types",
    "Country": ".types",
    "CountryList": ".types",
    "Currency": ".types",
    "CurrencyList": ".types",
    "Document": ".types",
    "DocumentList": ".types",
    "Error": ".types",
    "Execution": ".types",
    "ExecutionList": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "File": ".types",
    "FileList": ".types",
    "Function": ".types",
    "FunctionList": ".types",
    "InternalServerError": ".errors",
    "Language": ".types",
    "LanguageList": ".types",
    "Locale": ".types",
    "Log": ".types",
    "LogList": ".types",
    "Membership": ".types",
    "MembershipList": ".types",
    "Permissions": ".types",
    "Phone": ".types",
    "PhoneList": ".types",
    "Preferences": ".types",
    "Rule": ".types",
    "Session": ".types",
    "SessionList": ".types",
    "Tag": ".types",
    "TagList": ".types",
    "Team": ".types",
    "TeamList": ".types",
    "Token": ".types",
    "User": ".types",
    "UserList": ".types",
    "__version__": ".version",
    "account": ".account",
    "avatars": ".avatars",
    "database": ".database",
    "functions": ".functions",
    "health": ".health",
    "locale": ".locale",
    "storage": ".storage",
    "teams": ".teams",
    "users": ".users",
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
    "Collection",
    "CollectionList",
    "Continent",
    "ContinentList",
    "Country",
    "CountryList",
    "Currency",
    "CurrencyList",
    "Document",
    "DocumentList",
    "Error",
    "Execution",
    "ExecutionList",
    "FernApi",
    "FernApiEnvironment",
    "File",
    "FileList",
    "Function",
    "FunctionList",
    "InternalServerError",
    "Language",
    "LanguageList",
    "Locale",
    "Log",
    "LogList",
    "Membership",
    "MembershipList",
    "Permissions",
    "Phone",
    "PhoneList",
    "Preferences",
    "Rule",
    "Session",
    "SessionList",
    "Tag",
    "TagList",
    "Team",
    "TeamList",
    "Token",
    "User",
    "UserList",
    "__version__",
    "account",
    "avatars",
    "database",
    "functions",
    "health",
    "locale",
    "storage",
    "teams",
    "users",
]
