

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency


class Balance(UniversalBaseModel):
    siacoins: Currency
    immature_siacoins: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="immatureSiacoins"), pydantic.Field(alias="immatureSiacoins")
    ]
    siafunds: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
