

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheme_slot import SchemeSlot
from .scheme_summary_locale import SchemeSummaryLocale
from .scheme_summary_source import SchemeSummarySource


class SchemeSummary(UniversalBaseModel):
    description: typing.Optional[str] = None
    editable: typing.Optional[bool] = None
    enabled: typing.Optional[bool] = None
    id: str
    locale: SchemeSummaryLocale
    name: str
    slots: typing.List[SchemeSlot]
    source: typing.Optional[SchemeSummarySource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
