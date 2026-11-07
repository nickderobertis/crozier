

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .category_ref import CategoryRef
from .currency_code import CurrencyCode
from .non_empty_id import NonEmptyId
from .percent_bp import PercentBp
from .safe_url import SafeUrl
from .sku import Sku
from .timestamps import Timestamps


class Product(Timestamps):
    bonus_bp: typing_extensions.Annotated[
        typing.Optional[PercentBp], FieldMetadata(alias="bonusBP"), pydantic.Field(alias="bonusBP")
    ] = None
    category: CategoryRef
    currency: typing.Optional[CurrencyCode] = None
    description: typing.Optional[str] = None
    id: NonEmptyId
    name: str
    price_cents: typing_extensions.Annotated[int, FieldMetadata(alias="priceCents"), pydantic.Field(alias="priceCents")]
    site_url: typing_extensions.Annotated[
        typing.Optional[SafeUrl], FieldMetadata(alias="siteUrl"), pydantic.Field(alias="siteUrl")
    ] = None
    sku: Sku
    tags: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
