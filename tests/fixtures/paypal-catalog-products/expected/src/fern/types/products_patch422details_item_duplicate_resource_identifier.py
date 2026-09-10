

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch422details_item_duplicate_resource_identifier_description import (
    ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription,
)


class ProductsPatch422DetailsItemDuplicateResourceIdentifier(UniversalBaseModel):
    description: typing.Optional[ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
