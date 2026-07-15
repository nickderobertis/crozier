

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .id import Id
from .updated_at import UpdatedAt


class EcommerceStore(UniversalBaseModel):
    admin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The store's admin login URL
    """

    created_at: typing.Optional[CreatedAt] = None
    id: typing.Optional[Id] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The store's name
    """

    store_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The store's website URL
    """

    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
