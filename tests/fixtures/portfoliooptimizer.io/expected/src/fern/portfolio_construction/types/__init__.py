



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_portfolio_construction_investable_response import PostPortfolioConstructionInvestableResponse
    from .post_portfolio_construction_mimicking_request_assets_item import (
        PostPortfolioConstructionMimickingRequestAssetsItem,
    )
    from .post_portfolio_construction_mimicking_request_constraints import (
        PostPortfolioConstructionMimickingRequestConstraints,
    )
    from .post_portfolio_construction_mimicking_response import PostPortfolioConstructionMimickingResponse
    from .post_portfolio_construction_random_request_constraints import (
        PostPortfolioConstructionRandomRequestConstraints,
    )
    from .post_portfolio_construction_random_response import PostPortfolioConstructionRandomResponse
    from .post_portfolio_construction_random_response_portfolios_item import (
        PostPortfolioConstructionRandomResponsePortfoliosItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioConstructionInvestableResponse": ".post_portfolio_construction_investable_response",
    "PostPortfolioConstructionMimickingRequestAssetsItem": ".post_portfolio_construction_mimicking_request_assets_item",
    "PostPortfolioConstructionMimickingRequestConstraints": ".post_portfolio_construction_mimicking_request_constraints",
    "PostPortfolioConstructionMimickingResponse": ".post_portfolio_construction_mimicking_response",
    "PostPortfolioConstructionRandomRequestConstraints": ".post_portfolio_construction_random_request_constraints",
    "PostPortfolioConstructionRandomResponse": ".post_portfolio_construction_random_response",
    "PostPortfolioConstructionRandomResponsePortfoliosItem": ".post_portfolio_construction_random_response_portfolios_item",
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
    "PostPortfolioConstructionInvestableResponse",
    "PostPortfolioConstructionMimickingRequestAssetsItem",
    "PostPortfolioConstructionMimickingRequestConstraints",
    "PostPortfolioConstructionMimickingResponse",
    "PostPortfolioConstructionRandomRequestConstraints",
    "PostPortfolioConstructionRandomResponse",
    "PostPortfolioConstructionRandomResponsePortfoliosItem",
]
