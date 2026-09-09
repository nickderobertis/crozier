

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch400details_item_invalid_parameter_value_description import (
    ProductsPatch400DetailsItemInvalidParameterValueDescription,
)


class ProductsPatch400DetailsItemInvalidParameterValue(UniversalBaseModel):
    description: typing.Optional[ProductsPatch400DetailsItemInvalidParameterValueDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
