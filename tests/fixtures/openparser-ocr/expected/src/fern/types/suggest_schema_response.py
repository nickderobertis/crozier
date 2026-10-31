

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SuggestSchemaResponse(UniversalBaseModel):
    """
    Suggested extraction schema returned directly without creating a durable job.
    """

    name: str = pydantic.Field()
    """
    Short document-type label proposed by the model.
    """

    schema_: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="schema"),
        pydantic.Field(
            alias="schema", description="Canonical JSON Schema object ready for extract and manual editing."
        ),
    ]
    """
    Canonical JSON Schema object ready for extract and manual editing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
