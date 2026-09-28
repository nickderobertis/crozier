



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_mockserver_chaos_experiment_profiles_name_response import (
        DeleteMockserverChaosExperimentProfilesNameResponse,
    )
    from .delete_mockserver_chaos_experiment_profiles_name_response_status import (
        DeleteMockserverChaosExperimentProfilesNameResponseStatus,
    )
    from .delete_mockserver_chaos_experiment_response import DeleteMockserverChaosExperimentResponse
    from .delete_mockserver_chaos_experiment_response_status import DeleteMockserverChaosExperimentResponseStatus
    from .delete_mockserver_preemption_response import DeleteMockserverPreemptionResponse
    from .delete_mockserver_preemption_response_state import DeleteMockserverPreemptionResponseState
    from .get_mockserver_chaos_experiment_history_response import GetMockserverChaosExperimentHistoryResponse
    from .get_mockserver_chaos_experiment_profiles_response import GetMockserverChaosExperimentProfilesResponse
    from .get_mockserver_chaos_experiment_response import GetMockserverChaosExperimentResponse
    from .get_mockserver_chaos_experiment_response_status import GetMockserverChaosExperimentResponseStatus
    from .post_mockserver_chaos_experiment_apply_name_response import PostMockserverChaosExperimentApplyNameResponse
    from .post_mockserver_chaos_experiment_apply_name_response_status import (
        PostMockserverChaosExperimentApplyNameResponseStatus,
    )
    from .preemption_request_mode import PreemptionRequestMode
    from .put_mockserver_chaos_experiment_profiles_name_response import PutMockserverChaosExperimentProfilesNameResponse
    from .put_mockserver_chaos_experiment_profiles_name_response_status import (
        PutMockserverChaosExperimentProfilesNameResponseStatus,
    )
    from .put_mockserver_chaos_experiment_request_stages_item import PutMockserverChaosExperimentRequestStagesItem
    from .put_mockserver_chaos_experiment_response import PutMockserverChaosExperimentResponse
    from .put_mockserver_chaos_experiment_response_status import PutMockserverChaosExperimentResponseStatus
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteMockserverChaosExperimentProfilesNameResponse": ".delete_mockserver_chaos_experiment_profiles_name_response",
    "DeleteMockserverChaosExperimentProfilesNameResponseStatus": ".delete_mockserver_chaos_experiment_profiles_name_response_status",
    "DeleteMockserverChaosExperimentResponse": ".delete_mockserver_chaos_experiment_response",
    "DeleteMockserverChaosExperimentResponseStatus": ".delete_mockserver_chaos_experiment_response_status",
    "DeleteMockserverPreemptionResponse": ".delete_mockserver_preemption_response",
    "DeleteMockserverPreemptionResponseState": ".delete_mockserver_preemption_response_state",
    "GetMockserverChaosExperimentHistoryResponse": ".get_mockserver_chaos_experiment_history_response",
    "GetMockserverChaosExperimentProfilesResponse": ".get_mockserver_chaos_experiment_profiles_response",
    "GetMockserverChaosExperimentResponse": ".get_mockserver_chaos_experiment_response",
    "GetMockserverChaosExperimentResponseStatus": ".get_mockserver_chaos_experiment_response_status",
    "PostMockserverChaosExperimentApplyNameResponse": ".post_mockserver_chaos_experiment_apply_name_response",
    "PostMockserverChaosExperimentApplyNameResponseStatus": ".post_mockserver_chaos_experiment_apply_name_response_status",
    "PreemptionRequestMode": ".preemption_request_mode",
    "PutMockserverChaosExperimentProfilesNameResponse": ".put_mockserver_chaos_experiment_profiles_name_response",
    "PutMockserverChaosExperimentProfilesNameResponseStatus": ".put_mockserver_chaos_experiment_profiles_name_response_status",
    "PutMockserverChaosExperimentRequestStagesItem": ".put_mockserver_chaos_experiment_request_stages_item",
    "PutMockserverChaosExperimentResponse": ".put_mockserver_chaos_experiment_response",
    "PutMockserverChaosExperimentResponseStatus": ".put_mockserver_chaos_experiment_response_status",
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
    "DeleteMockserverChaosExperimentProfilesNameResponse",
    "DeleteMockserverChaosExperimentProfilesNameResponseStatus",
    "DeleteMockserverChaosExperimentResponse",
    "DeleteMockserverChaosExperimentResponseStatus",
    "DeleteMockserverPreemptionResponse",
    "DeleteMockserverPreemptionResponseState",
    "GetMockserverChaosExperimentHistoryResponse",
    "GetMockserverChaosExperimentProfilesResponse",
    "GetMockserverChaosExperimentResponse",
    "GetMockserverChaosExperimentResponseStatus",
    "PostMockserverChaosExperimentApplyNameResponse",
    "PostMockserverChaosExperimentApplyNameResponseStatus",
    "PreemptionRequestMode",
    "PutMockserverChaosExperimentProfilesNameResponse",
    "PutMockserverChaosExperimentProfilesNameResponseStatus",
    "PutMockserverChaosExperimentRequestStagesItem",
    "PutMockserverChaosExperimentResponse",
    "PutMockserverChaosExperimentResponseStatus",
]
