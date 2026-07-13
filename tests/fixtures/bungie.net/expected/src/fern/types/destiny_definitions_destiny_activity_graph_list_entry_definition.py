

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityGraphListEntryDefinition(UniversalBaseModel):
    """
    Destinations and Activities may have default Activity Graphs that should be shown when you bring up the Director and are playing in either.
    This contract defines the graph referred to and the gating for when it is relevant.
    """

    activity_graph_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityGraphHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of the DestinyActivityGraphDefinition that should be shown when opening the director.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
