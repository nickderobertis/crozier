

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsMetricsDestinyMetricDefinition(UniversalBaseModel):
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    lower_value_is_better: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="lowerValueIsBetter")
    ] = None
    parent_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="parentNodeHashes")
    ] = pydantic.Field(default=None)
    """
    A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    """

    presentation_node_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="presentationNodeType")
    ] = None
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    tracking_objective_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="trackingObjectiveHash")
    ] = None
    trait_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="traitHashes")] = (
        None
    )
    trait_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="traitIds")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
