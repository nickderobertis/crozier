

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .shared_meta import SharedMeta


class MyGlobal(UniversalBaseModel):
    id: str
    title: typing.Optional[str] = None
    meta: typing.Optional[SharedMeta] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
