

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .percent_bp import PercentBp
from .product_ref import ProductRef
from .sku import Sku


class LineItem(UniversalBaseModel):
    bonus_bp: typing_extensions.Annotated[
        typing.Optional[PercentBp], FieldMetadata(alias="bonusBP"), pydantic.Field(alias="bonusBP")
    ] = None
    note: typing.Optional[str] = None
    product: ProductRef
    quantity: int
    sku: Sku
    unit_cents: typing_extensions.Annotated[int, FieldMetadata(alias="unitCents"), pydantic.Field(alias="unitCents")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
