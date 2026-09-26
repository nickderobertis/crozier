

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class User(UniversalBaseModel):
    """
    User.
    """

    id: str
    username: str
    name: str
    first_name: str
    last_name: str
    email: str
    groups: typing.Optional[typing.List[str]] = None
    school_ids: typing.Optional[typing.List[str]] = None
    is_active: bool
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
