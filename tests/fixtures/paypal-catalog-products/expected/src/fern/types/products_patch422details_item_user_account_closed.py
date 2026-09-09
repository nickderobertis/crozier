

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch422details_item_user_account_closed_description import (
    ProductsPatch422DetailsItemUserAccountClosedDescription,
)


class ProductsPatch422DetailsItemUserAccountClosed(UniversalBaseModel):
    description: typing.Optional[ProductsPatch422DetailsItemUserAccountClosedDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
