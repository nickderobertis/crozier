

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .format_schema import FormatSchema


class Format(UniversalBaseModel):
    media_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")
    ] = None
    encoding: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[FormatSchema], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Format)
