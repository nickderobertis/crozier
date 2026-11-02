

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collector_any import CollectorAny
from .collector_note import CollectorNote
from .label_translations import LabelTranslations


class Specimen(UniversalBaseModel):
    labels: typing.Optional[LabelTranslations] = None
    note: typing.Optional[CollectorNote] = None
    loose: typing.Optional[CollectorAny] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
