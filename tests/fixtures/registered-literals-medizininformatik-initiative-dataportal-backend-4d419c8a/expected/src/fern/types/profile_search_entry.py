

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .profile_display_entry import ProfileDisplayEntry


class ProfileSearchEntry(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    display: typing.Optional[DisplayEntry] = None
    selectable: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    module: typing.Optional[ProfileDisplayEntry] = None
    resource_type: typing_extensions.Annotated[
        typing.Optional[ProfileDisplayEntry], FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ] = None
    categories: typing.Optional[typing.List[ProfileDisplayEntry]] = None
    availability: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
