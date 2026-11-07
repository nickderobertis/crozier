

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_addons_read_response_attributes import UsersAddonsReadResponseAttributes
from .users_addons_read_response_links import UsersAddonsReadResponseLinks


class UsersAddonsReadResponse(UniversalBaseModel):
    attributes: typing.Optional[UsersAddonsReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the user addon entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the user addon entity.
    """

    links: typing.Optional[UsersAddonsReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the user addon entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the user addon entity (`user_addons`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
