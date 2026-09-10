

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .four_hundred_twenty_two_details_item_duplicate_resource_identifier_description import (
    FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription,
)


class FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifier(UniversalBaseModel):
    description: typing.Optional[FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
