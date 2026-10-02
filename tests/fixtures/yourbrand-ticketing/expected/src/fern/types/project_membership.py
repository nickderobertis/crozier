

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project import Project
from .user import User


class ProjectMembership(UniversalBaseModel):
    id: typing.Optional[str] = None
    project: typing.Optional[Project] = None
    user: typing.Optional[User] = None
    from_: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    thru: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
