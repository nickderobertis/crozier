



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .collection import Collection
    from .collection_list import CollectionList
    from .continent import Continent
    from .continent_list import ContinentList
    from .country import Country
    from .country_list import CountryList
    from .currency import Currency
    from .currency_list import CurrencyList
    from .document import Document
    from .document_list import DocumentList
    from .error import Error
    from .execution import Execution
    from .execution_list import ExecutionList
    from .file import File
    from .file_list import FileList
    from .function import Function
    from .function_list import FunctionList
    from .language import Language
    from .language_list import LanguageList
    from .locale import Locale
    from .log import Log
    from .log_list import LogList
    from .membership import Membership
    from .membership_list import MembershipList
    from .permissions import Permissions
    from .phone import Phone
    from .phone_list import PhoneList
    from .preferences import Preferences
    from .rule import Rule
    from .session import Session
    from .session_list import SessionList
    from .tag import Tag
    from .tag_list import TagList
    from .team import Team
    from .team_list import TeamList
    from .token import Token
    from .user import User
    from .user_list import UserList
_dynamic_imports: typing.Dict[str, str] = {
    "Collection": ".collection",
    "CollectionList": ".collection_list",
    "Continent": ".continent",
    "ContinentList": ".continent_list",
    "Country": ".country",
    "CountryList": ".country_list",
    "Currency": ".currency",
    "CurrencyList": ".currency_list",
    "Document": ".document",
    "DocumentList": ".document_list",
    "Error": ".error",
    "Execution": ".execution",
    "ExecutionList": ".execution_list",
    "File": ".file",
    "FileList": ".file_list",
    "Function": ".function",
    "FunctionList": ".function_list",
    "Language": ".language",
    "LanguageList": ".language_list",
    "Locale": ".locale",
    "Log": ".log",
    "LogList": ".log_list",
    "Membership": ".membership",
    "MembershipList": ".membership_list",
    "Permissions": ".permissions",
    "Phone": ".phone",
    "PhoneList": ".phone_list",
    "Preferences": ".preferences",
    "Rule": ".rule",
    "Session": ".session",
    "SessionList": ".session_list",
    "Tag": ".tag",
    "TagList": ".tag_list",
    "Team": ".team",
    "TeamList": ".team_list",
    "Token": ".token",
    "User": ".user",
    "UserList": ".user_list",
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
    "File",
    "FileList",
    "Function",
    "FunctionList",
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
]
