

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .data_element_base import DataElementBase


class MultiValuedDataElement(DataElementBase):
    """
    Multiple values of the same kind (EN 18223 clause 4.1.2.6). Values are either scalars or groups of nested data elements.
    """

    value_data_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="valueDataType"),
        pydantic.Field(alias="valueDataType", description="XSD type, when the values are scalars."),
    ] = None
    """
    XSD type, when the values are scalars.
    """

    value: typing.Optional[typing.List["MultiValuedDataElementValueItem"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .data_element import DataElement
from .data_element_collection import DataElementCollection
from .multi_valued_data_element_value_item import MultiValuedDataElementValueItem

update_forward_refs(
    MultiValuedDataElement,
    DataElement=DataElement,
    DataElementCollection=DataElementCollection,
    MultiValuedDataElementValueItem=MultiValuedDataElementValueItem,
)
