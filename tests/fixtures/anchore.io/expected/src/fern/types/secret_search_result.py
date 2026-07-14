

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .regex_content_match import RegexContentMatch


class SecretSearchResult(UniversalBaseModel):
    """
    The retrieved file entry including content (b64 encoded)
    """

    matches: typing.Optional[typing.List[RegexContentMatch]] = None
    path: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
