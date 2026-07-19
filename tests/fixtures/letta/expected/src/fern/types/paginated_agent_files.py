

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_file_attachment import AgentFileAttachment


class PaginatedAgentFiles(UniversalBaseModel):
    """
    Paginated response for agent files
    """

    files: typing.List[AgentFileAttachment] = pydantic.Field()
    """
    List of file attachments for the agent
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor for fetching the next page (file-agent relationship ID)
    """

    has_more: bool = pydantic.Field()
    """
    Whether more results exist after this page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
