



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .author import Author, Author_Autopilot, Author_Contractor, Author_Crew, Author_Harbour
    from .author_autopilot import AuthorAutopilot
    from .author_harbour import AuthorHarbour
    from .contractor import Contractor
    from .crew_member import CrewMember
    from .entry import Entry
_dynamic_imports: typing.Dict[str, str] = {
    "Author": ".author",
    "AuthorAutopilot": ".author_autopilot",
    "AuthorHarbour": ".author_harbour",
    "Author_Autopilot": ".author",
    "Author_Contractor": ".author",
    "Author_Crew": ".author",
    "Author_Harbour": ".author",
    "Contractor": ".contractor",
    "CrewMember": ".crew_member",
    "Entry": ".entry",
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
    "Author",
    "AuthorAutopilot",
    "AuthorHarbour",
    "Author_Autopilot",
    "Author_Contractor",
    "Author_Crew",
    "Author_Harbour",
    "Contractor",
    "CrewMember",
    "Entry",
]
