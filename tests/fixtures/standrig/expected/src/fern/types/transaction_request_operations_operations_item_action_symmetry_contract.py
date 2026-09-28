

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_symmetry_contract_contract import (
    TransactionRequestOperationsOperationsItemActionSymmetryContractContract,
)


class TransactionRequestOperationsOperationsItemActionSymmetryContract(UniversalBaseModel):
    contract: TransactionRequestOperationsOperationsItemActionSymmetryContractContract

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
