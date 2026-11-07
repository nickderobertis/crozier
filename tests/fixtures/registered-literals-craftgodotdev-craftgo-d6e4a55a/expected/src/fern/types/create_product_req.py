

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cents import Cents
from .currency_code import CurrencyCode
from .non_empty_id import NonEmptyId
from .sku import Sku


class CreateProductReq(UniversalBaseModel):
    category_id: typing_extensions.Annotated[
        NonEmptyId, FieldMetadata(alias="categoryId"), pydantic.Field(alias="categoryId")
    ]
    currency: typing.Optional[CurrencyCode] = None
    description: typing.Optional[str] = None
    name: str
    price_cents: typing_extensions.Annotated[
        Cents, FieldMetadata(alias="priceCents"), pydantic.Field(alias="priceCents")
    ]
    sku: Sku
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
