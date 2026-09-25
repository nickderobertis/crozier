

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QuoteTotalsQuoteTotal(UniversalBaseModel):
    sub_total: typing_extensions.Annotated[float, FieldMetadata(alias="subTotal"), pydantic.Field(alias="subTotal")]
    discount: float
    discounted_sub_total: typing_extensions.Annotated[
        float, FieldMetadata(alias="discountedSubTotal"), pydantic.Field(alias="discountedSubTotal")
    ]
    gst: float
    total: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
