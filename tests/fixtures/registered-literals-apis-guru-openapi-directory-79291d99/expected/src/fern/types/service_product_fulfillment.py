

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_product_fulfillment_detail import ServiceProductFulfillmentDetail


class ServiceProductFulfillment(UniversalBaseModel):
    """
    A collection of details related to a fulfillment service or product in terms of request, process and result.
    """

    service_product_fulfillment_detail: typing_extensions.Annotated[
        ServiceProductFulfillmentDetail,
        FieldMetadata(alias="SERVICE_PRODUCT_FULFILLMENT_DETAIL"),
        pydantic.Field(alias="SERVICE_PRODUCT_FULFILLMENT_DETAIL"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
