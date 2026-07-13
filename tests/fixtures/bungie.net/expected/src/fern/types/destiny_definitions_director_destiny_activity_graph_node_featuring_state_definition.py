

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition(UniversalBaseModel):
    """
    Nodes can have different visual states. This object represents a single visual state ("highlight type") that a node can be in, and the unlock expression condition to determine whether it should be set.
    """

    highlight_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="highlightType")] = (
        pydantic.Field(default=None)
    )
    """
    The node can be highlighted in a variety of ways - the game iterates through these and finds the first FeaturingState that is valid at the present moment given the Game, Account, and Character state, and renders the node in that state. See the ActivityGraphNodeHighlightType enum for possible values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
