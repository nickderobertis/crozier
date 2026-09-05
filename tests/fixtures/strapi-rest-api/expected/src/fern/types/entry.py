

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .document_meta import DocumentMeta


class Entry(DocumentMeta):
    """
    A generic Strapi document: content-type attributes plus system fields, flattened at the top level.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
