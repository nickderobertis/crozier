

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileBlock(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    Value of the block.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Character limit of the block.
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The associated project id.
    """

    template_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the block if it is a template.
    """

    is_template: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the block is a template (e.g. saved human/persona options).
    """

    template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the template.
    """

    base_template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The base template id of the block.
    """

    deployment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the deployment.
    """

    entity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the entity within the template.
    """

    preserve_on_migration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Preserve the block on template migration.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label of the block (e.g. 'human', 'persona') in the context window.
    """

    read_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the agent has read-only access to the block.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the block.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Metadata of the block.
    """

    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to True, the block will be hidden.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Block
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this Block.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that last updated this Block.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags associated with the block.
    """

    file_id: str = pydantic.Field()
    """
    Unique identifier of the file.
    """

    source_id: str = pydantic.Field()
    """
    Deprecated: Use `folder_id` field instead. Unique identifier of the source.
    """

    is_open: bool = pydantic.Field()
    """
    True if the agent currently has the file open.
    """

    last_accessed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    UTC timestamp of the agent’s most recent access to this file. Any operations from the open, close, or search tools will update this field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
