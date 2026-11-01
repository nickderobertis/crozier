

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_to_service_location_map import DestinationToServiceLocationMap
from .sku_capacity import SkuCapacity
from .sku_cost import SkuCost
from .sku_properties_disabled_reason import SkuPropertiesDisabledReason


class SkuProperties(UniversalBaseModel):
    """
    Properties of the sku.
    """

    api_versions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="apiVersions"),
        pydantic.Field(alias="apiVersions", description="Api versions that support this Sku."),
    ] = None
    """
    Api versions that support this Sku.
    """

    capacity: typing.Optional[SkuCapacity] = pydantic.Field(default=None)
    """
    Capacity of the Sku.
    """

    costs: typing.Optional[typing.List[SkuCost]] = pydantic.Field(default=None)
    """
    Cost of the Sku.
    """

    destination_to_service_location_map: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinationToServiceLocationMap]],
        FieldMetadata(alias="destinationToServiceLocationMap"),
        pydantic.Field(
            alias="destinationToServiceLocationMap", description="The map of destination location to service location."
        ),
    ] = None
    """
    The map of destination location to service location.
    """

    disabled_reason: typing_extensions.Annotated[
        typing.Optional[SkuPropertiesDisabledReason],
        FieldMetadata(alias="disabledReason"),
        pydantic.Field(alias="disabledReason", description="Reason why the Sku is disabled."),
    ] = None
    """
    Reason why the Sku is disabled.
    """

    disabled_reason_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="disabledReasonMessage"),
        pydantic.Field(alias="disabledReasonMessage", description="Message for why the Sku is disabled."),
    ] = None
    """
    Message for why the Sku is disabled.
    """

    required_feature: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requiredFeature"),
        pydantic.Field(alias="requiredFeature", description="Required feature to access the sku."),
    ] = None
    """
    Required feature to access the sku.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
