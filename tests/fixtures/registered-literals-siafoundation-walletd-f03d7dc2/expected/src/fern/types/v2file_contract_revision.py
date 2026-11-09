

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2file_contract import V2FileContract
from .v2file_contract_element import V2FileContractElement


class V2FileContractRevision(UniversalBaseModel):
    parent: V2FileContractElement
    revision: V2FileContract

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
