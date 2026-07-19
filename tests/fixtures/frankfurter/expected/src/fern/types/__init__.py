



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .currency import Currency
    from .currency_detail import CurrencyDetail
    from .currency_detail_peg import CurrencyDetailPeg
    from .get_currencies_request_scope import GetCurrenciesRequestScope
    from .get_rates_request_expand import GetRatesRequestExpand
    from .get_rates_request_group import GetRatesRequestGroup
    from .not_found_error_body import NotFoundErrorBody
    from .provider import Provider
    from .provider_publish_cadence import ProviderPublishCadence
    from .rate import Rate
    from .rate_providers_item import RateProvidersItem
    from .unprocessable_entity_error_body import UnprocessableEntityErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "Currency": ".currency",
    "CurrencyDetail": ".currency_detail",
    "CurrencyDetailPeg": ".currency_detail_peg",
    "GetCurrenciesRequestScope": ".get_currencies_request_scope",
    "GetRatesRequestExpand": ".get_rates_request_expand",
    "GetRatesRequestGroup": ".get_rates_request_group",
    "NotFoundErrorBody": ".not_found_error_body",
    "Provider": ".provider",
    "ProviderPublishCadence": ".provider_publish_cadence",
    "Rate": ".rate",
    "RateProvidersItem": ".rate_providers_item",
    "UnprocessableEntityErrorBody": ".unprocessable_entity_error_body",
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
    "Currency",
    "CurrencyDetail",
    "CurrencyDetailPeg",
    "GetCurrenciesRequestScope",
    "GetRatesRequestExpand",
    "GetRatesRequestGroup",
    "NotFoundErrorBody",
    "Provider",
    "ProviderPublishCadence",
    "Rate",
    "RateProvidersItem",
    "UnprocessableEntityErrorBody",
]
