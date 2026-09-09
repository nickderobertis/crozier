

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .four_hundred_three_details_item_description import FourHundredThreeDetailsItemDescription
from .four_hundred_three_details_item_issue import FourHundredThreeDetailsItemIssue


class FourHundredThreeDetailsItem(UniversalBaseModel):
    issue: typing.Optional[FourHundredThreeDetailsItemIssue] = None
    description: typing.Optional[FourHundredThreeDetailsItemDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
