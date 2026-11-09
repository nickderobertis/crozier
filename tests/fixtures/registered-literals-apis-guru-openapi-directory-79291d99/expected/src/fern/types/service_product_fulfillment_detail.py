

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_product_fulfillment_identifier import ServiceProductFulfillmentIdentifier


class ServiceProductFulfillmentDetail(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    service_product_fulfillment_identifier: typing_extensions.Annotated[
        ServiceProductFulfillmentIdentifier,
        FieldMetadata(alias="ServiceProductFulfillmentIdentifier"),
        pydantic.Field(alias="ServiceProductFulfillmentIdentifier"),
    ]
    vendor_order_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="VendorOrderIdentifier"),
        pydantic.Field(
            alias="VendorOrderIdentifier",
            description="A string that uniquely identifies a type of order Verification of Asset.",
        ),
    ] = None
    """
    A string that uniquely identifies a type of order Verification of Asset.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
