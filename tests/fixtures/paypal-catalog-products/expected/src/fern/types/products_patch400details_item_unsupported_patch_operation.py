

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch400details_item_unsupported_patch_operation_description import (
    ProductsPatch400DetailsItemUnsupportedPatchOperationDescription,
)


class ProductsPatch400DetailsItemUnsupportedPatchOperation(UniversalBaseModel):
    description: typing.Optional[ProductsPatch400DetailsItemUnsupportedPatchOperationDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
