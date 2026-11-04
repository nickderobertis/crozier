

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_create_new_context_request_owner_id_type import ContextCreateNewContextRequestOwnerIdType


class ContextCreateNewContextRequestOwnerId(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique ID of the owner of the context. Specify either this or slug.
    """

    type: typing.Optional[ContextCreateNewContextRequestOwnerIdType] = pydantic.Field(default=None)
    """
    The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
