

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_role_reclassify_expected_role import (
    TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole,
)
from .transaction_request_operations_operations_item_action_role_reclassify_role import (
    TransactionRequestOperationsOperationsItemActionRoleReclassifyRole,
)


class TransactionRequestOperationsOperationsItemActionRoleReclassify(UniversalBaseModel):
    expected_role: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole,
        FieldMetadata(alias="expectedRole"),
        pydantic.Field(alias="expectedRole"),
    ]
    role: TransactionRequestOperationsOperationsItemActionRoleReclassifyRole
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
