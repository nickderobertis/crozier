

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.article import Article
from ...types.content_pro_company import ContentProCompany
from ...types.content_pro_snippets import ContentProSnippets


class GetContentproSearchResponseDataItem(UniversalBaseModel):
    article: typing.Optional[Article] = None
    company: typing.Optional[ContentProCompany] = None
    snippets: typing.Optional[ContentProSnippets] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
