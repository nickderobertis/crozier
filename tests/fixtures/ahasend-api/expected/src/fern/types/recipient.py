

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Recipient(UniversalBaseModel):
    email: str = pydantic.Field()
    """
    Recipient email address
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name for the recipient
    """

    substitutions: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Substitution data for the recipient. Used with jinja2 templating language for dynamic content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
