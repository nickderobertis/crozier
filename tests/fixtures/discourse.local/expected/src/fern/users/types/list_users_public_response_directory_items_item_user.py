

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListUsersPublicResponseDirectoryItemsItemUser(UniversalBaseModel):
    avatar_template: str
    id: int
    name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
