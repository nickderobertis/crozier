

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsSocketsDestinySocketTypeScalarMaterialRequirementEntry(UniversalBaseModel):
    currency_item_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currencyItemHash"), pydantic.Field(alias="currencyItemHash")
    ] = None
    scalar_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="scalarValue"), pydantic.Field(alias="scalarValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
