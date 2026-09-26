

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60shipping_extended import V60ShippingExtended
from .v60shipping_taxable import V60ShippingTaxable


class V60Shipping(UniversalBaseModel):
    adjustment_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="adjustmentType"),
        pydantic.Field(
            alias="adjustmentType", description="Freight taxation classification. Currently always 'FREIGHT_TAXABLE'."
        ),
    ]
    """
    Freight taxation classification. Currently always 'FREIGHT_TAXABLE'.
    """

    description: str = pydantic.Field()
    """
    Human-readable explanation of the freight/shipping taxability determination.
    """

    shipping_extended: typing_extensions.Annotated[
        typing.Optional[V60ShippingExtended],
        FieldMetadata(alias="shippingExtended"),
        pydantic.Field(
            alias="shippingExtended",
            description="Extended state-level shipping rule detail. Present only when shippingExtended=true is supplied on the request.",
        ),
    ] = None
    """
    Extended state-level shipping rule detail. Present only when shippingExtended=true is supplied on the request.
    """

    taxable: V60ShippingTaxable = pydantic.Field()
    """
    Whether freight/shipping is taxable in this jurisdiction. 'Y' = taxable, 'N' = not taxable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
