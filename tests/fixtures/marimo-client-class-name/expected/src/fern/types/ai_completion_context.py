

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ai_completion_context_variables_item import AiCompletionContextVariablesItem
from .schema_table import SchemaTable


class AiCompletionContext(UniversalBaseModel):
    plain_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="plainText"), pydantic.Field(alias="plainText")
    ] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.List[SchemaTable]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    variables: typing.Optional[typing.List[AiCompletionContextVariablesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
