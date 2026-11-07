

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_type import DocumentType
from .vector_store_item_model_id import VectorStoreItemModelId


class VectorStoreItem(UniversalBaseModel):
    """
    A single item in a vector store, containing text content and its vector embedding.
    """

    id: typing.Optional[str] = None
    document_id: str
    document_type: typing.Optional[DocumentType] = None
    model_id: typing.Optional[VectorStoreItemModelId] = None
    text: str
    embedding: typing.List[float]
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
    information about the object in a structured format, and querying for objects via API or the dashboard.
    
    Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
    512 characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
