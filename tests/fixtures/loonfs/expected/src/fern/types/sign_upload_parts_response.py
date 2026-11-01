

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId
from .signed_upload_part import SignedUploadPart
from .upload_id import UploadId


class SignUploadPartsResponse(UniversalBaseModel):
    """
    One capability for each requested part.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the upload session belongs to.
    """

    parts: typing.List[SignedUploadPart] = pydantic.Field()
    """
    The capabilities, in the order that the request asked for them.
    """

    upload_id: UploadId = pydantic.Field()
    """
    The session that the parts belong to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
