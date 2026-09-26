

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataIntegritySummary(UniversalBaseModel):
    by_amount: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="byAmount"), pydantic.Field(alias="byAmount")
    ] = None
    by_count: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="byCount"), pydantic.Field(alias="byCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
