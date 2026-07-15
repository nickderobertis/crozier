

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .description import Description
from .id import Id
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class DriveGroup(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    description: typing.Optional[Description] = None
    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of the drive group
    """

    id: typing.Optional[Id] = None
    name: str = pydantic.Field()
    """
    The name of the drive group
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
