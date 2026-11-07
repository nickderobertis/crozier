

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.cursor import Cursor
from ...types.upload_session import UploadSession


class ListUploadsResponse(UniversalBaseModel):
    items: typing.List[UploadSession]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[Cursor], FieldMetadata(alias="nextCursor"), pydantic.Field(alias="nextCursor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
