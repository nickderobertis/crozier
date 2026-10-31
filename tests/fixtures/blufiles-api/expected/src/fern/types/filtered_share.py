

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filtered_share_collection import FilteredShareCollection
from .filtered_share_file import FilteredShareFile
from .filtered_share_folder import FilteredShareFolder
from .filtered_share_owner import FilteredShareOwner
from .filtered_share_paste import FilteredSharePaste
from .filtered_share_type import FilteredShareType


class FilteredShare(UniversalBaseModel):
    id: str
    owner_id: typing_extensions.Annotated[str, FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")]
    type: FilteredShareType
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    views: float
    protected: bool
    owner: typing.Optional[FilteredShareOwner] = None
    file: typing.Optional[FilteredShareFile] = None
    folder: typing.Optional[FilteredShareFolder] = None
    collection: typing.Optional[FilteredShareCollection] = None
    paste: typing.Optional[FilteredSharePaste] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
