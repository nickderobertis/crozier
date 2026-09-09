

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch422details_item_duplicate_resource_identifier_description import (
    ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription,
)
from .products_patch422details_item_user_account_closed_description import (
    ProductsPatch422DetailsItemUserAccountClosedDescription,
)


class ProductsPatch422DetailsItem_UserAccountClosed(UniversalBaseModel):
    issue: typing.Literal["USER_ACCOUNT_CLOSED"] = "USER_ACCOUNT_CLOSED"
    description: typing.Optional[ProductsPatch422DetailsItemUserAccountClosedDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsPatch422DetailsItem_DuplicateResourceIdentifier(UniversalBaseModel):
    issue: typing.Literal["DUPLICATE_RESOURCE_IDENTIFIER"] = "DUPLICATE_RESOURCE_IDENTIFIER"
    description: typing.Optional[ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProductsPatch422DetailsItem = typing_extensions.Annotated[
    typing.Union[
        ProductsPatch422DetailsItem_UserAccountClosed, ProductsPatch422DetailsItem_DuplicateResourceIdentifier
    ],
    pydantic.Field(discriminator="issue"),
]
