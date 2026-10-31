

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_availability_request_sku_name import ScheduleAvailabilityRequestSkuName


class ScheduleAvailabilityRequest(UniversalBaseModel):
    """
    Request body to get the availability for scheduling orders.
    """

    sku_name: typing_extensions.Annotated[
        ScheduleAvailabilityRequestSkuName,
        FieldMetadata(alias="skuName"),
        pydantic.Field(alias="skuName", description="Sku Name for which the order is to be scheduled."),
    ]
    """
    Sku Name for which the order is to be scheduled.
    """

    storage_location: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="storageLocation"),
        pydantic.Field(
            alias="storageLocation",
            description="Location for data transfer. \r\nFor locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01",
        ),
    ]
    """
    Location for data transfer. 
    For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
