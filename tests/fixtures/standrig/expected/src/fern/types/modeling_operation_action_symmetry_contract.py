

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_symmetry_contract_contract import ModelingOperationActionSymmetryContractContract


class ModelingOperationActionSymmetryContract(UniversalBaseModel):
    contract: ModelingOperationActionSymmetryContractContract

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
