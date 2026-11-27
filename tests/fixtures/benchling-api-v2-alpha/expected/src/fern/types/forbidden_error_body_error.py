

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ForbiddenErrorBodyError(UniversalBaseModel):
    invalid_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invalidId"), pydantic.Field(alias="invalidId")
    ] = None
    message: typing.Optional[str] = None
    type: typing.Optional[str] = None
    user_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userMessage"), pydantic.Field(alias="userMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
