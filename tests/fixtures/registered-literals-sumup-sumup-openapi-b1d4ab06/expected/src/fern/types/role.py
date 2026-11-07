

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metadata import Metadata


class Role(UniversalBaseModel):
    """
    A custom role that can be used to assign set of permissions to members.
    """

    id: str = pydantic.Field()
    """
    Unique identifier of the role.
    """

    name: str = pydantic.Field()
    """
    User-defined name of the role.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-defined description of the role.
    """

    permissions: typing.List[str] = pydantic.Field()
    """
    List of permission granted by this role.
    """

    is_predefined: bool = pydantic.Field()
    """
    True if the role is provided by SumUp.
    """

    metadata: typing.Optional[Metadata] = None
    created_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the role was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the role was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
