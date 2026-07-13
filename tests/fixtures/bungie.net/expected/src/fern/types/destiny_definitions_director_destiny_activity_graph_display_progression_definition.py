

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition(UniversalBaseModel):
    """
    When a Graph needs to show active Progressions, this defines those objectives as well as an identifier.
    """

    id: typing.Optional[int] = None
    progression_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="progressionHash")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
