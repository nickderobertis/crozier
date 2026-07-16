

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deduction_type_calculation_type import DeductionTypeCalculationType


class DeductionLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="Deduction type amount"),
    ] = None
    """
    Deduction type amount
    """

    calculation_type: typing_extensions.Annotated[
        DeductionTypeCalculationType, FieldMetadata(alias="CalculationType"), pydantic.Field(alias="CalculationType")
    ]
    deduction_type_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DeductionTypeID"),
        pydantic.Field(alias="DeductionTypeID", description="Xero deduction type identifier"),
    ]
    """
    Xero deduction type identifier
    """

    number_of_units: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NumberOfUnits"),
        pydantic.Field(alias="NumberOfUnits", description="Deduction number of units"),
    ] = None
    """
    Deduction number of units
    """

    percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Percentage"),
        pydantic.Field(alias="Percentage", description="The Percentage of the Deduction"),
    ] = None
    """
    The Percentage of the Deduction
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
