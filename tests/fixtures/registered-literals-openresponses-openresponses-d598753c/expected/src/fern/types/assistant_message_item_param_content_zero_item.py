

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .url_citation_param import UrlCitationParam


class AssistantMessageItemParamContentZeroItem_OutputText(UniversalBaseModel):
    """
    A piece of assistant message content, such as text or a refusal.
    """

    type: typing.Literal["output_text"] = "output_text"
    text: str
    annotations: typing.Optional[typing.List[UrlCitationParam]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssistantMessageItemParamContentZeroItem_Refusal(UniversalBaseModel):
    """
    A piece of assistant message content, such as text or a refusal.
    """

    type: typing.Literal["refusal"] = "refusal"
    refusal: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssistantMessageItemParamContentZeroItem = typing_extensions.Annotated[
    typing.Union[AssistantMessageItemParamContentZeroItem_OutputText, AssistantMessageItemParamContentZeroItem_Refusal],
    pydantic.Field(discriminator="type"),
]
