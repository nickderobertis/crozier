

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error import Error
from .job_delivery_info import JobDeliveryInfo
from .job_details import JobDetails
from .job_properties_delivery_type import JobPropertiesDeliveryType
from .job_properties_status import JobPropertiesStatus


class JobProperties(UniversalBaseModel):
    """
    Job Properties
    """

    cancellation_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cancellationReason"),
        pydantic.Field(alias="cancellationReason", description="Reason for cancellation."),
    ] = None
    """
    Reason for cancellation.
    """

    delivery_info: typing_extensions.Annotated[
        typing.Optional[JobDeliveryInfo],
        FieldMetadata(alias="deliveryInfo"),
        pydantic.Field(alias="deliveryInfo", description="Delivery Info of Job."),
    ] = None
    """
    Delivery Info of Job.
    """

    delivery_type: typing_extensions.Annotated[
        typing.Optional[JobPropertiesDeliveryType],
        FieldMetadata(alias="deliveryType"),
        pydantic.Field(alias="deliveryType", description="Delivery type of Job."),
    ] = None
    """
    Delivery type of Job.
    """

    details: typing.Optional[JobDetails] = pydantic.Field(default=None)
    """
    Details of a job run. This field will only be sent for expand details filter.
    """

    error: typing.Optional[Error] = pydantic.Field(default=None)
    """
    Top level error for the job.
    """

    is_cancellable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCancellable"),
        pydantic.Field(alias="isCancellable", description="Describes whether the job is cancellable or not."),
    ] = None
    """
    Describes whether the job is cancellable or not.
    """

    is_cancellable_without_fee: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCancellableWithoutFee"),
        pydantic.Field(alias="isCancellableWithoutFee", description="Flag to indicate cancellation of scheduled job."),
    ] = None
    """
    Flag to indicate cancellation of scheduled job.
    """

    is_deletable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDeletable"),
        pydantic.Field(alias="isDeletable", description="Describes whether the job is deletable or not."),
    ] = None
    """
    Describes whether the job is deletable or not.
    """

    is_shipping_address_editable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isShippingAddressEditable"),
        pydantic.Field(
            alias="isShippingAddressEditable", description="Describes whether the shipping address is editable or not."
        ),
    ] = None
    """
    Describes whether the shipping address is editable or not.
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="Time at which the job was started in UTC ISO 8601 format."),
    ] = None
    """
    Time at which the job was started in UTC ISO 8601 format.
    """

    status: typing.Optional[JobPropertiesStatus] = pydantic.Field(default=None)
    """
    Name of the stage which is in progress.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
