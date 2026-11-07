

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .document_type import DocumentType
from .page import Page


class Document(UniversalBaseModel):
    type: typing.Optional[DocumentType] = pydantic.Field(default=None)
    """
    The node type. Identifies this node as the root of the structure tree.
    """

    children: typing.Optional[typing.List[Page]] = pydantic.Field(default=None)
    """
    The pages of the document, in source order.
    """

    markdown: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full document markdown — identical to the top-level `markdown` field, included so the structure tree is self-contained. Present only when `options.inline_markdown` is `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Document)
