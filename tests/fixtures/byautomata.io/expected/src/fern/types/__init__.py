



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .article import Article
    from .content_pro_company import ContentProCompany
    from .content_pro_snippets import ContentProSnippets
    from .input_company import InputCompany
    from .similar_company import SimilarCompany
    from .similar_company_search import SimilarCompanySearch
    from .snippet import Snippet
_dynamic_imports: typing.Dict[str, str] = {
    "Article": ".article",
    "ContentProCompany": ".content_pro_company",
    "ContentProSnippets": ".content_pro_snippets",
    "InputCompany": ".input_company",
    "SimilarCompany": ".similar_company",
    "SimilarCompanySearch": ".similar_company_search",
    "Snippet": ".snippet",
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
    "Article",
    "ContentProCompany",
    "ContentProSnippets",
    "InputCompany",
    "SimilarCompany",
    "SimilarCompanySearch",
    "Snippet",
]
