

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .id import Id
from .updated_at import UpdatedAt


class CollectionTicketComment(UniversalBaseModel):
    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    Body of the comment
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    id: typing.Optional[Id] = None
    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
