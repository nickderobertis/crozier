

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation(UniversalBaseModel):
    file_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the specific File the citation is from.
    """

    quote: typing.Optional[str] = pydantic.Field(default=None)
    """
    The specific quote in the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
