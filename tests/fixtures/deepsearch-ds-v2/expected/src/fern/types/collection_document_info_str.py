

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collection_document_info_str_type import CollectionDocumentInfoStrType


class CollectionDocumentInfoStr(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the collection.
    """

    type: CollectionDocumentInfoStrType = pydantic.Field()
    """
    The collection type.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of this collection model.
    """

    alias: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags (aliases) for the collection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
