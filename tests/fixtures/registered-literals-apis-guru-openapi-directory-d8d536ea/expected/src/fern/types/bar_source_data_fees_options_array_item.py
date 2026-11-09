

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataFeesOptionsArrayItem(UniversalBaseModel):
    contingency_fees: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contingencyFees"), pydantic.Field(alias="contingencyFees")
    ] = None
    flat_fees: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="flatFees"), pydantic.Field(alias="flatFees")
    ] = None
    hourly_rate: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hourlyRate"), pydantic.Field(alias="hourlyRate")
    ] = None
    payment_plans: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="paymentPlans"), pydantic.Field(alias="paymentPlans")
    ] = None
    sliding_scale_fees: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="slidingScaleFees"), pydantic.Field(alias="slidingScaleFees")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
