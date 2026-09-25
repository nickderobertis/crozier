

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemAttachmentAttachment(UniversalBaseModel):
    """
    Dictionary containing the ID of the deleted attachment.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the deleted attachment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
