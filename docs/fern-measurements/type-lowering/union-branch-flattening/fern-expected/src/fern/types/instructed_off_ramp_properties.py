

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .instructed_off_ramp_properties_payment_instructions import InstructedOffRampPropertiesPaymentInstructions
from .off_ramp_properties import OffRampProperties


class InstructedOffRampProperties(OffRampProperties):
    payment_instructions: typing_extensions.Annotated[
        InstructedOffRampPropertiesPaymentInstructions,
        FieldMetadata(alias="paymentInstructions"),
        pydantic.Field(alias="paymentInstructions"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
