

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .profile_display_entry import ProfileDisplayEntry
from .profile_relative_entry import ProfileRelativeEntry


class ProfileEntry(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    display: typing.Optional[DisplayEntry] = None
    description: typing.Optional[ProfileDisplayEntry] = None
    selectable: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    module: typing.Optional[ProfileDisplayEntry] = None
    resource_type: typing_extensions.Annotated[
        typing.Optional[ProfileDisplayEntry], FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ] = None
    categories: typing.Optional[typing.List[ProfileDisplayEntry]] = None
    availability: typing.Optional[int] = None
    fields: typing.Optional[typing.List[ProfileDisplayEntry]] = None
    parents: typing.Optional[typing.List[ProfileRelativeEntry]] = None
    children: typing.Optional[typing.List[ProfileRelativeEntry]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
