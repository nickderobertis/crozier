

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class CreateScriptResponse(UniversalBaseModel):
    script_id: str = pydantic.Field()
    """
    Unique script identifier
    """

    version: int = pydantic.Field()
    """
    Script version number
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the workflow run or task run that generated this script
    """

    file_count: int = pydantic.Field()
    """
    Total number of files in the script
    """

    file_tree: typing.Dict[str, "FileNode"] = pydantic.Field()
    """
    Hierarchical file tree structure
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the script was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .file_node import FileNode

update_forward_refs(CreateScriptResponse, FileNode=FileNode)
