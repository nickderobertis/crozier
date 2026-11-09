

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_status_down_details import ServiceStatusDownDetails
from .service_status_service_details import ServiceStatusServiceDetails


class ServiceStatus(UniversalBaseModel):
    object: str = pydantic.Field()
    """
    Name of the object
    """

    service_details: typing_extensions.Annotated[
        ServiceStatusServiceDetails,
        FieldMetadata(alias="serviceDetails"),
        pydantic.Field(alias="serviceDetails", description="Status Details of Case Update Services Status."),
    ]
    """
    Status Details of Case Update Services Status.
    """

    service_status_down_details: typing_extensions.Annotated[
        typing.Optional[ServiceStatusDownDetails],
        FieldMetadata(alias="serviceStatusDownDetails"),
        pydantic.Field(alias="serviceStatusDownDetails"),
    ] = None
    service_up: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="serviceUp"),
        pydantic.Field(alias="serviceUp", description="Status of Case Update Services Status."),
    ]
    """
    Status of Case Update Services Status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
