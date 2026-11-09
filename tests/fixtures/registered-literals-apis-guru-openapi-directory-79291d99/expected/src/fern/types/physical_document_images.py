

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_image_back import DocumentImageBack
from .document_image_cropped_back import DocumentImageCroppedBack
from .document_image_cropped_front import DocumentImageCroppedFront
from .document_image_face import DocumentImageFace
from .document_image_front import DocumentImageFront


class PhysicalDocumentImages(UniversalBaseModel):
    """
    URLs for downloading original and cropped images for this document submission. The URLs are designed to only allow downloading, not hot linking, so the URL will only serve the document image for 60 seconds before expiring. The expiration time is 60 seconds after the `GET` request for the associated Identity Verification attempt. A new expiring URL is generated with each request, so you can always rerequest the Identity Verification attempt if one of your URLs expires.
    """

    cropped_back: typing.Optional[DocumentImageCroppedBack] = None
    cropped_front: typing.Optional[DocumentImageCroppedFront] = None
    face: typing.Optional[DocumentImageFace] = None
    original_back: typing.Optional[DocumentImageBack] = None
    original_front: typing.Optional[DocumentImageFront] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
