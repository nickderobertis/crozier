

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgentSkill(UniversalBaseModel):
    """
    Represents a distinct capability or function that an agent can perform.
    """

    description: str
    examples: typing.Optional[typing.List[str]] = None
    id: str
    input_modes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="inputModes"), pydantic.Field(alias="inputModes")
    ] = None
    name: str
    output_modes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="outputModes"), pydantic.Field(alias="outputModes")
    ] = None
    security: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]] = None
    tags: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
