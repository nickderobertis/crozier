

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentFileAttachment(UniversalBaseModel):
    """
    Response model for agent file attachments showing file status in agent context
    """

    id: str = pydantic.Field()
    """
    Unique identifier of the file-agent relationship
    """

    file_id: str = pydantic.Field()
    """
    Unique identifier of the file
    """

    file_name: str = pydantic.Field()
    """
    Name of the file
    """

    folder_id: str = pydantic.Field()
    """
    Unique identifier of the folder/source
    """

    folder_name: str = pydantic.Field()
    """
    Name of the folder/source
    """

    is_open: bool = pydantic.Field()
    """
    Whether the file is currently open in the agent's context
    """

    last_accessed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp of last access by the agent
    """

    visible_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Portion of the file visible to the agent if open
    """

    start_line: typing.Optional[int] = pydantic.Field(default=None)
    """
    Starting line number if file was opened with line range
    """

    end_line: typing.Optional[int] = pydantic.Field(default=None)
    """
    Ending line number if file was opened with line range
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
