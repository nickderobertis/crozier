

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.account_category import AccountCategory
from .confirm_categories_categories_item_account_ref import ConfirmCategoriesCategoriesItemAccountRef


class ConfirmCategoriesCategoriesItem(UniversalBaseModel):
    account_ref: typing_extensions.Annotated[
        typing.Optional[ConfirmCategoriesCategoriesItemAccountRef],
        FieldMetadata(alias="accountRef"),
        pydantic.Field(alias="accountRef"),
    ] = None
    confirmed: typing.Optional[AccountCategory] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
