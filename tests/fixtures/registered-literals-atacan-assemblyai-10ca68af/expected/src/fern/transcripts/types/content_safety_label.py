

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContentSafetyLabel(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    The label of the sensitive topic
    """

    confidence: float = pydantic.Field()
    """
    The confidence score for the topic being discussed, from 0 to 1
    """

    severity: float = pydantic.Field()
    """
    How severely the topic is discussed in the section, from 0 to 1
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
