

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .id import Id
from .updated_at import UpdatedAt


class Collection(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the collection
    """

    id: typing.Optional[Id] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the collection
    """

    parent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The collections's parent ID
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The collections's type
    """

    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
