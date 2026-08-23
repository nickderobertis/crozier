

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .dpp_envelope import DppEnvelope


class DigitalProductPassportFull(DppEnvelope):
    """
    Full (expanded) representation — EN 18223 Annex A. The envelope plus an array of explicit DataElements.
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
from .data_element_collection import DataElementCollection
from .multi_valued_data_element import MultiValuedDataElement
from .multi_valued_data_element_value_item import MultiValuedDataElementValueItem

update_forward_refs(
    DigitalProductPassportFull,
    DataElement=DataElement,
    DataElementCollection=DataElementCollection,
    MultiValuedDataElement=MultiValuedDataElement,
    MultiValuedDataElementValueItem=MultiValuedDataElementValueItem,
)
