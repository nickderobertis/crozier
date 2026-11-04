

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class CreateProjectResponse(UniversalBaseModel):
    project_id: str = pydantic.Field()
    """
    Unique project identifier
    """

    version: int = pydantic.Field()
    """
    Project version number
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the workflow run or task run that generated this project
    """

    file_count: int = pydantic.Field()
    """
    Total number of files in the project
    """

    file_tree: typing.Dict[str, "FileNode"] = pydantic.Field()
    """
    Hierarchical file tree structure
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the project was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .file_node import FileNode

update_forward_refs(CreateProjectResponse, FileNode=FileNode)
