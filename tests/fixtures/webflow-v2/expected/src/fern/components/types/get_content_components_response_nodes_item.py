

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_content_components_response_nodes_item_component_instance_property_overrides_item import (
    GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem,
)
from .get_content_components_response_nodes_item_image_image import GetContentComponentsResponseNodesItemImageImage
from .get_content_components_response_nodes_item_select_choices_item import (
    GetContentComponentsResponseNodesItemSelectChoicesItem,
)
from .get_content_components_response_nodes_item_text_text import GetContentComponentsResponseNodesItemTextText


class GetContentComponentsResponseNodesItem_Text(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["text"] = "text"
    id: str
    text: GetContentComponentsResponseNodesItemTextText
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentComponentsResponseNodesItem_Image(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["image"] = "image"
    id: str
    image: GetContentComponentsResponseNodesItemImageImage
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentComponentsResponseNodesItem_ComponentInstance(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["component-instance"] = "component-instance"
    id: str
    component_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="componentId"), pydantic.Field(alias="componentId")
    ]
    property_overrides: typing_extensions.Annotated[
        typing.List[GetContentComponentsResponseNodesItemComponentInstancePropertyOverridesItem],
        FieldMetadata(alias="propertyOverrides"),
        pydantic.Field(alias="propertyOverrides"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentComponentsResponseNodesItem_TextInput(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["text-input"] = "text-input"
    id: str
    placeholder: str
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentComponentsResponseNodesItem_Select(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["select"] = "select"
    id: str
    choices: typing.List[GetContentComponentsResponseNodesItemSelectChoicesItem]
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentComponentsResponseNodesItem_SubmitButton(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["submit-button"] = "submit-button"
    id: str
    value: str
    waiting_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="waitingText"), pydantic.Field(alias="waitingText")
    ]
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentComponentsResponseNodesItem_SearchButton(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["search-button"] = "search-button"
    id: str
    value: str
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GetContentComponentsResponseNodesItem = typing_extensions.Annotated[
    typing.Union[
        GetContentComponentsResponseNodesItem_Text,
        GetContentComponentsResponseNodesItem_Image,
        GetContentComponentsResponseNodesItem_ComponentInstance,
        GetContentComponentsResponseNodesItem_TextInput,
        GetContentComponentsResponseNodesItem_Select,
        GetContentComponentsResponseNodesItem_SubmitButton,
        GetContentComponentsResponseNodesItem_SearchButton,
    ],
    pydantic.Field(discriminator="type"),
]
