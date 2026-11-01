

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class InferredReturnsDiscriminatedResultResponseResultData_Success(UniversalBaseModel):
    type: typing.Literal["success"] = "success"
    id: float
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    message: typing.Optional[typing.Any] = None
    code: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InferredReturnsDiscriminatedResultResponseResultData_Error(UniversalBaseModel):
    type: typing.Literal["error"] = "error"
    message: str
    code: float
    id: typing.Optional[typing.Any] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InferredReturnsDiscriminatedResultResponseResultData = typing_extensions.Annotated[
    typing.Union[
        InferredReturnsDiscriminatedResultResponseResultData_Success,
        InferredReturnsDiscriminatedResultResponseResultData_Error,
    ],
    pydantic.Field(discriminator="type"),
]
