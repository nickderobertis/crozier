

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch400details_item_missing_required_parameter_description import (
    ProductsPatch400DetailsItemMissingRequiredParameterDescription,
)


class ProductsPatch400DetailsItemMissingRequiredParameter(UniversalBaseModel):
    description: typing.Optional[ProductsPatch400DetailsItemMissingRequiredParameterDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
