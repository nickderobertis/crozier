

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_policy import AccessPolicy


class Collaboration(UniversalBaseModel):
    access_policy: typing_extensions.Annotated[
        typing.Optional[AccessPolicy], FieldMetadata(alias="accessPolicy"), pydantic.Field(alias="accessPolicy")
    ] = None
    collaborator: typing.Any
    created_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    id: typing.Optional[str] = None
    item_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="itemId"), pydantic.Field(alias="itemId")
    ] = None
    item_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="itemType"), pydantic.Field(alias="itemType")
    ] = None
    modified_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
