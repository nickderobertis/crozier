

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesListTemplateVersionsResponseVersionsItem(UniversalBaseModel):
    version: str = pydantic.Field()
    """
    The version number
    """

    created_at: str = pydantic.Field()
    """
    When the version was created
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version description message
    """

    is_latest: bool = pydantic.Field()
    """
    Whether this is the latest version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
