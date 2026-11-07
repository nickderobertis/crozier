

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ValueInputWithDictEditor(UniversalBaseModel):
    dict_id: typing_extensions.Annotated[str, FieldMetadata(alias="dictId"), pydantic.Field(alias="dictId")]
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
