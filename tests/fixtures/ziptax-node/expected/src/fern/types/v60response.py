

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60address_detail import V60AddressDetail
from .v60base_rate import V60BaseRate
from .v60metadata import V60Metadata
from .v60origin_destination import V60OriginDestination
from .v60product_detail import V60ProductDetail
from .v60service import V60Service
from .v60shipping import V60Shipping
from .v60tax_summary import V60TaxSummary


class V60Response(UniversalBaseModel):
    address_detail: typing_extensions.Annotated[
        V60AddressDetail,
        FieldMetadata(alias="addressDetail"),
        pydantic.Field(
            alias="addressDetail", description="Normalized and geocoded address details used for the lookup."
        ),
    ]
    """
    Normalized and geocoded address details used for the lookup.
    """

    base_rates: typing_extensions.Annotated[
        typing.Optional[typing.List[V60BaseRate]],
        FieldMetadata(alias="baseRates"),
        pydantic.Field(
            alias="baseRates",
            description="Component tax rates broken out by jurisdiction level (state/county/city/district) and tax type (sales/use). Sum the relevant components to obtain a combined rate.",
        ),
    ] = None
    """
    Component tax rates broken out by jurisdiction level (state/county/city/district) and tax type (sales/use). Sum the relevant components to obtain a combined rate.
    """

    metadata: V60Metadata = pydantic.Field()
    """
    Versioning and response-code metadata for the request.
    """

    product_detail: typing_extensions.Annotated[
        typing.Optional[V60ProductDetail],
        FieldMetadata(alias="productDetail"),
        pydantic.Field(
            alias="productDetail",
            description="Product-specific tax rules. Present only when a taxabilityCode is supplied on the request and the account carries the product_rates entitlement.",
        ),
    ] = None
    """
    Product-specific tax rules. Present only when a taxabilityCode is supplied on the request and the account carries the product_rates entitlement.
    """

    service: V60Service = pydantic.Field()
    """
    Whether services/labor are taxable in the resolved jurisdiction.
    """

    shipping: V60Shipping = pydantic.Field()
    """
    Whether freight/shipping is taxable in the resolved jurisdiction.
    """

    sourcing_rules: typing_extensions.Annotated[
        V60OriginDestination,
        FieldMetadata(alias="sourcingRules"),
        pydantic.Field(
            alias="sourcingRules",
            description="Sourcing model (origin- vs destination-based) that applies to the resolved location.",
        ),
    ]
    """
    Sourcing model (origin- vs destination-based) that applies to the resolved location.
    """

    tax_summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[V60TaxSummary]],
        FieldMetadata(alias="taxSummaries"),
        pydantic.Field(
            alias="taxSummaries",
            description="Aggregated sales and use tax rates for the location, summarizing the base rate components.",
        ),
    ] = None
    """
    Aggregated sales and use tax rates for the location, summarizing the base rate components.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
