

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_employment_verification import CreditEmploymentVerification
from .item_id import ItemId


class CreditEmploymentItem(UniversalBaseModel):
    """
    The object containing employment items.
    """

    employment_report_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token to represent the underlying Employment data
    """

    employments: typing.List[CreditEmploymentVerification]
    item_id: ItemId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
