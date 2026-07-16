

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .manual_tax_type import ManualTaxType


class TaxLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Amount")] = pydantic.Field(
        default=None
    )
    """
    The tax line amount
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    Description of the tax line.
    """

    liability_account: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LiabilityAccount")] = (
        pydantic.Field(default=None)
    )
    """
    The tax line liability account code. For posted pay run you should be able to see liability account code
    """

    manual_tax_type: typing_extensions.Annotated[
        typing.Optional[ManualTaxType], FieldMetadata(alias="ManualTaxType")
    ] = None
    payslip_tax_line_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PayslipTaxLineID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero identifier for payslip tax line ID.
    """

    tax_type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TaxTypeName")] = (
        pydantic.Field(default=None)
    )
    """
    Name of the tax type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
