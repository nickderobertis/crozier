

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .profile_data_filter import ProfileDataFilter


class ProfileDataEntry(UniversalBaseModel):
    url: typing.Optional[str] = None
    display: typing.Optional[DisplayEntry] = None
    fields: typing.Optional[typing.List["ProfileDataField"]] = None
    filters: typing.Optional[typing.List[ProfileDataFilter]] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")
    ] = None
    error_cause: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorCause"), pydantic.Field(alias="errorCause")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .profile_data_field import ProfileDataField

update_forward_refs(ProfileDataEntry, ProfileDataField=ProfileDataField)
