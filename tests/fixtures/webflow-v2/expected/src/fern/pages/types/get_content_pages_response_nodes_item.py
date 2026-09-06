

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_content_pages_response_nodes_item_component_instance_property_overrides_item import (
    GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItem,
)
from .get_content_pages_response_nodes_item_image_image import GetContentPagesResponseNodesItemImageImage
from .get_content_pages_response_nodes_item_select_choices_item import GetContentPagesResponseNodesItemSelectChoicesItem
from .get_content_pages_response_nodes_item_text_text import GetContentPagesResponseNodesItemTextText


class GetContentPagesResponseNodesItem_Text(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["text"] = "text"
    id: str
    text: GetContentPagesResponseNodesItemTextText
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentPagesResponseNodesItem_Image(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["image"] = "image"
    id: str
    image: GetContentPagesResponseNodesItemImageImage
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentPagesResponseNodesItem_ComponentInstance(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["component-instance"] = "component-instance"
    id: str
    component_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="componentId"), pydantic.Field(alias="componentId")
    ]
    property_overrides: typing_extensions.Annotated[
        typing.List[GetContentPagesResponseNodesItemComponentInstancePropertyOverridesItem],
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


class GetContentPagesResponseNodesItem_TextInput(UniversalBaseModel):
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


class GetContentPagesResponseNodesItem_Select(UniversalBaseModel):
    """
    A generic representation of a content element within the Document Object Model (DOM). Each node has a unique identifier and a specific type that determines its content structure and attributes.
    """

    type: typing.Literal["select"] = "select"
    id: str
    choices: typing.List[GetContentPagesResponseNodesItemSelectChoicesItem]
    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetContentPagesResponseNodesItem_SubmitButton(UniversalBaseModel):
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


class GetContentPagesResponseNodesItem_SearchButton(UniversalBaseModel):
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


GetContentPagesResponseNodesItem = typing_extensions.Annotated[
    typing.Union[
        GetContentPagesResponseNodesItem_Text,
        GetContentPagesResponseNodesItem_Image,
        GetContentPagesResponseNodesItem_ComponentInstance,
        GetContentPagesResponseNodesItem_TextInput,
        GetContentPagesResponseNodesItem_Select,
        GetContentPagesResponseNodesItem_SubmitButton,
        GetContentPagesResponseNodesItem_SearchButton,
    ],
    pydantic.Field(discriminator="type"),
]
