

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pay_frequency_value import PayFrequencyValue
from .verification_status import VerificationStatus


class PayFrequency(UniversalBaseModel):
    """
    The frequency of the pay period.
    """

    value: PayFrequencyValue
    verification_status: VerificationStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
