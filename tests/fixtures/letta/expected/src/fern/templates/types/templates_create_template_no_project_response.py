

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesCreateTemplateNoProjectResponse(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The exact name of the template
    """

    id: str
    project_id: str
    project_slug: str
    latest_version: str = pydantic.Field()
    """
    The latest version of the template
    """

    description: typing.Optional[str] = None
    template_deployment_slug: str = pydantic.Field()
    """
    The full name of the template, including version and project slug
    """

    updated_at: str = pydantic.Field()
    """
    When the template was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
