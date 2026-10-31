

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_details import ContactDetails
from .copy_log_details import CopyLogDetails
from .destination_account_details import DestinationAccountDetails
from .job_details_job_details_type import JobDetailsJobDetailsType
from .job_error_details import JobErrorDetails
from .job_stages import JobStages
from .package_shipping_details import PackageShippingDetails
from .preferences import Preferences
from .shipping_address import ShippingAddress


class JobDetails(UniversalBaseModel):
    """
    Job details.
    """

    chain_of_custody_sas_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="chainOfCustodySasKey"),
        pydantic.Field(
            alias="chainOfCustodySasKey", description="Shared access key to download the chain of custody logs"
        ),
    ] = None
    """
    Shared access key to download the chain of custody logs
    """

    contact_details: typing_extensions.Annotated[
        ContactDetails,
        FieldMetadata(alias="contactDetails"),
        pydantic.Field(alias="contactDetails", description="Contact details for notification and shipping."),
    ]
    """
    Contact details for notification and shipping.
    """

    copy_log_details: typing_extensions.Annotated[
        typing.Optional[typing.List[CopyLogDetails]],
        FieldMetadata(alias="copyLogDetails"),
        pydantic.Field(alias="copyLogDetails", description="List of copy log details."),
    ] = None
    """
    List of copy log details.
    """

    delivery_package: typing_extensions.Annotated[
        typing.Optional[PackageShippingDetails],
        FieldMetadata(alias="deliveryPackage"),
        pydantic.Field(alias="deliveryPackage", description="Delivery package shipping details."),
    ] = None
    """
    Delivery package shipping details.
    """

    destination_account_details: typing_extensions.Annotated[
        typing.List[DestinationAccountDetails],
        FieldMetadata(alias="destinationAccountDetails"),
        pydantic.Field(alias="destinationAccountDetails", description="Destination account details."),
    ]
    """
    Destination account details.
    """

    error_details: typing_extensions.Annotated[
        typing.Optional[typing.List[JobErrorDetails]],
        FieldMetadata(alias="errorDetails"),
        pydantic.Field(alias="errorDetails", description="Error details for failure. This is optional."),
    ] = None
    """
    Error details for failure. This is optional.
    """

    expected_data_size_in_terabytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expectedDataSizeInTerabytes"),
        pydantic.Field(
            alias="expectedDataSizeInTerabytes",
            description="The expected size of the data, which needs to be transferred in this job, in terabytes.",
        ),
    ] = None
    """
    The expected size of the data, which needs to be transferred in this job, in terabytes.
    """

    job_details_type: typing_extensions.Annotated[
        JobDetailsJobDetailsType,
        FieldMetadata(alias="jobDetailsType"),
        pydantic.Field(alias="jobDetailsType", description="Indicates the type of job details."),
    ]
    """
    Indicates the type of job details.
    """

    job_stages: typing_extensions.Annotated[
        typing.Optional[typing.List[JobStages]],
        FieldMetadata(alias="jobStages"),
        pydantic.Field(alias="jobStages", description="List of stages that run in the job."),
    ] = None
    """
    List of stages that run in the job.
    """

    preferences: typing.Optional[Preferences] = pydantic.Field(default=None)
    """
    Preferences for the order.
    """

    return_package: typing_extensions.Annotated[
        typing.Optional[PackageShippingDetails],
        FieldMetadata(alias="returnPackage"),
        pydantic.Field(alias="returnPackage", description="Return package shipping details."),
    ] = None
    """
    Return package shipping details.
    """

    reverse_shipment_label_sas_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reverseShipmentLabelSasKey"),
        pydantic.Field(
            alias="reverseShipmentLabelSasKey", description="Shared access key to download the return shipment label"
        ),
    ] = None
    """
    Shared access key to download the return shipment label
    """

    shipping_address: typing_extensions.Annotated[
        ShippingAddress,
        FieldMetadata(alias="shippingAddress"),
        pydantic.Field(alias="shippingAddress", description="Shipping address of the customer."),
    ]
    """
    Shipping address of the customer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
