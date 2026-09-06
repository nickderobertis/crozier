

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_content_components_request_nodes_item_property_overrides_property_overrides_item import (
    UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem,
)


class UpdateContentComponentsRequestNodesItemPropertyOverrides(UniversalBaseModel):
    """
    Update text property overrides of a component instance
    """

    node_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId", description="Node UUID")
    ]
    """
    Node UUID
    """

    property_overrides: typing_extensions.Annotated[
        typing.List[UpdateContentComponentsRequestNodesItemPropertyOverridesPropertyOverridesItem],
        FieldMetadata(alias="propertyOverrides"),
        pydantic.Field(
            alias="propertyOverrides",
            description="A list of component instance properties to override within the specified secondary locale.",
        ),
    ]
    """
    A list of component instance properties to override within the specified secondary locale.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
