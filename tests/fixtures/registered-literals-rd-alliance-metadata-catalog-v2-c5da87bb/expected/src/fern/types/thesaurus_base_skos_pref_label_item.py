

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ThesaurusBaseSkosPrefLabelItem(UniversalBaseModel):
    value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@value"), pydantic.Field(alias="@value")
    ] = None
    language: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@language"), pydantic.Field(alias="@language")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
