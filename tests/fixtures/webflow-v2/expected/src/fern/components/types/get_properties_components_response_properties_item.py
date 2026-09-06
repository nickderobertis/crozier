

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_properties_components_response_properties_item_text import GetPropertiesComponentsResponsePropertiesItemText
from .get_properties_components_response_properties_item_type import GetPropertiesComponentsResponsePropertiesItemType


class GetPropertiesComponentsResponsePropertiesItem(UniversalBaseModel):
    """
    A text-based component property containing raw text and HTML representation.
    """

    property_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="propertyId"),
        pydantic.Field(alias="propertyId", description="The ID of the property."),
    ]
    """
    The ID of the property.
    """

    type: GetPropertiesComponentsResponsePropertiesItemType = pydantic.Field()
    """
    The type of the property.
    """

    label: str = pydantic.Field()
    """
    The label of the property in the UI.
    """

    text: GetPropertiesComponentsResponsePropertiesItemText = pydantic.Field()
    """
    Represents text content within the DOM. It contains both the raw text and its HTML representation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
