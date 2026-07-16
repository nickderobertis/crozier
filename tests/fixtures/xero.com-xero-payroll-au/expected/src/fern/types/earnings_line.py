

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .earnings_rate_calculation_type import EarningsRateCalculationType


class EarningsLine(UniversalBaseModel):
    amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="Earnings rate amount"),
    ] = None
    """
    Earnings rate amount
    """

    annual_salary: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="AnnualSalary"),
        pydantic.Field(alias="AnnualSalary", description="Annual salary for earnings line"),
    ] = None
    """
    Annual salary for earnings line
    """

    calculation_type: typing_extensions.Annotated[
        typing.Optional[EarningsRateCalculationType],
        FieldMetadata(alias="CalculationType"),
        pydantic.Field(alias="CalculationType"),
    ] = None
    earnings_rate_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="EarningsRateID"),
        pydantic.Field(alias="EarningsRateID", description="Xero unique id for earnings rate"),
    ]
    """
    Xero unique id for earnings rate
    """

    fixed_amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="FixedAmount"),
        pydantic.Field(
            alias="FixedAmount",
            description="Earnings rate amount. Only applicable if the EarningsRate RateType is Fixed",
        ),
    ] = None
    """
    Earnings rate amount. Only applicable if the EarningsRate RateType is Fixed
    """

    normal_number_of_units: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NormalNumberOfUnits"),
        pydantic.Field(
            alias="NormalNumberOfUnits",
            description='Normal number of units for EarningsLine. Applicable when RateType is "MULTIPLE"',
        ),
    ] = None
    """
    Normal number of units for EarningsLine. Applicable when RateType is "MULTIPLE"
    """

    number_of_units: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NumberOfUnits"),
        pydantic.Field(alias="NumberOfUnits", description="Earnings rate number of units."),
    ] = None
    """
    Earnings rate number of units.
    """

    number_of_units_per_week: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NumberOfUnitsPerWeek"),
        pydantic.Field(alias="NumberOfUnitsPerWeek", description="number of units for earning line"),
    ] = None
    """
    number of units for earning line
    """

    rate_per_unit: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="RatePerUnit"),
        pydantic.Field(alias="RatePerUnit", description="Rate per unit of the EarningsLine."),
    ] = None
    """
    Rate per unit of the EarningsLine.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
