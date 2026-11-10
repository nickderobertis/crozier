

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_type import DocType


class DocumentMetadata(UniversalBaseModel):
    """
    An object representing metadata from the end user's uploaded document.
    """

    doc_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier of the document that is also present in the paystub response.
    """

    doc_type: typing.Optional[DocType] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the document.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The processing status of the document.
    
    `PROCESSING_COMPLETE`: The document was successfully processed.
    
    `DOCUMENT_ERROR`: The document could not be processed. Possible causes include: The document was an unacceptable document type such as an offer letter or bank statement, the document image was cropped or blurry, or the document was corrupted.
    
    `UNKNOWN` or `null`: An internal error occured. If this happens repeatedly, contact support or your Plaid account manager.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
