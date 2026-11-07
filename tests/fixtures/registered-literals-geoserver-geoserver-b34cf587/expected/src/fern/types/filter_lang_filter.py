

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filter_lang import FilterLang


class FilterLangFilter(UniversalBaseModel):
    filter_lang: typing_extensions.Annotated[
        typing.Optional[FilterLang], FieldMetadata(alias="filterLang"), pydantic.Field(alias="filterLang")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
