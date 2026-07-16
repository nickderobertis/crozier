

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReimbursementLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Amount")] = pydantic.Field(
        default=None
    )
    """
    Reimbursement type amount
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    Reimbursement lines description (max length 50)
    """

    expense_account: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ExpenseAccount")] = (
        pydantic.Field(default=None)
    )
    """
    Reimbursement expense account. For posted pay run you should be able to see expense account code.
    """

    reimbursement_type_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ReimbursementTypeID")
    ] = pydantic.Field(default=None)
    """
    Xero reimbursement type identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
