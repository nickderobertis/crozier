

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BlockResponse(UniversalBaseModel):
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
    (Deprecated) The name of the block template (if it is a template).
    """

    is_template: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the block is a template (e.g. saved human/persona options).
    """

    template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    (Deprecated) The id of the template.
    """

    base_template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    (Deprecated) The base template id of the block.
    """

    deployment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    (Deprecated) The id of the deployment.
    """

    entity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    (Deprecated) The id of the entity within the template.
    """

    preserve_on_migration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    (Deprecated) Preserve the block on template migration.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label of the block (e.g. 'human', 'persona') in the context window.
    """

    read_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    (Deprecated) Whether the agent has read-only access to the block.
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
    (Deprecated) If set to True, the block will be hidden.
    """

    id: str = pydantic.Field()
    """
    The id of the block.
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
