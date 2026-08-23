

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .multi_language_value import MultiLanguageValue
from .single_valued_data_element_value import SingleValuedDataElementValue


class DataElement_SingleValuedDataElement(UniversalBaseModel):
    """
    Abstract data element (EN 18223 clause 4.1.2.3). The concrete shape is selected by `objectType`.
    """

    object_type: typing_extensions.Annotated[
        typing.Literal["SingleValuedDataElement"], FieldMetadata(alias="objectType"), pydantic.Field(alias="objectType")
    ] = "SingleValuedDataElement"
    value_data_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueDataType"), pydantic.Field(alias="valueDataType")
    ] = None
    value: typing.Optional[SingleValuedDataElementValue] = None
    element_id: typing_extensions.Annotated[str, FieldMetadata(alias="elementId"), pydantic.Field(alias="elementId")]
    dictionary_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dictionaryReference"), pydantic.Field(alias="dictionaryReference")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DataElement_MultiValuedDataElement(UniversalBaseModel):
    """
    Abstract data element (EN 18223 clause 4.1.2.3). The concrete shape is selected by `objectType`.
    """

    object_type: typing_extensions.Annotated[
        typing.Literal["MultiValuedDataElement"], FieldMetadata(alias="objectType"), pydantic.Field(alias="objectType")
    ] = "MultiValuedDataElement"
    value_data_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueDataType"), pydantic.Field(alias="valueDataType")
    ] = None
    value: typing.Optional[typing.List["MultiValuedDataElementValueItem"]] = None
    element_id: typing_extensions.Annotated[str, FieldMetadata(alias="elementId"), pydantic.Field(alias="elementId")]
    dictionary_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dictionaryReference"), pydantic.Field(alias="dictionaryReference")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DataElement_MultiLanguageDataElement(UniversalBaseModel):
    """
    Abstract data element (EN 18223 clause 4.1.2.3). The concrete shape is selected by `objectType`.
    """

    object_type: typing_extensions.Annotated[
        typing.Literal["MultiLanguageDataElement"],
        FieldMetadata(alias="objectType"),
        pydantic.Field(alias="objectType"),
    ] = "MultiLanguageDataElement"
    value: typing.Optional[typing.List[MultiLanguageValue]] = None
    element_id: typing_extensions.Annotated[str, FieldMetadata(alias="elementId"), pydantic.Field(alias="elementId")]
    dictionary_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dictionaryReference"), pydantic.Field(alias="dictionaryReference")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DataElement_DataElementCollection(UniversalBaseModel):
    """
    Abstract data element (EN 18223 clause 4.1.2.3). The concrete shape is selected by `objectType`.
    """

    object_type: typing_extensions.Annotated[
        typing.Literal["DataElementCollection"], FieldMetadata(alias="objectType"), pydantic.Field(alias="objectType")
    ] = "DataElementCollection"
    elements: typing.Optional[typing.List["DataElement"]] = None
    element_id: typing_extensions.Annotated[str, FieldMetadata(alias="elementId"), pydantic.Field(alias="elementId")]
    dictionary_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dictionaryReference"), pydantic.Field(alias="dictionaryReference")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DataElement_RelatedResource(UniversalBaseModel):
    """
    Abstract data element (EN 18223 clause 4.1.2.3). The concrete shape is selected by `objectType`.
    """

    object_type: typing_extensions.Annotated[
        typing.Literal["RelatedResource"], FieldMetadata(alias="objectType"), pydantic.Field(alias="objectType")
    ] = "RelatedResource"
    resource_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceTitle"), pydantic.Field(alias="resourceTitle")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    url: typing.Optional[str] = None
    language: typing.Optional[str] = None
    element_id: typing_extensions.Annotated[str, FieldMetadata(alias="elementId"), pydantic.Field(alias="elementId")]
    dictionary_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dictionaryReference"), pydantic.Field(alias="dictionaryReference")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DataElement = typing_extensions.Annotated[
    typing.Union[
        DataElement_SingleValuedDataElement,
        DataElement_MultiValuedDataElement,
        DataElement_MultiLanguageDataElement,
        DataElement_DataElementCollection,
        DataElement_RelatedResource,
    ],
    pydantic.Field(discriminator="object_type"),
]
from .data_element_collection import DataElementCollection
from .multi_valued_data_element_value_item import MultiValuedDataElementValueItem
from .multi_valued_data_element import MultiValuedDataElement

update_forward_refs(
    DataElement_MultiValuedDataElement,
    DataElement=DataElement,
    DataElementCollection=DataElementCollection,
    MultiValuedDataElementValueItem=MultiValuedDataElementValueItem,
)
update_forward_refs(
    DataElement_DataElementCollection,
    DataElement=DataElement,
    MultiValuedDataElement=MultiValuedDataElement,
    MultiValuedDataElementValueItem=MultiValuedDataElementValueItem,
)
