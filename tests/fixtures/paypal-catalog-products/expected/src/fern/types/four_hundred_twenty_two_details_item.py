

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .four_hundred_twenty_two_details_item_country_not_supported_description import (
    FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription,
)
from .four_hundred_twenty_two_details_item_duplicate_resource_identifier_description import (
    FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription,
)
from .four_hundred_twenty_two_details_item_user_account_closed_description import (
    FourHundredTwentyTwoDetailsItemUserAccountClosedDescription,
)


class FourHundredTwentyTwoDetailsItem_UserAccountClosed(UniversalBaseModel):
    issue: typing.Literal["USER_ACCOUNT_CLOSED"] = "USER_ACCOUNT_CLOSED"
    description: typing.Optional[FourHundredTwentyTwoDetailsItemUserAccountClosedDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FourHundredTwentyTwoDetailsItem_DuplicateResourceIdentifier(UniversalBaseModel):
    issue: typing.Literal["DUPLICATE_RESOURCE_IDENTIFIER"] = "DUPLICATE_RESOURCE_IDENTIFIER"
    description: typing.Optional[FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FourHundredTwentyTwoDetailsItem_CountryNotSupported(UniversalBaseModel):
    issue: typing.Literal["COUNTRY_NOT_SUPPORTED"] = "COUNTRY_NOT_SUPPORTED"
    description: typing.Optional[FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FourHundredTwentyTwoDetailsItem = typing_extensions.Annotated[
    typing.Union[
        FourHundredTwentyTwoDetailsItem_UserAccountClosed,
        FourHundredTwentyTwoDetailsItem_DuplicateResourceIdentifier,
        FourHundredTwentyTwoDetailsItem_CountryNotSupported,
    ],
    pydantic.Field(discriminator="issue"),
]
