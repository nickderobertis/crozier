

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateGroupRequestGroup(UniversalBaseModel):
    automatic_membership_email_domains: typing.Optional[str] = pydantic.Field(default=None)
    """
    pipe|separated
    """

    bio_raw: typing.Optional[str] = pydantic.Field(default=None)
    """
    About Group
    """

    default_notification_level: typing.Optional[int] = None
    flair_bg_color: typing.Optional[str] = None
    flair_icon: typing.Optional[str] = None
    flair_upload_id: typing.Optional[int] = None
    full_name: typing.Optional[str] = None
    muted_category_ids: typing.Optional[typing.List[int]] = None
    name: str
    owner_usernames: typing.Optional[str] = pydantic.Field(default=None)
    """
    comma,separated
    """

    primary_group: typing.Optional[bool] = None
    public_admission: typing.Optional[bool] = None
    public_exit: typing.Optional[bool] = None
    regular_category_ids: typing.Optional[typing.List[int]] = None
    tracking_category_ids: typing.Optional[typing.List[int]] = None
    usernames: typing.Optional[str] = pydantic.Field(default=None)
    """
    comma,separated
    """

    visibility_level: typing.Optional[int] = None
    watching_category_ids: typing.Optional[typing.List[int]] = None
    watching_first_post_category_ids: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
