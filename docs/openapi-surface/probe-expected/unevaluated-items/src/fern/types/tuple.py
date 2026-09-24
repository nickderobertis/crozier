

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Tuple(UniversalBaseModel):
    with_unevaluated_items: typing_extensions.Annotated[
        typing.List[typing.Any],
        FieldMetadata(alias="withUnevaluatedItems"),
        pydantic.Field(alias="withUnevaluatedItems"),
    ]
    without_unevaluated_items: typing_extensions.Annotated[
        typing.List[typing.Any],
        FieldMetadata(alias="withoutUnevaluatedItems"),
        pydantic.Field(alias="withoutUnevaluatedItems"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
