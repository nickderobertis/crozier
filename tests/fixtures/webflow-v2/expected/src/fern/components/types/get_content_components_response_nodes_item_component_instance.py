

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_content_components_response_nodes_item_component_instance_property_overrides_item import (
    GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem,
)


class GetContentComponentsResponseNodesItemComponentInstance(UniversalBaseModel):
    """
    Represents a component instance within the DOM. It contains details about the component instance, such as its type and properties.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the component instance node
    """

    component_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="componentId"),
        pydantic.Field(alias="componentId", description="The unique identifier of the component"),
    ]
    """
    The unique identifier of the component
    """

    property_overrides: typing_extensions.Annotated[
        typing.List[GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem],
        FieldMetadata(alias="propertyOverrides"),
        pydantic.Field(
            alias="propertyOverrides",
            description="List of component properties with overrides for a component instance.",
        ),
    ]
    """
    List of component properties with overrides for a component instance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
