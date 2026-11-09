

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TreeViewModelLicenseListItemAgentsItem(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the agent.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the agent.
    """

    match_percentage: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="matchPercentage"),
        pydantic.Field(alias="matchPercentage", description="The match percentage of the agent."),
    ] = None
    """
    The match percentage of the agent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
