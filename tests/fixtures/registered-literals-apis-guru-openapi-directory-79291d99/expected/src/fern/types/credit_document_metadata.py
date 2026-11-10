

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_document_type import CreditDocumentType


class CreditDocumentMetadata(UniversalBaseModel):
    """
    Object representing metadata pertaining to the document.
    """

    document_type: typing.Optional[CreditDocumentType] = None
    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Signed URL to retrieve the underlying file.
    """

    name: str = pydantic.Field()
    """
    The name of the document.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The processing status of the document.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
