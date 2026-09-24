

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .update_quote_payload_sections_item import UpdateQuotePayloadSectionsItem


class UpdateQuotePayload(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    sections: typing.List[UpdateQuotePayloadSectionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(UpdateQuotePayload)
