

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document import Document


class RankedDocument(UniversalBaseModel):
    """
    A ranked document with a relevance score and an index position.
    """

    index: int = pydantic.Field()
    """
    The index position of the document from the original request.
    """

    score: float = pydantic.Field()
    """
    The relevance of the document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.
    """

    document: typing.Optional[Document] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
