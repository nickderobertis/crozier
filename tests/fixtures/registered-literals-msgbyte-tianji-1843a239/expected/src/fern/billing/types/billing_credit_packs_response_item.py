

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class BillingCreditPacksResponseItem(UniversalBaseModel):
    id: str
    name: str
    variant_id: typing_extensions.Annotated[str, FieldMetadata(alias="variantId"), pydantic.Field(alias="variantId")]
    credit: float
    price: float
    currency: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
