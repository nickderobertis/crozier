

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .user_settings_document_key import UserSettingsDocumentKey


class GetUserSettingsResponseDocument(UniversalBaseModel):
    document_key: typing_extensions.Annotated[
        UserSettingsDocumentKey, FieldMetadata(alias="documentKey"), pydantic.Field(alias="documentKey")
    ]
    value: typing.Optional["JsonValue"] = None
    version: int
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value import JsonValue

update_forward_refs(GetUserSettingsResponseDocument, JsonValue=JsonValue)
