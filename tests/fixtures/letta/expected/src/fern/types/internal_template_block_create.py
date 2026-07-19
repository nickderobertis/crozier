

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InternalTemplateBlockCreate(UniversalBaseModel):
    """
    Used for Letta Cloud
    """

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

    is_template: typing.Optional[bool] = None
    template_id: str = pydantic.Field()
    """
    The id of the template.
    """

    base_template_id: str = pydantic.Field()
    """
    The id of the base template.
    """

    deployment_id: str = pydantic.Field()
    """
    The id of the deployment.
    """

    entity_id: str = pydantic.Field()
    """
    The id of the entity within the template.
    """

    preserve_on_migration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Preserve the block on template migration.
    """

    label: str = pydantic.Field()
    """
    Label of the block.
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

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags to associate with the block.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
