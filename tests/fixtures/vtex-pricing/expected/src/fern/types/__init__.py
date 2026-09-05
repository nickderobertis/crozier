



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .date_range import DateRange
    from .fixed_price import FixedPrice
    from .getcomputedprice import Getcomputedprice
    from .getprice import Getprice
    from .pricing_configuration import PricingConfiguration
    from .pricing_configuration_price_variation import PricingConfigurationPriceVariation
    from .pricing_configuration_trade_policy_configs_item import PricingConfigurationTradePolicyConfigsItem
_dynamic_imports: typing.Dict[str, str] = {
    "DateRange": ".date_range",
    "FixedPrice": ".fixed_price",
    "Getcomputedprice": ".getcomputedprice",
    "Getprice": ".getprice",
    "PricingConfiguration": ".pricing_configuration",
    "PricingConfigurationPriceVariation": ".pricing_configuration_price_variation",
    "PricingConfigurationTradePolicyConfigsItem": ".pricing_configuration_trade_policy_configs_item",
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
    "DateRange",
    "FixedPrice",
    "Getcomputedprice",
    "Getprice",
    "PricingConfiguration",
    "PricingConfigurationPriceVariation",
    "PricingConfigurationTradePolicyConfigsItem",
]
