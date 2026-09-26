

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .template_summary_category import TemplateSummaryCategory
from .template_summary_locale import TemplateSummaryLocale
from .template_summary_source import TemplateSummarySource


class TemplateSummary(UniversalBaseModel):
    category: TemplateSummaryCategory
    copyable: typing.Optional[bool] = None
    defaults: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    description: typing.Optional[str] = None
    editable: typing.Optional[bool] = None
    enabled: typing.Optional[bool] = None
    examples: typing.Optional[typing.List[str]] = None
    id: str
    locale: TemplateSummaryLocale
    name: str
    name_en: typing.Optional[str] = None
    prompt_template: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    source: typing.Optional[TemplateSummarySource] = None
    tags: typing.List[str]
    thumbnail_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
