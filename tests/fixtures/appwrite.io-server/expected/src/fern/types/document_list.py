

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document import Document


class DocumentList(UniversalBaseModel):
    """
    Documents List
    """

    documents: typing.List[Document] = pydantic.Field()
    """
    List of documents.
    """

    sum: int = pydantic.Field()
    """
    Total sum of items in the list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
