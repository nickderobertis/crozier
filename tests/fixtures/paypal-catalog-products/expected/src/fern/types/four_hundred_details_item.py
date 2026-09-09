

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .four_hundred_details_item_description import FourHundredDetailsItemDescription
from .four_hundred_details_item_issue import FourHundredDetailsItemIssue


class FourHundredDetailsItem(UniversalBaseModel):
    issue: typing.Optional[FourHundredDetailsItemIssue] = None
    description: typing.Optional[FourHundredDetailsItemDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
