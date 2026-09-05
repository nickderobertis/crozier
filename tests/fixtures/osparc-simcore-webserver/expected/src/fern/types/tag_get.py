

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tag_access_rights import TagAccessRights


class TagGet(UniversalBaseModel):
    id: int
    name: str
    description: typing.Optional[str] = None
    color: str
    access_rights: typing_extensions.Annotated[
        TagAccessRights, FieldMetadata(alias="accessRights"), pydantic.Field(alias="accessRights")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
