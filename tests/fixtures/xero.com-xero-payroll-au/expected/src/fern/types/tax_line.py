

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .manual_tax_type import ManualTaxType


class TaxLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="The tax line amount"),
    ] = None
    """
    The tax line amount
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="Description of the tax line."),
    ] = None
    """
    Description of the tax line.
    """

    liability_account: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LiabilityAccount"),
        pydantic.Field(
            alias="LiabilityAccount",
            description="The tax line liability account code. For posted pay run you should be able to see liability account code",
        ),
    ] = None
    """
    The tax line liability account code. For posted pay run you should be able to see liability account code
    """

    manual_tax_type: typing_extensions.Annotated[
        typing.Optional[ManualTaxType], FieldMetadata(alias="ManualTaxType"), pydantic.Field(alias="ManualTaxType")
    ] = None
    payslip_tax_line_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayslipTaxLineID"),
        pydantic.Field(alias="PayslipTaxLineID", description="Xero identifier for payslip tax line ID."),
    ] = None
    """
    Xero identifier for payslip tax line ID.
    """

    tax_type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TaxTypeName"),
        pydantic.Field(alias="TaxTypeName", description="Name of the tax type."),
    ] = None
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
