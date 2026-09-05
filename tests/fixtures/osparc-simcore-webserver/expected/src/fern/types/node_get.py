

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_state import ServiceState


class NodeGet(UniversalBaseModel):
    published_port: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="publishedPort"),
        pydantic.Field(alias="publishedPort", description="The ports where the service provides its interface"),
    ] = None
    """
    The ports where the service provides its interface
    """

    entry_point: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entryPoint"),
        pydantic.Field(
            alias="entryPoint", description="The entry point where the service provides its interface if specified"
        ),
    ] = None
    """
    The entry point where the service provides its interface if specified
    """

    service_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceUuid"),
        pydantic.Field(alias="serviceUuid", description="The UUID attached to this service"),
    ]
    """
    The UUID attached to this service
    """

    service_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceKey"),
        pydantic.Field(
            alias="serviceKey", description="distinctive name for the node based on the docker registry path"
        ),
    ]
    """
    distinctive name for the node based on the docker registry path
    """

    service_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceVersion"),
        pydantic.Field(alias="serviceVersion", description="semantic version number"),
    ]
    """
    semantic version number
    """

    service_host: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceHost"),
        pydantic.Field(alias="serviceHost", description="service host name within the network"),
    ]
    """
    service host name within the network
    """

    service_port: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="servicePort"),
        pydantic.Field(alias="servicePort", description="port to access the service within the network"),
    ]
    """
    port to access the service within the network
    """

    service_basepath: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serviceBasepath"),
        pydantic.Field(
            alias="serviceBasepath",
            description="different base path where current service is mounted otherwise defaults to root",
        ),
    ] = None
    """
    different base path where current service is mounted otherwise defaults to root
    """

    service_state: typing_extensions.Annotated[
        ServiceState,
        FieldMetadata(alias="serviceState"),
        pydantic.Field(
            alias="serviceState",
            description="the service state * 'pending' - The service is waiting for resources to start * 'pulling' - The service is being pulled from the registry * 'starting' - The service is starting * 'running' - The service is running * 'complete' - The service completed * 'failed' - The service failed to start",
        ),
    ]
    """
    the service state * 'pending' - The service is waiting for resources to start * 'pulling' - The service is being pulled from the registry * 'starting' - The service is starting * 'running' - The service is running * 'complete' - The service completed * 'failed' - The service failed to start
    """

    service_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serviceMessage"),
        pydantic.Field(alias="serviceMessage", description="the service message"),
    ] = None
    """
    the service message
    """

    user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="the user that started the service"),
    ]
    """
    the user that started the service
    """

    product_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="productName"),
        pydantic.Field(alias="productName", description="Product upon which this service is scheduled."),
    ]
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
