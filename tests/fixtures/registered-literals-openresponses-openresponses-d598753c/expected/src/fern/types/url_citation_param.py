

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .url_citation_param_type import UrlCitationParamType


class UrlCitationParam(UniversalBaseModel):
    type: UrlCitationParamType = pydantic.Field()
    """
    The citation type. Always `url_citation`.
    """

    start_index: int = pydantic.Field()
    """
    The index of the first character of the citation in the message.
    """

    end_index: int = pydantic.Field()
    """
    The index of the last character of the citation in the message.
    """

    url: str = pydantic.Field()
    """
    The URL of the cited resource.
    """

    title: str = pydantic.Field()
    """
    The title of the cited resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
