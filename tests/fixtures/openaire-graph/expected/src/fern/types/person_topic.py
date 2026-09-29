

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PersonTopic(UniversalBaseModel):
    value: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    from_year: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fromYear"), pydantic.Field(alias="fromYear")
    ] = None
    to_year: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="toYear"), pydantic.Field(alias="toYear")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
