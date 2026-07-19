

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invalid_param import InvalidParam


class ProblemDetails(UniversalBaseModel):
    type: typing.Optional[str] = None
    title: typing.Optional[str] = None
    status: typing.Optional[int] = None
    detail: typing.Optional[str] = None
    instance: typing.Optional[str] = None
    cause: typing.Optional[str] = None
    invalid_params: typing_extensions.Annotated[
        typing.Optional[typing.List[InvalidParam]],
        FieldMetadata(alias="invalidParams"),
        pydantic.Field(alias="invalidParams"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
