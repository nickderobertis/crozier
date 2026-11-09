

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chain_index import ChainIndex
from .unspent_siafund_element import UnspentSiafundElement


class AddressSiafundElementsResponse(UniversalBaseModel):
    basis: ChainIndex
    outputs: typing.List[UnspentSiafundElement]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
