

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .id import Id
from .photo_url import PhotoUrl
from .updated_at import UpdatedAt


class CollectionUser(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    email: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    id: typing.Optional[Id] = None
    last_name: typing.Optional[str] = None
    name: typing.Optional[str] = None
    photo_url: typing.Optional[PhotoUrl] = None
    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
