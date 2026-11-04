

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilesSharingShareInfo(UniversalBaseModel):
    id: int
    parent_id: typing_extensions.Annotated[int, FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")]
    mtime: int
    name: str
    permissions: int
    mimetype: str
    size: int
    type: str
    etag: str
    children: typing.Optional[typing.List[typing.Dict[str, typing.Dict[str, typing.Any]]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
