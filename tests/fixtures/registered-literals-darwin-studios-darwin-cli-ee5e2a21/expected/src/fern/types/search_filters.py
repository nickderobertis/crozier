

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_filters_capability_kinds_item import SearchFiltersCapabilityKindsItem
from .search_filters_capability_types_item import SearchFiltersCapabilityTypesItem
from .search_filters_execution_domains_item import SearchFiltersExecutionDomainsItem
from .search_filters_protocols_item import SearchFiltersProtocolsItem


class SearchFilters(UniversalBaseModel):
    capability_types: typing_extensions.Annotated[
        typing.Optional[typing.List[SearchFiltersCapabilityTypesItem]],
        FieldMetadata(alias="capabilityTypes"),
        pydantic.Field(
            alias="capabilityTypes",
            description="Return only these public capability types. PRODUCT is a purchasable item, SERVICE is delivered work, CAPABILITY is an executable ability, CAPACITY is available throughput, ASSET is a licensable resource, DATA is a dataset, and RIGHT is a permission or entitlement.",
        ),
    ] = None
    """
    Return only these public capability types. PRODUCT is a purchasable item, SERVICE is delivered work, CAPABILITY is an executable ability, CAPACITY is available throughput, ASSET is a licensable resource, DATA is a dataset, and RIGHT is a permission or entitlement.
    """

    execution_domains: typing_extensions.Annotated[
        typing.Optional[typing.List[SearchFiltersExecutionDomainsItem]],
        FieldMetadata(alias="executionDomains"),
        pydantic.Field(
            alias="executionDomains",
            description="Return only capabilities delivered in these execution domains: HUMAN for people-led work, DIGITAL for software or online work, and PHYSICAL for work involving real-world goods or locations.",
        ),
    ] = None
    """
    Return only capabilities delivered in these execution domains: HUMAN for people-led work, DIGITAL for software or online work, and PHYSICAL for work involving real-world goods or locations.
    """

    capability_kinds: typing_extensions.Annotated[
        typing.Optional[typing.List[SearchFiltersCapabilityKindsItem]],
        FieldMetadata(alias="capabilityKinds"),
        pydantic.Field(
            alias="capabilityKinds",
            description="Return only these executable capability kinds. Use this when the integration mechanism is a hard requirement; leave it unset when Darwin should rank across mechanisms.",
        ),
    ] = None
    """
    Return only these executable capability kinds. Use this when the integration mechanism is a hard requirement; leave it unset when Darwin should rank across mechanisms.
    """

    protocols: typing.Optional[typing.List[SearchFiltersProtocolsItem]] = pydantic.Field(default=None)
    """
    Require every returned capability to support each listed public protocol. Multiple values use AND semantics, not OR semantics.
    """

    max_price_minor: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxPriceMinor"),
        pydantic.Field(
            alias="maxPriceMinor",
            description="Maximum acceptable advertised starting price in the smallest unit of the requested currency, such as cents for USD.",
        ),
    ] = None
    """
    Maximum acceptable advertised starting price in the smallest unit of the requested currency, such as cents for USD.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Require structured pricing in this uppercase ISO 4217 currency.
    """

    requires_executable_route: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="requiresExecutableRoute"),
        pydantic.Field(
            alias="requiresExecutableRoute",
            description="When true, require an observed executable route in the active index. This does not grant the caller permission to start an Act action.",
        ),
    ] = None
    """
    When true, require an observed executable route in the active index. This does not grant the caller permission to start an Act action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
