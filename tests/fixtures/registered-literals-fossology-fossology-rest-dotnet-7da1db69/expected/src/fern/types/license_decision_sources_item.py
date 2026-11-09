

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LicenseDecisionSourcesItem(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the agent.
    """

    clearing_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="clearingId"),
        pydantic.Field(alias="clearingId", description="The clearing ID."),
    ] = None
    """
    The clearing ID.
    """

    agent_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="agentId"),
        pydantic.Field(alias="agentId", description="The agent ID."),
    ] = None
    """
    The agent ID.
    """

    highlight_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="highlightId"),
        pydantic.Field(alias="highlightId", description="The highlight ID."),
    ] = None
    """
    The highlight ID.
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    The page number.
    """

    percentage: typing.Optional[int] = pydantic.Field(default=None)
    """
    The percentage value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
