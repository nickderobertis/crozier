

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2file_contract_element import V2FileContractElement
from .v2file_contract_resolution_resolution import V2FileContractResolutionResolution
from .v2file_contract_resolution_type import V2FileContractResolutionType


class V2FileContractResolution(UniversalBaseModel):
    parent: V2FileContractElement
    type: V2FileContractResolutionType
    resolution: V2FileContractResolutionResolution

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
