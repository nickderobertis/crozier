

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_schema_manager_config import GroupSchemaManagerConfig


class GroupSchema(UniversalBaseModel):
    """
    Group with human-readable ID for agent file
    """

    agent_ids: typing.List[str] = pydantic.Field()
    """
    
    """

    description: str = pydantic.Field()
    """
    
    """

    manager_config: typing.Optional[GroupSchemaManagerConfig] = pydantic.Field(default=None)
    """
    
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The associated project id.
    """

    shared_block_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    
    """

    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to True, the group will be hidden.
    """

    id: str = pydantic.Field()
    """
    Human-readable identifier for this group in the file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
