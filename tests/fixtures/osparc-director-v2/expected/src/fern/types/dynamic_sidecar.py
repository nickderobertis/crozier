

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delayed_exception_handler import DelayedExceptionHandler
from .docker_container_inspect import DockerContainerInspect
from .service_removal_state import ServiceRemovalState
from .services_instrumentation import ServicesInstrumentation
from .simcore_service_director_v2models_dynamic_services_scheduler_status import (
    SimcoreServiceDirectorV2ModelsDynamicServicesSchedulerStatus,
)


class DynamicSidecar(UniversalBaseModel):
    status: typing.Optional[SimcoreServiceDirectorV2ModelsDynamicServicesSchedulerStatus] = pydantic.Field(default=None)
    """
    status of the service sidecar also with additional information
    """

    is_ready: typing.Optional[bool] = pydantic.Field(default=None)
    """
    is True while the health check on the dynamic-sidecar is responding. Meaning that the dynamic-sidecar is reachable and can accept requests
    """

    was_compose_spec_submitted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if the docker-compose spec was already submitted this fields is True
    """

    containers_inspect: typing.Optional[typing.List[DockerContainerInspect]] = pydantic.Field(default=None)
    """
    docker inspect results from all the container ran at regular intervals
    """

    was_dynamic_sidecar_started: typing.Optional[bool] = None
    is_healthy: typing.Optional[bool] = None
    were_containers_created: typing.Optional[bool] = pydantic.Field(default=None)
    """
    when True no longer will the Docker api be used to check if the services were started
    """

    is_project_network_attached: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When True, all containers were in running state and project networks were attached. Waiting for the container sto be in running state guarantees all containers have been created
    """

    is_service_environment_ready: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True when the environment setup required by the dynamic-sidecars created services was completed.Example: nodeports data downloaded, globally shared service data fetched, etc..
    """

    service_removal_state: typing.Optional[ServiceRemovalState] = pydantic.Field(default=None)
    """
    stores information used during service removal from the dynamic-sidecar scheduler
    """

    wait_for_manual_intervention_after_error: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Marks the sidecar as untouchable since there was an error and important data might be lost. awaits for manual intervention.
    """

    wait_for_manual_intervention_logged: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if a relative message was logged
    """

    were_state_and_outputs_saved: typing.Optional[bool] = pydantic.Field(default=None)
    """
    set True if the dy-sidecar saves the state and uploads the outputs
    """

    instrumentation: typing.Optional[ServicesInstrumentation] = pydantic.Field(default=None)
    """
    keeps track times for various operations
    """

    dynamic_sidecar_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    returned by the docker engine; used for starting the proxy
    """

    dynamic_sidecar_network_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    returned by the docker engine; used for starting the proxy
    """

    swarm_network_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    returned by the docker engine; used for starting the proxy
    """

    swarm_network_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    used for starting the proxy
    """

    docker_node_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    contains node id of the docker node where all services and created containers are started
    """

    inspect_error_handler: typing.Optional[DelayedExceptionHandler] = pydantic.Field(default=None)
    """
    Set when the dy-sidecar can no longer be reached by the director-v2. If it will be possible to reach the dy-sidecar again, this value will be set to None.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
