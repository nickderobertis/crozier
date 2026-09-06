

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .published_file_author_snapshot import PublishedFileAuthorSnapshot
from .published_file_details_child import PublishedFileDetailsChild
from .published_file_details_for_sale_data import PublishedFileDetailsForSaleData
from .published_file_details_kv_tag import PublishedFileDetailsKvTag
from .published_file_details_playtime_stats import PublishedFileDetailsPlaytimeStats
from .published_file_details_preview import PublishedFileDetailsPreview
from .published_file_details_reaction import PublishedFileDetailsReaction
from .published_file_details_tag import PublishedFileDetailsTag
from .published_file_details_vote_data import PublishedFileDetailsVoteData


class PublishedFileDetails(UniversalBaseModel):
    app_name: typing.Optional[str] = None
    author_snapshots: typing.Optional[typing.List[PublishedFileAuthorSnapshot]] = None
    available_revisions: typing.Optional[typing.List[int]] = None
    ban_reason: typing.Optional[str] = None
    ban_text_check_result: typing.Optional[int] = None
    banned: typing.Optional[bool] = None
    banner: typing.Optional[int] = None
    can_be_deleted: typing.Optional[bool] = None
    can_subscribe: typing.Optional[bool] = None
    children: typing.Optional[typing.List[PublishedFileDetailsChild]] = None
    consumer_appid: typing.Optional[int] = None
    consumer_shortcutid: typing.Optional[int] = None
    content_descriptorids: typing.Optional[typing.List[int]] = None
    creator: typing.Optional[int] = None
    creator_appid: typing.Optional[int] = None
    external_asset_id: typing.Optional[int] = None
    favorited: typing.Optional[int] = None
    file_description: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    file_type: typing.Optional[int] = None
    file_url: typing.Optional[str] = None
    filename: typing.Optional[str] = None
    flags: typing.Optional[int] = None
    followers: typing.Optional[int] = None
    for_sale_data: typing.Optional[PublishedFileDetailsForSaleData] = None
    hcontent_file: typing.Optional[int] = None
    hcontent_preview: typing.Optional[int] = None
    image_height: typing.Optional[int] = None
    image_url: typing.Optional[str] = None
    image_width: typing.Optional[int] = None
    incompatible: typing.Optional[bool] = None
    kvtags: typing.Optional[typing.List[PublishedFileDetailsKvTag]] = None
    language: typing.Optional[int] = None
    lifetime_favorited: typing.Optional[int] = None
    lifetime_followers: typing.Optional[int] = None
    lifetime_playtime: typing.Optional[int] = None
    lifetime_playtime_sessions: typing.Optional[int] = None
    lifetime_subscriptions: typing.Optional[int] = None
    maybe_inappropriate_sex: typing.Optional[bool] = None
    maybe_inappropriate_violence: typing.Optional[bool] = None
    metadata: typing.Optional[str] = None
    num_children: typing.Optional[int] = None
    num_comments_developer: typing.Optional[int] = None
    num_comments_public: typing.Optional[int] = None
    num_reports: typing.Optional[int] = None
    playtime_stats: typing.Optional[PublishedFileDetailsPlaytimeStats] = None
    preview_file_size: typing.Optional[int] = None
    preview_url: typing.Optional[str] = None
    previews: typing.Optional[typing.List[PublishedFileDetailsPreview]] = None
    publishedfileid: typing.Optional[int] = None
    reactions: typing.Optional[typing.List[PublishedFileDetailsReaction]] = None
    result: typing.Optional[int] = None
    revision: typing.Optional[int] = None
    revision_change_number: typing.Optional[int] = None
    search_score: typing.Optional[float] = None
    short_description: typing.Optional[str] = None
    shortcutid: typing.Optional[int] = None
    shortcutname: typing.Optional[str] = None
    show_subscribe_all: typing.Optional[bool] = None
    spoiler_tag: typing.Optional[bool] = None
    subscriptions: typing.Optional[int] = None
    tags: typing.Optional[typing.List[PublishedFileDetailsTag]] = None
    time_created: typing.Optional[int] = None
    time_subscribed: typing.Optional[int] = None
    time_updated: typing.Optional[int] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None
    views: typing.Optional[int] = None
    visibility: typing.Optional[int] = None
    vote_data: typing.Optional[PublishedFileDetailsVoteData] = None
    workshop_accepted: typing.Optional[bool] = None
    workshop_file: typing.Optional[bool] = None
    youtubevideoid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
