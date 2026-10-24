

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateSingleMessageResponseRecipient(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Display name for the recipient
    """

    email: str = pydantic.Field()
    """
    Recipient email address
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
