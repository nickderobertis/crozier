

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .url_citation_body_type import UrlCitationBodyType


class UrlCitationBody(UniversalBaseModel):
    """
    A citation for a web resource used to generate a model response.
    """

    type: UrlCitationBodyType = pydantic.Field()
    """
    The type of the URL citation. Always `url_citation`.
    """

    url: str = pydantic.Field()
    """
    The URL of the web resource.
    """

    start_index: int = pydantic.Field()
    """
    The index of the first character of the URL citation in the message.
    """

    end_index: int = pydantic.Field()
    """
    The index of the last character of the URL citation in the message.
    """

    title: str = pydantic.Field()
    """
    The title of the web resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
