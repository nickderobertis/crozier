

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_address import TaxCloudAddress
from .tax_cloud_exempt_state import TaxCloudExemptState


class TaxCloudCertResponse(UniversalBaseModel):
    account_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="accountId"),
        pydantic.Field(alias="accountId", description="The TaxCloud account id the certificate belongs to."),
    ]
    """
    The TaxCloud account id the certificate belongs to.
    """

    address: TaxCloudAddress = pydantic.Field()
    """
    Address of the exempt customer.
    """

    certificate_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="certificateId"),
        pydantic.Field(
            alias="certificateId",
            description="TaxCloud's identifier for the exemption certificate. Use it with /merchant/cert/get, /merchant/cert/delete, and as exemptionId on carts and orders.",
        ),
    ]
    """
    TaxCloud's identifier for the exemption certificate. Use it with /merchant/cert/get, /merchant/cert/delete, and as exemptionId on carts and orders.
    """

    connection_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionId"),
        pydantic.Field(alias="connectionId", description="The TaxCloud connection the certificate belongs to."),
    ]
    """
    The TaxCloud connection the certificate belongs to.
    """

    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(alias="createdDate", description="RFC3339 datetime the certificate was created."),
    ]
    """
    RFC3339 datetime the certificate was created.
    """

    customer_business_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customerBusinessDescription"),
        pydantic.Field(
            alias="customerBusinessDescription",
            description="Free-text description of the business, present when customerBusinessType is Other.",
        ),
    ] = None
    """
    Free-text description of the business, present when customerBusinessType is Other.
    """

    customer_business_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerBusinessType"),
        pydantic.Field(
            alias="customerBusinessType",
            description="The type of business the customer is (e.g. RetailTrade, Government, NonprofitOrganization).",
        ),
    ]
    """
    The type of business the customer is (e.g. RetailTrade, Government, NonprofitOrganization).
    """

    customer_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerId"),
        pydantic.Field(alias="customerId", description="Your identifier for the exempt customer."),
    ]
    """
    Your identifier for the exempt customer.
    """

    customer_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerName"),
        pydantic.Field(alias="customerName", description="Name of the customer the certificate was issued to."),
    ]
    """
    Name of the customer the certificate was issued to.
    """

    disabled_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="disabledAt"),
        pydantic.Field(
            alias="disabledAt", description="RFC3339 datetime the certificate was disabled, or null while it is active."
        ),
    ] = None
    """
    RFC3339 datetime the certificate was disabled, or null while it is active.
    """

    reason: str = pydantic.Field()
    """
    The reason the customer is exempt (e.g. Resale, FederalGovernment, CharitableOrganization).
    """

    reason_description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="reasonDescription"),
        pydantic.Field(alias="reasonDescription", description="Free-text elaboration of the exemption reason."),
    ]
    """
    Free-text elaboration of the exemption reason.
    """

    single_purchase: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="singlePurchase"),
        pydantic.Field(
            alias="singlePurchase",
            description="Whether the certificate covers a single purchase only, rather than being a blanket certificate.",
        ),
    ]
    """
    Whether the certificate covers a single purchase only, rather than being a blanket certificate.
    """

    states: typing.Optional[typing.List[TaxCloudExemptState]] = pydantic.Field(default=None)
    """
    The states the certificate is valid in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
