

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .add_quote_payload_sections_item import AddQuotePayloadSectionsItem


class AddQuotePayload(UniversalBaseModel):
    title: str
    description: typing.Optional[str] = None
    due_days: typing_extensions.Annotated[float, FieldMetadata(alias="dueDays"), pydantic.Field(alias="dueDays")]
    version_number: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="versionNumber"), pydantic.Field(alias="versionNumber")
    ] = None
    sections: typing.List[AddQuotePayloadSectionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(AddQuotePayload)
