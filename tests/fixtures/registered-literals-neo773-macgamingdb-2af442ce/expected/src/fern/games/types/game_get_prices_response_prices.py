

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GameGetPricesResponsePrices(UniversalBaseModel):
    current_retail: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentRetail"), pydantic.Field(alias="currentRetail")
    ]
    current_keyshops: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentKeyshops"), pydantic.Field(alias="currentKeyshops")
    ]
    historical_retail: typing_extensions.Annotated[
        str, FieldMetadata(alias="historicalRetail"), pydantic.Field(alias="historicalRetail")
    ]
    historical_keyshops: typing_extensions.Annotated[
        str, FieldMetadata(alias="historicalKeyshops"), pydantic.Field(alias="historicalKeyshops")
    ]
    currency: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
