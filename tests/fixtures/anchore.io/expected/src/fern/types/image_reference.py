

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tag_entry import TagEntry


class ImageReference(UniversalBaseModel):
    """
    A summary of an image identity, including digest, id (if available), and any tags known to have ever been mapped to the digest
    """

    analyzed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timestamp, in rfc3339 format, indicating when the image state became 'analyzed' in Anchore Engine.
    """

    digest: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image digest
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image id if available
    """

    tag_history: typing.Optional[typing.List[TagEntry]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
