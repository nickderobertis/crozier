

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fixed_expression_value import FixedExpressionValue


class ValueInputWithFixedValuesProvided(UniversalBaseModel):
    fixed_values_list: typing_extensions.Annotated[
        typing.Optional[typing.List[FixedExpressionValue]],
        FieldMetadata(alias="fixedValuesList"),
        pydantic.Field(alias="fixedValuesList"),
    ] = None
    allow_other_value: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowOtherValue"), pydantic.Field(alias="allowOtherValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
