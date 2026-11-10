

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_stated_income_source_category import UserStatedIncomeSourceCategory
from .user_stated_income_source_frequency import UserStatedIncomeSourceFrequency
from .user_stated_income_source_pay_type import UserStatedIncomeSourcePayType


class LinkTokenCreateRequestUserStatedIncomeSource(UniversalBaseModel):
    """
    Specifies user stated income sources for the Income product
    """

    category: typing.Optional[UserStatedIncomeSourceCategory] = None
    employer: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employer corresponding to an income source specified by the user
    """

    pay_annual: typing.Optional[float] = pydantic.Field(default=None)
    """
    The income amount paid annually for a specified income source
    """

    pay_frequency: typing.Optional[UserStatedIncomeSourceFrequency] = None
    pay_per_cycle: typing.Optional[float] = pydantic.Field(default=None)
    """
    The income amount paid per cycle for a specified income source
    """

    pay_type: typing.Optional[UserStatedIncomeSourcePayType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
