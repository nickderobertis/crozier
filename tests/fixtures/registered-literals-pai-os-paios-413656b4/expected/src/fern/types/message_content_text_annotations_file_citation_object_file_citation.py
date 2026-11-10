

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageContentTextAnnotationsFileCitationObjectFileCitation(UniversalBaseModel):
    file_id: str = pydantic.Field()
    """
    The ID of the specific File the citation is from.
    """

    quote: str = pydantic.Field()
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
