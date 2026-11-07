

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .template_descriptor import TemplateDescriptor


class CustomTemplates(UniversalBaseModel):
    """
    Custom template descriptors grouped by the content type they render.
    """

    category: typing.Optional[typing.List[TemplateDescriptor]] = pydantic.Field(default=None)
    """
    Custom templates available for categories.
    """

    page: typing.Optional[typing.List[TemplateDescriptor]] = pydantic.Field(default=None)
    """
    Custom templates available for single pages.
    """

    post: typing.Optional[typing.List[TemplateDescriptor]] = pydantic.Field(default=None)
    """
    Custom templates available for posts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
