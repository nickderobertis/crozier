

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class PricebookItemPricingTier(UniversalBaseModel):
    id: float
    price: float
    markup: float
    discount_rate: typing_extensions.Annotated[
        float, FieldMetadata(alias="discountRate"), pydantic.Field(alias="discountRate")
    ]
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
