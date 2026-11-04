

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Error(UniversalBaseModel):
    test_case_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCaseId"), pydantic.Field(alias="testCaseId")
    ]
    test_case_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCaseName"), pydantic.Field(alias="testCaseName")
    ]
    error: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
