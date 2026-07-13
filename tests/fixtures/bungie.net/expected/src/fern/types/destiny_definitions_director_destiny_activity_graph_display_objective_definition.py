

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition(UniversalBaseModel):
    """
    When a Graph needs to show active Objectives, this defines those objectives as well as an identifier.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    $NOTE $amola 2017-01-19 This field is apparently something that CUI uses to manually wire up objectives to display info. I am unsure how it works.
    """

    objective_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="objectiveHash")] = (
        pydantic.Field(default=None)
    )
    """
    The objective being shown on the map.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
