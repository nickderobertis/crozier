

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class BirdeeInvestmentPortfolioGoal(UniversalBaseModel):
    amount_target: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The investment goal amount.
    """

    time_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The investment goal end time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
