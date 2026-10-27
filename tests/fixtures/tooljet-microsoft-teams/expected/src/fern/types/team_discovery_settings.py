

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TeamDiscoverySettings(UniversalBaseModel):
    show_in_teams_search_and_suggestions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="showInTeamsSearchAndSuggestions"),
        pydantic.Field(alias="showInTeamsSearchAndSuggestions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
