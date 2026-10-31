



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .http_validation_error import HttpValidationError
    from .multi_series_anomaly import MultiSeriesAnomaly
    from .multi_series_anomaly_model import MultiSeriesAnomalyModel
    from .multi_series_cross_validation import MultiSeriesCrossValidation
    from .multi_series_cross_validation_fewshot_loss import MultiSeriesCrossValidationFewshotLoss
    from .multi_series_cross_validation_finetune_loss import MultiSeriesCrossValidationFinetuneLoss
    from .multi_series_cross_validation_model import MultiSeriesCrossValidationModel
    from .multi_series_forecast import MultiSeriesForecast
    from .multi_series_forecast_fewshot_loss import MultiSeriesForecastFewshotLoss
    from .multi_series_forecast_finetune_loss import MultiSeriesForecastFinetuneLoss
    from .multi_series_forecast_model import MultiSeriesForecastModel
    from .multi_series_input import MultiSeriesInput
    from .multi_series_insample_forecast import MultiSeriesInsampleForecast
    from .multi_series_insample_forecast_model import MultiSeriesInsampleForecastModel
    from .single_series_forecast import SingleSeriesForecast
    from .single_series_forecast_fewshot_loss import SingleSeriesForecastFewshotLoss
    from .single_series_forecast_finetune_loss import SingleSeriesForecastFinetuneLoss
    from .single_series_forecast_model import SingleSeriesForecastModel
    from .single_series_insample_forecast import SingleSeriesInsampleForecast
    from .single_series_insample_forecast_model import SingleSeriesInsampleForecastModel
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "HttpValidationError": ".http_validation_error",
    "MultiSeriesAnomaly": ".multi_series_anomaly",
    "MultiSeriesAnomalyModel": ".multi_series_anomaly_model",
    "MultiSeriesCrossValidation": ".multi_series_cross_validation",
    "MultiSeriesCrossValidationFewshotLoss": ".multi_series_cross_validation_fewshot_loss",
    "MultiSeriesCrossValidationFinetuneLoss": ".multi_series_cross_validation_finetune_loss",
    "MultiSeriesCrossValidationModel": ".multi_series_cross_validation_model",
    "MultiSeriesForecast": ".multi_series_forecast",
    "MultiSeriesForecastFewshotLoss": ".multi_series_forecast_fewshot_loss",
    "MultiSeriesForecastFinetuneLoss": ".multi_series_forecast_finetune_loss",
    "MultiSeriesForecastModel": ".multi_series_forecast_model",
    "MultiSeriesInput": ".multi_series_input",
    "MultiSeriesInsampleForecast": ".multi_series_insample_forecast",
    "MultiSeriesInsampleForecastModel": ".multi_series_insample_forecast_model",
    "SingleSeriesForecast": ".single_series_forecast",
    "SingleSeriesForecastFewshotLoss": ".single_series_forecast_fewshot_loss",
    "SingleSeriesForecastFinetuneLoss": ".single_series_forecast_finetune_loss",
    "SingleSeriesForecastModel": ".single_series_forecast_model",
    "SingleSeriesInsampleForecast": ".single_series_insample_forecast",
    "SingleSeriesInsampleForecastModel": ".single_series_insample_forecast_model",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "HttpValidationError",
    "MultiSeriesAnomaly",
    "MultiSeriesAnomalyModel",
    "MultiSeriesCrossValidation",
    "MultiSeriesCrossValidationFewshotLoss",
    "MultiSeriesCrossValidationFinetuneLoss",
    "MultiSeriesCrossValidationModel",
    "MultiSeriesForecast",
    "MultiSeriesForecastFewshotLoss",
    "MultiSeriesForecastFinetuneLoss",
    "MultiSeriesForecastModel",
    "MultiSeriesInput",
    "MultiSeriesInsampleForecast",
    "MultiSeriesInsampleForecastModel",
    "SingleSeriesForecast",
    "SingleSeriesForecastFewshotLoss",
    "SingleSeriesForecastFinetuneLoss",
    "SingleSeriesForecastModel",
    "SingleSeriesInsampleForecast",
    "SingleSeriesInsampleForecastModel",
    "ValidationError",
    "ValidationErrorLocItem",
]
