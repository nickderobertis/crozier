

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MyFunctionPermissionsGet(UniversalBaseModel):
    read_functions: typing_extensions.Annotated[
        bool, FieldMetadata(alias="readFunctions"), pydantic.Field(alias="readFunctions")
    ]
    write_functions: typing_extensions.Annotated[
        bool, FieldMetadata(alias="writeFunctions"), pydantic.Field(alias="writeFunctions")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
