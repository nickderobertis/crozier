



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .getallpricetablesandrules_response_item import GetallpricetablesandrulesResponseItem
    from .getallpricetablesandrules_response_item_rules_item import GetallpricetablesandrulesResponseItemRulesItem
    from .getallpricetablesandrules_response_item_rules_item_context import (
        GetallpricetablesandrulesResponseItemRulesItemContext,
    )
    from .getallpricetablesandrules_response_item_rules_item_context_date_range import (
        GetallpricetablesandrulesResponseItemRulesItemContextDateRange,
    )
    from .getallpricetablesandrules_response_item_rules_item_context_markup_range import (
        GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange,
    )
    from .getrulesforapricetable_response import GetrulesforapricetableResponse
    from .getrulesforapricetable_response_rules_item import GetrulesforapricetableResponseRulesItem
    from .getrulesforapricetable_response_rules_item_context import GetrulesforapricetableResponseRulesItemContext
    from .getrulesforapricetable_response_rules_item_context_date_range import (
        GetrulesforapricetableResponseRulesItemContextDateRange,
    )
    from .getrulesforapricetable_response_rules_item_context_markup_range import (
        GetrulesforapricetableResponseRulesItemContextMarkupRange,
    )
    from .put_pricing_pipeline_catalog_price_table_id_request_rules_item import (
        PutPricingPipelineCatalogPriceTableIdRequestRulesItem,
    )
    from .put_pricing_pipeline_catalog_price_table_id_request_rules_item_context import (
        PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext,
    )
    from .put_pricing_pipeline_catalog_price_table_id_request_rules_item_context_date_range import (
        PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange,
    )
    from .put_pricing_pipeline_catalog_price_table_id_request_rules_item_context_markup_range import (
        PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetallpricetablesandrulesResponseItem": ".getallpricetablesandrules_response_item",
    "GetallpricetablesandrulesResponseItemRulesItem": ".getallpricetablesandrules_response_item_rules_item",
    "GetallpricetablesandrulesResponseItemRulesItemContext": ".getallpricetablesandrules_response_item_rules_item_context",
    "GetallpricetablesandrulesResponseItemRulesItemContextDateRange": ".getallpricetablesandrules_response_item_rules_item_context_date_range",
    "GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange": ".getallpricetablesandrules_response_item_rules_item_context_markup_range",
    "GetrulesforapricetableResponse": ".getrulesforapricetable_response",
    "GetrulesforapricetableResponseRulesItem": ".getrulesforapricetable_response_rules_item",
    "GetrulesforapricetableResponseRulesItemContext": ".getrulesforapricetable_response_rules_item_context",
    "GetrulesforapricetableResponseRulesItemContextDateRange": ".getrulesforapricetable_response_rules_item_context_date_range",
    "GetrulesforapricetableResponseRulesItemContextMarkupRange": ".getrulesforapricetable_response_rules_item_context_markup_range",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItem": ".put_pricing_pipeline_catalog_price_table_id_request_rules_item",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext": ".put_pricing_pipeline_catalog_price_table_id_request_rules_item_context",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange": ".put_pricing_pipeline_catalog_price_table_id_request_rules_item_context_date_range",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange": ".put_pricing_pipeline_catalog_price_table_id_request_rules_item_context_markup_range",
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
    "GetallpricetablesandrulesResponseItem",
    "GetallpricetablesandrulesResponseItemRulesItem",
    "GetallpricetablesandrulesResponseItemRulesItemContext",
    "GetallpricetablesandrulesResponseItemRulesItemContextDateRange",
    "GetallpricetablesandrulesResponseItemRulesItemContextMarkupRange",
    "GetrulesforapricetableResponse",
    "GetrulesforapricetableResponseRulesItem",
    "GetrulesforapricetableResponseRulesItemContext",
    "GetrulesforapricetableResponseRulesItemContextDateRange",
    "GetrulesforapricetableResponseRulesItemContextMarkupRange",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItem",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContext",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextDateRange",
    "PutPricingPipelineCatalogPriceTableIdRequestRulesItemContextMarkupRange",
]
