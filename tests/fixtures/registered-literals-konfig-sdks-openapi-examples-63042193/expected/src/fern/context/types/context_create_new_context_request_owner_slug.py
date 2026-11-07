

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_create_new_context_request_owner_slug_type import ContextCreateNewContextRequestOwnerSlugType


class ContextCreateNewContextRequestOwnerSlug(UniversalBaseModel):
    slug: str = pydantic.Field()
    """
    A string that represents an organization. Specify either this or id. Cannot be used for accounts.
    """

    type: typing.Optional[ContextCreateNewContextRequestOwnerSlugType] = pydantic.Field(default=None)
    """
    The type of owner. Defaults to "organization". Accounts are only used as context owners in server and must be specified by an id instead of a slug.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
