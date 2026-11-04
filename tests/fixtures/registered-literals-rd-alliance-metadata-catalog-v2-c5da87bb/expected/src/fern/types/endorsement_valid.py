

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EndorsementValid(UniversalBaseModel):
    """
    The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
    If an end date is provided, it expresses the date on which the endorsement was withdrawn.
    """

    start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the period.
    """

    end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end date of the period (if applicable).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
