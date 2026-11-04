

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreTranslationApiLanguages200ResponseOcsDataLanguagesInner(UniversalBaseModel):
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    from_label: typing_extensions.Annotated[str, FieldMetadata(alias="fromLabel"), pydantic.Field(alias="fromLabel")]
    to: str
    to_label: typing_extensions.Annotated[str, FieldMetadata(alias="toLabel"), pydantic.Field(alias="toLabel")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
