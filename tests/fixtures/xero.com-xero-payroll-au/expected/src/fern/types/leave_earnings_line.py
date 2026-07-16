

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LeaveEarningsLine(UniversalBaseModel):
    earnings_rate_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EarningsRateID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero identifier
    """

    number_of_units: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="NumberOfUnits")] = (
        pydantic.Field(default=None)
    )
    """
    Earnings rate number of units.
    """

    rate_per_unit: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="RatePerUnit")] = (
        pydantic.Field(default=None)
    )
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
