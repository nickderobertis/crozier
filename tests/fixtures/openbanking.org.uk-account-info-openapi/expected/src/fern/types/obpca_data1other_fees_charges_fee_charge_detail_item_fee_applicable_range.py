

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObpcaData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange(UniversalBaseModel):
    """
    Range or amounts or rates for which the fee/charge applies
    """

    maximum_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MaximumAmount"),
        pydantic.Field(
            alias="MaximumAmount",
            description="Maximum Amount on which fee is applicable (where it is expressed as an amount)",
        ),
    ] = None
    """
    Maximum Amount on which fee is applicable (where it is expressed as an amount)
    """

    maximum_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MaximumRate"),
        pydantic.Field(
            alias="MaximumRate",
            description="Maximum rate on which fee/charge is applicable(where it is expressed as an rate)",
        ),
    ] = None
    """
    Maximum rate on which fee/charge is applicable(where it is expressed as an rate)
    """

    minimum_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MinimumAmount"),
        pydantic.Field(
            alias="MinimumAmount",
            description="Minimum Amount on which fee/charge is applicable (where it is expressed as an amount)",
        ),
    ] = None
    """
    Minimum Amount on which fee/charge is applicable (where it is expressed as an amount)
    """

    minimum_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MinimumRate"),
        pydantic.Field(
            alias="MinimumRate",
            description="Minimum rate on which fee/charge is applicable(where it is expressed as an rate)",
        ),
    ] = None
    """
    Minimum rate on which fee/charge is applicable(where it is expressed as an rate)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
