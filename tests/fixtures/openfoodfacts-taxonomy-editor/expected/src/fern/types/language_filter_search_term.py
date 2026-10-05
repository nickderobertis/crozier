

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LanguageFilterSearchTerm(UniversalBaseModel):
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]
    negated: typing.Optional[bool] = None
    language: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
