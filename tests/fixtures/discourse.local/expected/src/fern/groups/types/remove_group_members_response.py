

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemoveGroupMembersResponse(UniversalBaseModel):
    skipped_usernames: typing.List[typing.Optional[typing.Any]]
    success: str
    usernames: typing.List[typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
