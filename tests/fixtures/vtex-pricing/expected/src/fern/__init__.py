



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DateRange,
        FixedPrice,
        Getcomputedprice,
        Getprice,
        PricingConfiguration,
        PricingConfigurationPriceVariation,
        PricingConfigurationTradePolicyConfigsItem,
    )
    from .errors import ForbiddenError, TooManyRequestsError, UnauthorizedError
    from . import price_tables, prices_and_fixed_prices, pricing_configuration
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .price_tables import (
        GetallpricetablesandrulesResponseItem,
        GetallpricetablesandrulesResponseItemRulesItem,
        GetallpricetablesandrulesResponseItemRulesItemContext,
        GetallpricetablesandrulesResponseItemRulesItemContextDateRange,
        GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange,
        GetrulesforapricetableResponse,
        GetrulesforapricetableResponseRulesItem,
        GetrulesforapricetableResponseRulesItemContext,
        GetrulesforapricetableResponseRulesItemContextDateRange,
        GetrulesforapricetableResponseRulesItemContextMarkupRange,
        PutPricingPipelineCatalogPriceTableIdRequestRulesItem,
        PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext,
        PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange,
        PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange,
    )
    from .prices_and_fixed_prices import (
        CreateUpdatePriceOrFixedPriceRequestFixedPricesItem,
        CreateUpdatePriceOrFixedPriceRequestFixedPricesItemDateRange,
        CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem,
        CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItemDateRange,
    )
    from .pricing_configuration import GetPricingv2StatusResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CreateUpdatePriceOrFixedPriceRequestFixedPricesItem": ".prices_and_fixed_prices",
    "CreateUpdatePriceOrFixedPriceRequestFixedPricesItemDateRange": ".prices_and_fixed_prices",
    "CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem": ".prices_and_fixed_prices",
    "CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItemDateRange": ".prices_and_fixed_prices",
    "DateRange": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FixedPrice": ".types",
    "ForbiddenError": ".errors",
    "GetPricingv2StatusResponse": ".pricing_configuration",
    "GetallpricetablesandrulesResponseItem": ".price_tables",
    "GetallpricetablesandrulesResponseItemRulesItem": ".price_tables",
    "GetallpricetablesandrulesResponseItemRulesItemContext": ".price_tables",
    "GetallpricetablesandrulesResponseItemRulesItemContextDateRange": ".price_tables",
    "GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange": ".price_tables",
    "Getcomputedprice": ".types",
    "Getprice": ".types",
    "GetrulesforapricetableResponse": ".price_tables",
    "GetrulesforapricetableResponseRulesItem": ".price_tables",
    "GetrulesforapricetableResponseRulesItemContext": ".price_tables",
    "GetrulesforapricetableResponseRulesItemContextDateRange": ".price_tables",
    "GetrulesforapricetableResponseRulesItemContextMarkupRange": ".price_tables",
    "PricingConfiguration": ".types",
    "PricingConfigurationPriceVariation": ".types",
    "PricingConfigurationTradePolicyConfigsItem": ".types",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItem": ".price_tables",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext": ".price_tables",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange": ".price_tables",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange": ".price_tables",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "price_tables": ".price_tables",
    "prices_and_fixed_prices": ".prices_and_fixed_prices",
    "pricing_configuration": ".pricing_configuration",
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
    "CreateUpdatePriceOrFixedPriceRequestFixedPricesItem",
    "CreateUpdatePriceOrFixedPriceRequestFixedPricesItemDateRange",
    "CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem",
    "CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItemDateRange",
    "DateRange",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "FixedPrice",
    "ForbiddenError",
    "GetPricingv2StatusResponse",
    "GetallpricetablesandrulesResponseItem",
    "GetallpricetablesandrulesResponseItemRulesItem",
    "GetallpricetablesandrulesResponseItemRulesItemContext",
    "GetallpricetablesandrulesResponseItemRulesItemContextDateRange",
    "GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange",
    "Getcomputedprice",
    "Getprice",
    "GetrulesforapricetableResponse",
    "GetrulesforapricetableResponseRulesItem",
    "GetrulesforapricetableResponseRulesItemContext",
    "GetrulesforapricetableResponseRulesItemContextDateRange",
    "GetrulesforapricetableResponseRulesItemContextMarkupRange",
    "PricingConfiguration",
    "PricingConfigurationPriceVariation",
    "PricingConfigurationTradePolicyConfigsItem",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItem",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange",
    "TooManyRequestsError",
    "UnauthorizedError",
    "__version__",
    "price_tables",
    "prices_and_fixed_prices",
    "pricing_configuration",
]
