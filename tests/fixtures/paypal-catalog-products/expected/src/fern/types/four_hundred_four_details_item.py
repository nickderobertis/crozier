

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .four_hundred_four_details_item_description import FourHundredFourDetailsItemDescription
from .four_hundred_four_details_item_issue import FourHundredFourDetailsItemIssue


class FourHundredFourDetailsItem(UniversalBaseModel):
    issue: typing.Optional[FourHundredFourDetailsItemIssue] = None
    description: typing.Optional[FourHundredFourDetailsItemDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
