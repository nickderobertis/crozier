

from __future__ import annotations

import typing

from .multi_valued_data_element_value_item_zero import MultiValuedDataElementValueItemZero

if typing.TYPE_CHECKING:
    from .data_element import DataElement
MultiValuedDataElementValueItem = typing.Union[MultiValuedDataElementValueItemZero, typing.List["DataElement"]]
