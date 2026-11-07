



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ai_classify_survey_request_language_strategy import AiClassifySurveyRequestLanguageStrategy
    from .ai_classify_survey_request_run_strategy import AiClassifySurveyRequestRunStrategy
    from .ai_classify_survey_response import AiClassifySurveyResponse
    from .ai_gateway_delete_response import AiGatewayDeleteResponse
    from .ai_gateway_info_response import AiGatewayInfoResponse
    from .ai_gateway_logs_response import AiGatewayLogsResponse
    from .ai_gateway_logs_response_items_item import AiGatewayLogsResponseItemsItem
    from .ai_gateway_logs_response_items_item_status import AiGatewayLogsResponseItemsItemStatus
    from .ai_gateway_model_pricing_response import AiGatewayModelPricingResponse
    from .ai_gateway_model_pricing_response_providers_item import AiGatewayModelPricingResponseProvidersItem
    from .ai_gateway_model_pricing_response_providers_item_models_item import (
        AiGatewayModelPricingResponseProvidersItemModelsItem,
    )
    from .ai_gateway_model_pricing_response_providers_item_models_item_cost import (
        AiGatewayModelPricingResponseProvidersItemModelsItemCost,
    )
    from .ai_gateway_model_pricing_response_providers_item_models_item_limit import (
        AiGatewayModelPricingResponseProvidersItemModelsItemLimit,
    )
    from .ai_gateway_model_pricing_response_providers_item_models_item_modalities import (
        AiGatewayModelPricingResponseProvidersItemModelsItemModalities,
    )
    from .ai_gateway_quota_alert_get_response import AiGatewayQuotaAlertGetResponse
    from .ai_gateway_quota_alert_upsert_response import AiGatewayQuotaAlertUpsertResponse
    from .ai_gateway_update_response import AiGatewayUpdateResponse
    from .ai_translate_survey_request_language_strategy import AiTranslateSurveyRequestLanguageStrategy
    from .ai_translate_survey_request_run_strategy import AiTranslateSurveyRequestRunStrategy
    from .ai_translate_survey_response import AiTranslateSurveyResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AiClassifySurveyRequestLanguageStrategy": ".ai_classify_survey_request_language_strategy",
    "AiClassifySurveyRequestRunStrategy": ".ai_classify_survey_request_run_strategy",
    "AiClassifySurveyResponse": ".ai_classify_survey_response",
    "AiGatewayDeleteResponse": ".ai_gateway_delete_response",
    "AiGatewayInfoResponse": ".ai_gateway_info_response",
    "AiGatewayLogsResponse": ".ai_gateway_logs_response",
    "AiGatewayLogsResponseItemsItem": ".ai_gateway_logs_response_items_item",
    "AiGatewayLogsResponseItemsItemStatus": ".ai_gateway_logs_response_items_item_status",
    "AiGatewayModelPricingResponse": ".ai_gateway_model_pricing_response",
    "AiGatewayModelPricingResponseProvidersItem": ".ai_gateway_model_pricing_response_providers_item",
    "AiGatewayModelPricingResponseProvidersItemModelsItem": ".ai_gateway_model_pricing_response_providers_item_models_item",
    "AiGatewayModelPricingResponseProvidersItemModelsItemCost": ".ai_gateway_model_pricing_response_providers_item_models_item_cost",
    "AiGatewayModelPricingResponseProvidersItemModelsItemLimit": ".ai_gateway_model_pricing_response_providers_item_models_item_limit",
    "AiGatewayModelPricingResponseProvidersItemModelsItemModalities": ".ai_gateway_model_pricing_response_providers_item_models_item_modalities",
    "AiGatewayQuotaAlertGetResponse": ".ai_gateway_quota_alert_get_response",
    "AiGatewayQuotaAlertUpsertResponse": ".ai_gateway_quota_alert_upsert_response",
    "AiGatewayUpdateResponse": ".ai_gateway_update_response",
    "AiTranslateSurveyRequestLanguageStrategy": ".ai_translate_survey_request_language_strategy",
    "AiTranslateSurveyRequestRunStrategy": ".ai_translate_survey_request_run_strategy",
    "AiTranslateSurveyResponse": ".ai_translate_survey_response",
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
    "AiClassifySurveyRequestLanguageStrategy",
    "AiClassifySurveyRequestRunStrategy",
    "AiClassifySurveyResponse",
    "AiGatewayDeleteResponse",
    "AiGatewayInfoResponse",
    "AiGatewayLogsResponse",
    "AiGatewayLogsResponseItemsItem",
    "AiGatewayLogsResponseItemsItemStatus",
    "AiGatewayModelPricingResponse",
    "AiGatewayModelPricingResponseProvidersItem",
    "AiGatewayModelPricingResponseProvidersItemModelsItem",
    "AiGatewayModelPricingResponseProvidersItemModelsItemCost",
    "AiGatewayModelPricingResponseProvidersItemModelsItemLimit",
    "AiGatewayModelPricingResponseProvidersItemModelsItemModalities",
    "AiGatewayQuotaAlertGetResponse",
    "AiGatewayQuotaAlertUpsertResponse",
    "AiGatewayUpdateResponse",
    "AiTranslateSurveyRequestLanguageStrategy",
    "AiTranslateSurveyRequestRunStrategy",
    "AiTranslateSurveyResponse",
]
