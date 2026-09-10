

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .four_hundred_one_details_item_description import FourHundredOneDetailsItemDescription
from .four_hundred_one_details_item_issue import FourHundredOneDetailsItemIssue


class FourHundredOneDetailsItem(UniversalBaseModel):
    issue: typing.Optional[FourHundredOneDetailsItemIssue] = None
    description: typing.Optional[FourHundredOneDetailsItemDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
