

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ToolInfo(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Tool name
    """

    description: str = pydantic.Field()
    """
    Tool description
    """

    schema_: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Tool input schema"),
    ]
    """
    Tool input schema
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tool category
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tool tags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
