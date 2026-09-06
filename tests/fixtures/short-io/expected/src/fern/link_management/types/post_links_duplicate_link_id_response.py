

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_links_duplicate_link_id_response_expires_at import PostLinksDuplicateLinkIdResponseExpiresAt
from .post_links_duplicate_link_id_response_redirect_type import PostLinksDuplicateLinkIdResponseRedirectType
from .post_links_duplicate_link_id_response_source import PostLinksDuplicateLinkIdResponseSource
from .post_links_duplicate_link_id_response_split_urlv2item import PostLinksDuplicateLinkIdResponseSplitUrlv2Item
from .post_links_duplicate_link_id_response_ttl import PostLinksDuplicateLinkIdResponseTtl
from .post_links_duplicate_link_id_response_user import PostLinksDuplicateLinkIdResponseUser


class PostLinksDuplicateLinkIdResponse(UniversalBaseModel):
    original_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalURL"), pydantic.Field(alias="originalURL", description="Original URL")
    ]
    """
    Original URL
    """

    cloaking: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Cloaking
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link password
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[PostLinksDuplicateLinkIdResponseExpiresAt],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="Link expiration date in milliseconds or ISO string"),
    ] = None
    """
    Link expiration date in milliseconds or ISO string
    """

    expired_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expiredURL"),
        pydantic.Field(alias="expiredURL", description="Expired URL"),
    ] = None
    """
    Expired URL
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link title
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array of link tags
    """

    utm_source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmSource"),
        pydantic.Field(alias="utmSource", description="set utm_source parameter to destination link"),
    ] = None
    """
    set utm_source parameter to destination link
    """

    utm_medium: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmMedium"),
        pydantic.Field(alias="utmMedium", description="set utm_medium parameter to destination link"),
    ] = None
    """
    set utm_medium parameter to destination link
    """

    utm_campaign: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmCampaign"),
        pydantic.Field(alias="utmCampaign", description="set utm_campaign parameter to destination link"),
    ] = None
    """
    set utm_campaign parameter to destination link
    """

    utm_term: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmTerm"),
        pydantic.Field(alias="utmTerm", description="set utm_term parameter to destination link"),
    ] = None
    """
    set utm_term parameter to destination link
    """

    utm_content: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmContent"),
        pydantic.Field(alias="utmContent", description="set utm_content parameter to destination link"),
    ] = None
    """
    set utm_content parameter to destination link
    """

    ttl: typing.Optional[PostLinksDuplicateLinkIdResponseTtl] = pydantic.Field(default=None)
    """
    Time to live in milliseconds or ISO string
    """

    android_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="androidURL"),
        pydantic.Field(alias="androidURL", description="Android URL"),
    ] = None
    """
    Android URL
    """

    iphone_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iphoneURL"),
        pydantic.Field(alias="iphoneURL", description="iPhone URL"),
    ] = None
    """
    iPhone URL
    """

    clicks_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="clicksLimit"),
        pydantic.Field(alias="clicksLimit", description="disable link after specified number of clicks"),
    ] = None
    """
    disable link after specified number of clicks
    """

    password_contact: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="passwordContact"),
        pydantic.Field(alias="passwordContact", description="Provide your email to users to get a password"),
    ] = None
    """
    Provide your email to users to get a password
    """

    skip_qs: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="skipQS"),
        pydantic.Field(alias="skipQS", description="Skip query string merging"),
    ] = None
    """
    Skip query string merging
    """

    archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Link is archived
    """

    split_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="splitURL"), pydantic.Field(alias="splitURL", description="Split URL")
    ] = None
    """
    Split URL
    """

    split_percent: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="splitPercent"),
        pydantic.Field(alias="splitPercent", description="Split URL percentage"),
    ] = None
    """
    Split URL percentage
    """

    split_urlv2: typing_extensions.Annotated[
        typing.Optional[typing.List[PostLinksDuplicateLinkIdResponseSplitUrlv2Item]],
        FieldMetadata(alias="splitURLV2"),
        pydantic.Field(alias="splitURLV2", description="Split URL configurations for multi-way A/B testing"),
    ] = None
    """
    Split URL configurations for multi-way A/B testing
    """

    integration_adroll: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrationAdroll"),
        pydantic.Field(alias="integrationAdroll", description="Adroll integration"),
    ] = None
    """
    Adroll integration
    """

    integration_fb: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrationFB"),
        pydantic.Field(alias="integrationFB", description="Facebook integration"),
    ] = None
    """
    Facebook integration
    """

    integration_tt: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrationTT"),
        pydantic.Field(alias="integrationTT", description="TikTok integration"),
    ] = None
    """
    TikTok integration
    """

    integration_ga: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrationGA"),
        pydantic.Field(alias="integrationGA", description="Google Analytics integration"),
    ] = None
    """
    Google Analytics integration
    """

    integration_gtm: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrationGTM"),
        pydantic.Field(alias="integrationGTM", description="Google Tag Manager integration"),
    ] = None
    """
    Google Tag Manager integration
    """

    id_string: typing_extensions.Annotated[
        str, FieldMetadata(alias="idString"), pydantic.Field(alias="idString", description="Link ID")
    ]
    """
    Link ID
    """

    id: str = pydantic.Field()
    """
    Link ID
    """

    short_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="shortURL"), pydantic.Field(alias="shortURL", description="Short URL")
    ]
    """
    Short URL
    """

    secure_short_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="secureShortURL"),
        pydantic.Field(alias="secureShortURL", description="Secure short URL"),
    ]
    """
    Secure short URL
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link slug. For case-insensitive domains, this is the normalized lowercase version of the path.
    """

    display_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayPath"),
        pydantic.Field(
            alias="displayPath",
            description="Original path preserving the case as provided during creation. Set only for case-insensitive domains when the path contains uppercase characters, otherwise null.",
        ),
    ] = None
    """
    Original path preserving the case as provided during creation. Set only for case-insensitive domains when the path contains uppercase characters, otherwise null.
    """

    redirect_type: typing_extensions.Annotated[
        typing.Optional[PostLinksDuplicateLinkIdResponseRedirectType],
        FieldMetadata(alias="redirectType"),
        pydantic.Field(alias="redirectType", description="HTTP code for redirect"),
    ] = None
    """
    HTTP code for redirect
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Link creation date in ISO format"),
    ] = None
    """
    Link creation date in ISO format
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Link last update date in ISO format"),
    ] = None
    """
    Link last update date in ISO format
    """

    folder_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="FolderId"), pydantic.Field(alias="FolderId", description="Folder ID")
    ] = None
    """
    Folder ID
    """

    domain_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="DomainId"), pydantic.Field(alias="DomainId", description="Domain ID")
    ] = None
    """
    Domain ID
    """

    owner_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="OwnerId"), pydantic.Field(alias="OwnerId", description="Owner ID")
    ] = None
    """
    Owner ID
    """

    has_password: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasPassword"),
        pydantic.Field(alias="hasPassword", description="Link has password"),
    ] = None
    """
    Link has password
    """

    source: typing.Optional[PostLinksDuplicateLinkIdResponseSource] = pydantic.Field(default=None)
    """
    Link source
    """

    user: typing_extensions.Annotated[
        typing.Optional[PostLinksDuplicateLinkIdResponseUser], FieldMetadata(alias="User"), pydantic.Field(alias="User")
    ] = None
    success: typing.Optional[bool] = None
    duplicate: typing.Optional[bool] = None
    duplicated_from: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="duplicatedFrom"),
        pydantic.Field(alias="duplicatedFrom", description="Original link's idString"),
    ]
    """
    Original link's idString
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
