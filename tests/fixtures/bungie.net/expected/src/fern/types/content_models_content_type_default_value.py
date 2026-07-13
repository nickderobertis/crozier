

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentModelsContentTypeDefaultValue(UniversalBaseModel):
    default_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="defaultValue")] = None
    when_clause: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="whenClause")] = None
    when_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="whenValue")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
