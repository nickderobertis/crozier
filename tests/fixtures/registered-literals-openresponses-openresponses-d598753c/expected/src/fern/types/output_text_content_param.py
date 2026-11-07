

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .url_citation_param import UrlCitationParam


class OutputTextContentParam(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The text content.
    """

    annotations: typing.Optional[typing.List[UrlCitationParam]] = pydantic.Field(default=None)
    """
    Citations associated with the text content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
