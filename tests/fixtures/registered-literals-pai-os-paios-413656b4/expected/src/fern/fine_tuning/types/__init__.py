



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_fine_tuning_job_request_hyperparameters import CreateFineTuningJobRequestHyperparameters
    from .create_fine_tuning_job_request_hyperparameters_batch_size import (
        CreateFineTuningJobRequestHyperparametersBatchSize,
    )
    from .create_fine_tuning_job_request_hyperparameters_batch_size_zero import (
        CreateFineTuningJobRequestHyperparametersBatchSizeZero,
    )
    from .create_fine_tuning_job_request_hyperparameters_learning_rate_multiplier import (
        CreateFineTuningJobRequestHyperparametersLearningRateMultiplier,
    )
    from .create_fine_tuning_job_request_hyperparameters_learning_rate_multiplier_zero import (
        CreateFineTuningJobRequestHyperparametersLearningRateMultiplierZero,
    )
    from .create_fine_tuning_job_request_hyperparameters_n_epochs import (
        CreateFineTuningJobRequestHyperparametersNEpochs,
    )
    from .create_fine_tuning_job_request_hyperparameters_n_epochs_zero import (
        CreateFineTuningJobRequestHyperparametersNEpochsZero,
    )
    from .create_fine_tuning_job_request_integrations_item import CreateFineTuningJobRequestIntegrationsItem
    from .create_fine_tuning_job_request_integrations_item_type import CreateFineTuningJobRequestIntegrationsItemType
    from .create_fine_tuning_job_request_integrations_item_wandb import CreateFineTuningJobRequestIntegrationsItemWandb
    from .create_fine_tuning_job_request_model import CreateFineTuningJobRequestModel
    from .create_fine_tuning_job_request_model_one import CreateFineTuningJobRequestModelOne
_dynamic_imports: typing.Dict[str, str] = {
    "CreateFineTuningJobRequestHyperparameters": ".create_fine_tuning_job_request_hyperparameters",
    "CreateFineTuningJobRequestHyperparametersBatchSize": ".create_fine_tuning_job_request_hyperparameters_batch_size",
    "CreateFineTuningJobRequestHyperparametersBatchSizeZero": ".create_fine_tuning_job_request_hyperparameters_batch_size_zero",
    "CreateFineTuningJobRequestHyperparametersLearningRateMultiplier": ".create_fine_tuning_job_request_hyperparameters_learning_rate_multiplier",
    "CreateFineTuningJobRequestHyperparametersLearningRateMultiplierZero": ".create_fine_tuning_job_request_hyperparameters_learning_rate_multiplier_zero",
    "CreateFineTuningJobRequestHyperparametersNEpochs": ".create_fine_tuning_job_request_hyperparameters_n_epochs",
    "CreateFineTuningJobRequestHyperparametersNEpochsZero": ".create_fine_tuning_job_request_hyperparameters_n_epochs_zero",
    "CreateFineTuningJobRequestIntegrationsItem": ".create_fine_tuning_job_request_integrations_item",
    "CreateFineTuningJobRequestIntegrationsItemType": ".create_fine_tuning_job_request_integrations_item_type",
    "CreateFineTuningJobRequestIntegrationsItemWandb": ".create_fine_tuning_job_request_integrations_item_wandb",
    "CreateFineTuningJobRequestModel": ".create_fine_tuning_job_request_model",
    "CreateFineTuningJobRequestModelOne": ".create_fine_tuning_job_request_model_one",
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
    "CreateFineTuningJobRequestHyperparameters",
    "CreateFineTuningJobRequestHyperparametersBatchSize",
    "CreateFineTuningJobRequestHyperparametersBatchSizeZero",
    "CreateFineTuningJobRequestHyperparametersLearningRateMultiplier",
    "CreateFineTuningJobRequestHyperparametersLearningRateMultiplierZero",
    "CreateFineTuningJobRequestHyperparametersNEpochs",
    "CreateFineTuningJobRequestHyperparametersNEpochsZero",
    "CreateFineTuningJobRequestIntegrationsItem",
    "CreateFineTuningJobRequestIntegrationsItemType",
    "CreateFineTuningJobRequestIntegrationsItemWandb",
    "CreateFineTuningJobRequestModel",
    "CreateFineTuningJobRequestModelOne",
]
