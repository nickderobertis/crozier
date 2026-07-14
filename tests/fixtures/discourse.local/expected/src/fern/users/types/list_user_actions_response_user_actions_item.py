

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListUserActionsResponseUserActionsItem(UniversalBaseModel):
    acting_avatar_template: str
    acting_name: typing.Optional[str] = None
    acting_user_id: int
    acting_username: str
    action_code: typing.Optional[str] = None
    action_type: int
    archived: bool
    avatar_template: str
    category_id: int
    closed: bool
    created_at: str
    deleted: bool
    excerpt: str
    hidden: typing.Optional[str] = None
    name: typing.Optional[str] = None
    post_id: typing.Optional[str] = None
    post_number: int
    post_type: typing.Optional[str] = None
    slug: str
    target_name: typing.Optional[str] = None
    target_user_id: int
    target_username: str
    title: str
    topic_id: int
    user_id: int
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
