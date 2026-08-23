

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .data_element_base import DataElementBase


class DataElementCollection(DataElementBase):
    """
    A collection of nested data elements (EN 18223 clause 4.1.2.4).
    """

    elements: typing.Optional[typing.List["DataElement"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .data_element import DataElement
from .multi_valued_data_element import MultiValuedDataElement
from .multi_valued_data_element_value_item import MultiValuedDataElementValueItem

update_forward_refs(
    DataElementCollection,
    DataElement=DataElement,
    MultiValuedDataElement=MultiValuedDataElement,
    MultiValuedDataElementValueItem=MultiValuedDataElementValueItem,
)
