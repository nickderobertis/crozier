

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Space(UniversalBaseModel):
    id: int
    mount_point: str
    groups: typing.List[typing.Dict[str, typing.Any]]
    quota: int
    size: int
    acl: bool
    manage: typing.List[typing.Dict[str, typing.Any]]
    groupfolder_id: int
    name: str
    color_code: str
    users_count: typing_extensions.Annotated[int, FieldMetadata(alias="usersCount"), pydantic.Field(alias="usersCount")]
    added_groups: typing.List[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
