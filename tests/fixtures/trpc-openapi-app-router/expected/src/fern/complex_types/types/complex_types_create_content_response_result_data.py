

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ComplexTypesCreateContentResponseResultData_Success(UniversalBaseModel):
    status: typing.Literal["success"] = "success"
    id: float
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ComplexTypesCreateContentResponseResultData_Error(UniversalBaseModel):
    status: typing.Literal["error"] = "error"
    message: str
    code: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ComplexTypesCreateContentResponseResultData = typing_extensions.Annotated[
    typing.Union[
        ComplexTypesCreateContentResponseResultData_Success, ComplexTypesCreateContentResponseResultData_Error
    ],
    pydantic.Field(discriminator="status"),
]
