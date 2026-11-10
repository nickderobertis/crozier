

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .verification_status import VerificationStatus


class IncomeSummaryFieldString(UniversalBaseModel):
    """
    Data about the income summary
    """

    value: str = pydantic.Field()
    """
    The value of the field.
    """

    verification_status: VerificationStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
