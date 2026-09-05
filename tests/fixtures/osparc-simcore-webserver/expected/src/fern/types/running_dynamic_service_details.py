

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_boot_type import ServiceBootType
from .service_state import ServiceState
from .user_id_int import UserIdInt


class RunningDynamicServiceDetails(UniversalBaseModel):
    service_key: str = pydantic.Field()
    """
    distinctive name for the node based on the docker registry path
    """

    service_version: str = pydantic.Field()
    """
    semantic version number of the node
    """

    user_id: UserIdInt
    project_id: str
    service_uuid: str
    service_basepath: typing.Optional[str] = pydantic.Field(default=None)
    """
    predefined path where the dynamic service should be served. If empty, the service shall use the root endpoint.
    """

    boot_type: typing.Optional[ServiceBootType] = pydantic.Field(default=None)
    """
    Describes how the dynamic services was started (legacy=V0, modern=V2).Since legacy services do not have this label it defaults to V0.
    """

    service_host: str = pydantic.Field()
    """
    the service swarm internal host name
    """

    service_port: int = pydantic.Field()
    """
    the service swarm internal port
    """

    published_port: typing.Optional[int] = pydantic.Field(default=None)
    """
    the service swarm published port if any
    """

    entry_point: typing.Optional[str] = pydantic.Field(default=None)
    """
    if empty string the service entrypoint is on the root endpoint.
    """

    service_state: ServiceState = pydantic.Field()
    """
    service current state
    """

    service_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    additional information related to service state
    """

    is_collaborative: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if service allows collaboration (multi-tenant access)
    """

    product_name: str = pydantic.Field()
    """
    Product upon which this service is scheduled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
