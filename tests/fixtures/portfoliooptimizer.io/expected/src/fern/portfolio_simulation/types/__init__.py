



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_portfolio_simulation_rebalancing_drift_weight_request_assets_item import (
        PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem,
    )
    from .post_portfolio_simulation_rebalancing_drift_weight_request_portfolios_item import (
        PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem,
    )
    from .post_portfolio_simulation_rebalancing_drift_weight_response import (
        PostPortfolioSimulationRebalancingDriftWeightResponse,
    )
    from .post_portfolio_simulation_rebalancing_drift_weight_response_portfolios_item import (
        PostPortfolioSimulationRebalancingDriftWeightResponsePortfoliosItem,
    )
    from .post_portfolio_simulation_rebalancing_fixed_weight_request_assets_item import (
        PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem,
    )
    from .post_portfolio_simulation_rebalancing_fixed_weight_request_portfolios_item import (
        PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem,
    )
    from .post_portfolio_simulation_rebalancing_fixed_weight_response import (
        PostPortfolioSimulationRebalancingFixedWeightResponse,
    )
    from .post_portfolio_simulation_rebalancing_fixed_weight_response_portfolios_item import (
        PostPortfolioSimulationRebalancingFixedWeightResponsePortfoliosItem,
    )
    from .post_portfolio_simulation_rebalancing_random_weight_request_assets_item import (
        PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem,
    )
    from .post_portfolio_simulation_rebalancing_random_weight_response import (
        PostPortfolioSimulationRebalancingRandomWeightResponse,
    )
    from .post_portfolio_simulation_rebalancing_random_weight_response_portfolios_item import (
        PostPortfolioSimulationRebalancingRandomWeightResponsePortfoliosItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem": ".post_portfolio_simulation_rebalancing_drift_weight_request_assets_item",
    "PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem": ".post_portfolio_simulation_rebalancing_drift_weight_request_portfolios_item",
    "PostPortfolioSimulationRebalancingDriftWeightResponse": ".post_portfolio_simulation_rebalancing_drift_weight_response",
    "PostPortfolioSimulationRebalancingDriftWeightResponsePortfoliosItem": ".post_portfolio_simulation_rebalancing_drift_weight_response_portfolios_item",
    "PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem": ".post_portfolio_simulation_rebalancing_fixed_weight_request_assets_item",
    "PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem": ".post_portfolio_simulation_rebalancing_fixed_weight_request_portfolios_item",
    "PostPortfolioSimulationRebalancingFixedWeightResponse": ".post_portfolio_simulation_rebalancing_fixed_weight_response",
    "PostPortfolioSimulationRebalancingFixedWeightResponsePortfoliosItem": ".post_portfolio_simulation_rebalancing_fixed_weight_response_portfolios_item",
    "PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem": ".post_portfolio_simulation_rebalancing_random_weight_request_assets_item",
    "PostPortfolioSimulationRebalancingRandomWeightResponse": ".post_portfolio_simulation_rebalancing_random_weight_response",
    "PostPortfolioSimulationRebalancingRandomWeightResponsePortfoliosItem": ".post_portfolio_simulation_rebalancing_random_weight_response_portfolios_item",
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
    "PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem",
    "PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem",
    "PostPortfolioSimulationRebalancingDriftWeightResponse",
    "PostPortfolioSimulationRebalancingDriftWeightResponsePortfoliosItem",
    "PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem",
    "PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem",
    "PostPortfolioSimulationRebalancingFixedWeightResponse",
    "PostPortfolioSimulationRebalancingFixedWeightResponsePortfoliosItem",
    "PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem",
    "PostPortfolioSimulationRebalancingRandomWeightResponse",
    "PostPortfolioSimulationRebalancingRandomWeightResponsePortfoliosItem",
]
