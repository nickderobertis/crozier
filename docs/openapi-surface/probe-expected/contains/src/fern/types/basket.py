

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Basket(UniversalBaseModel):
    with_contains: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="withContains"), pydantic.Field(alias="withContains")
    ]
    without_contains: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="withoutContains"), pydantic.Field(alias="withoutContains")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
