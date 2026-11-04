

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserStatusPublic(UniversalBaseModel):
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    message: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    clear_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="clearAt"), pydantic.Field(alias="clearAt")
    ] = None
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
