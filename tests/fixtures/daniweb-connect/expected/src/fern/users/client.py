

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_users import EndpointGetUsers
from ..types.endpoint_get_users_id import EndpointGetUsersId
from ..types.endpoint_get_users_id_groups import EndpointGetUsersIdGroups
from ..types.endpoint_get_users_id_groups_messages import EndpointGetUsersIdGroupsMessages
from ..types.endpoint_get_users_id_metadata import EndpointGetUsersIdMetadata
from ..types.endpoint_get_users_id_metadata_collections import EndpointGetUsersIdMetadataCollections
from ..types.endpoint_get_users_id_positions import EndpointGetUsersIdPositions
from ..types.endpoint_get_users_id_synergies import EndpointGetUsersIdSynergies
from ..types.endpoint_get_users_nearby import EndpointGetUsersNearby
from ..types.endpoint_patch_users import EndpointPatchUsers
from ..types.endpoint_patch_users_id_synergies import EndpointPatchUsersIdSynergies
from ..types.endpoint_post_users_id_messages import EndpointPostUsersIdMessages
from ..types.endpoint_post_users_id_metadata import EndpointPostUsersIdMetadata
from ..types.endpoint_post_users_invites import EndpointPostUsersInvites
from ..types.endpoint_post_users_metadata_filters import EndpointPostUsersMetadataFilters
from ..types.endpoint_post_users_searches import EndpointPostUsersSearches
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.patch_users_request_company_size import PatchUsersRequestCompanySize
from .types.patch_users_request_goals_item import PatchUsersRequestGoalsItem
from .types.patch_users_request_industry import PatchUsersRequestIndustry
from .types.patch_users_request_job_position import PatchUsersRequestJobPosition
from .types.patch_users_request_location_importance import PatchUsersRequestLocationImportance
from .types.patch_users_request_targeted_industry import PatchUsersRequestTargetedIndustry
from .types.post_users_id_messages_request_metadata0privacy import PostUsersIdMessagesRequestMetadata0Privacy
from .types.post_users_id_messages_request_metadata1privacy import PostUsersIdMessagesRequestMetadata1Privacy
from .types.post_users_id_messages_request_metadata2privacy import PostUsersIdMessagesRequestMetadata2Privacy
from .types.post_users_id_metadata_request_metadata0privacy import PostUsersIdMetadataRequestMetadata0Privacy
from .types.post_users_id_metadata_request_metadata1privacy import PostUsersIdMetadataRequestMetadata1Privacy
from .types.post_users_id_metadata_request_metadata2privacy import PostUsersIdMetadataRequestMetadata2Privacy


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointGetUsers:
        """
        Retrieve the currently OAuth'ed end-user, based on the access token being used, including private information and settings such as their email address.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsers
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users()
        """
        _response = self._raw_client.get_users(request_options=request_options)
        return _response.data

    def post_users_invites(
        self,
        *,
        csv: typing.Optional[core.File] = OMIT,
        emails: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersInvites:
        """
        Invite users to into your current access token's bubble by having Dazah send out email invitations on your behalf. The invitation sends users to begin the OAuth flow for the current application (based on the settings specified in the application's profile), and therefore they will be redirected to the application upon signing up / logging in. Upon doing so, if they aren't already, they will automatically be connected with you as well. If your current access token does not escape the bubble, the invitation will specify you wish to connect within the application's name. If your current access token escapes the bubble, the invitation will specify you wish to connect within Dazah. Submit either a list of emails, or a LinkedIn or Outlook CSV file. You can retrieve your LinkedIn CSV file by exporting your LinkedIn Connections at https://www.linkedin.com/people/export-settings. You can retrieve your Outlook CSV file by using the Outlook Import and Export Wizard. This endpoint buckets the invitations into four categories: Existing invites are existing users who are already connected with you within the current bubble, and are therefore not emailed; Discovered invites are existing Dazah users who are available to be connected with within the current bubble, and are therefore not emailed. Now that they have been discovered, the users/{:ID}/meet API endpoint may be used to connect with them; Invalid invites are existing Dazah users who are unavailable to be connected with, because they have deactivated accounts, are muting you, etc., and are therefore not emailed; Emailed invites are queued to receive an invitation within approximately 1 hour. Note that if you are attempting to invite an existing Dazah user who does not currently exist within your current access token's bubble, they will fall within the Discovered bucket if your current access token escapes the bubble, but will be emailed an invitation to join the application if your current access token does not escape the bubble.

        Parameters
        ----------
        csv : typing.Optional[core.File]
            See core.File for more documentation

        emails : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersInvites
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.post_users_invites()
        """
        _response = self._raw_client.post_users_invites(csv=csv, emails=emails, request_options=request_options)
        return _response.data

    def post_users_metadata_filters(
        self,
        *,
        limit: typing.Optional[int] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersMetadataFilters:
        """
        Paginated listing of users filtered by arbitrary metadata criteria. Users must match on all key/value pairs passed in. Users may only match on one value of an array passed in. However, users are sorted based on how many distinct values they match on (most matches first).

        Parameters
        ----------
        limit : typing.Optional[int]

        metadata0key : typing.Optional[str]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2values : typing.Optional[typing.List[str]]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersMetadataFilters
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.post_users_metadata_filters()
        """
        _response = self._raw_client.post_users_metadata_filters(
            limit=limit,
            metadata0key=metadata0key,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2values=metadata2values,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_users_nearby(
        self,
        *,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetUsersNearby:
        """
        Fetch an array of users that are geographically close to a set of coordinates. You can only retrieve users existing within the current access token's bubble.

        Parameters
        ----------
        latitude : typing.Optional[float]

        longitude : typing.Optional[float]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersNearby
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_nearby()
        """
        _response = self._raw_client.get_users_nearby(
            latitude=latitude, longitude=longitude, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def post_users_searches(
        self,
        *,
        active_within_x_days: typing.Optional[int] = OMIT,
        audience_ids: typing.Optional[typing.List[int]] = OMIT,
        bubbled: typing.Optional[bool] = OMIT,
        exclude_connections: typing.Optional[bool] = OMIT,
        exclude_matches: typing.Optional[bool] = OMIT,
        exclude_muted: typing.Optional[bool] = OMIT,
        exclude_skipped: typing.Optional[bool] = OMIT,
        geo_latitude: typing.Optional[float] = OMIT,
        geo_longitude: typing.Optional[float] = OMIT,
        geo_miles_away: typing.Optional[float] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        location_city_query: typing.Optional[str] = OMIT,
        location_city_weight: typing.Optional[int] = OMIT,
        location_country_query: typing.Optional[str] = OMIT,
        location_country_weight: typing.Optional[int] = OMIT,
        location_region_query: typing.Optional[str] = OMIT,
        location_region_weight: typing.Optional[int] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0query: typing.Optional[str] = OMIT,
        metadata0weight: typing.Optional[int] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1query: typing.Optional[str] = OMIT,
        metadata1weight: typing.Optional[int] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2query: typing.Optional[str] = OMIT,
        metadata2weight: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        position_organization_query: typing.Optional[str] = OMIT,
        position_organization_weight: typing.Optional[int] = OMIT,
        position_role_query: typing.Optional[str] = OMIT,
        position_role_weight: typing.Optional[int] = OMIT,
        position_summary_query: typing.Optional[str] = OMIT,
        position_summary_weight: typing.Optional[int] = OMIT,
        profile_first_name_query: typing.Optional[str] = OMIT,
        profile_first_name_weight: typing.Optional[int] = OMIT,
        profile_goals_query: typing.Optional[str] = OMIT,
        profile_goals_weight: typing.Optional[str] = OMIT,
        profile_headline_query: typing.Optional[str] = OMIT,
        profile_headline_weight: typing.Optional[int] = OMIT,
        profile_industry_query: typing.Optional[str] = OMIT,
        profile_industry_weight: typing.Optional[int] = OMIT,
        profile_last_name_query: typing.Optional[str] = OMIT,
        profile_last_name_weight: typing.Optional[int] = OMIT,
        profile_pitch_query: typing.Optional[str] = OMIT,
        profile_pitch_weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersSearches:
        """
        Filter and perform a weighted search against user profile fields, CV fields, and metadata by specifying a string to search on for each individual field. By default, results are filtered such that all words in the string must exist, unless you seprate the words with OR. To perform a weighted search (as opposed to filtering), specify the weight (from 0-100) the search algorithm should assign to the field. You can optionally exclude users who you are already in or not in conversations with, exclude users who you previously skipped, or exclude users who you are muting. By doing so, you can effectively customize your own matching algorithm. You can specify geo coordinates to only find users a certain distance away from a specific location, or only find users within a certain distance from the OAuth'ed end-user's last known location. If your app utilizes multiple audience segments, you can specify which audiences you would like to search. You can also limit users to just those who have been recently active. You can also choose to only receive users originating from the current access token's bubble. Only users existing within the current access token's bubble will be matched, and you can only search within a group created by a bubbled user.

        Parameters
        ----------
        active_within_x_days : typing.Optional[int]

        audience_ids : typing.Optional[typing.List[int]]

        bubbled : typing.Optional[bool]

        exclude_connections : typing.Optional[bool]

        exclude_matches : typing.Optional[bool]

        exclude_muted : typing.Optional[bool]

        exclude_skipped : typing.Optional[bool]

        geo_latitude : typing.Optional[float]

        geo_longitude : typing.Optional[float]

        geo_miles_away : typing.Optional[float]

        group_id : typing.Optional[int]

        limit : typing.Optional[int]

        location_city_query : typing.Optional[str]

        location_city_weight : typing.Optional[int]

        location_country_query : typing.Optional[str]

        location_country_weight : typing.Optional[int]

        location_region_query : typing.Optional[str]

        location_region_weight : typing.Optional[int]

        metadata0key : typing.Optional[str]

        metadata0query : typing.Optional[str]

        metadata0weight : typing.Optional[int]

        metadata1key : typing.Optional[str]

        metadata1query : typing.Optional[str]

        metadata1weight : typing.Optional[int]

        metadata2key : typing.Optional[str]

        metadata2query : typing.Optional[str]

        metadata2weight : typing.Optional[int]

        offset : typing.Optional[int]

        position_organization_query : typing.Optional[str]

        position_organization_weight : typing.Optional[int]

        position_role_query : typing.Optional[str]

        position_role_weight : typing.Optional[int]

        position_summary_query : typing.Optional[str]

        position_summary_weight : typing.Optional[int]

        profile_first_name_query : typing.Optional[str]

        profile_first_name_weight : typing.Optional[int]

        profile_goals_query : typing.Optional[str]

        profile_goals_weight : typing.Optional[str]

        profile_headline_query : typing.Optional[str]

        profile_headline_weight : typing.Optional[int]

        profile_industry_query : typing.Optional[str]

        profile_industry_weight : typing.Optional[int]

        profile_last_name_query : typing.Optional[str]

        profile_last_name_weight : typing.Optional[int]

        profile_pitch_query : typing.Optional[str]

        profile_pitch_weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersSearches
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.post_users_searches()
        """
        _response = self._raw_client.post_users_searches(
            active_within_x_days=active_within_x_days,
            audience_ids=audience_ids,
            bubbled=bubbled,
            exclude_connections=exclude_connections,
            exclude_matches=exclude_matches,
            exclude_muted=exclude_muted,
            exclude_skipped=exclude_skipped,
            geo_latitude=geo_latitude,
            geo_longitude=geo_longitude,
            geo_miles_away=geo_miles_away,
            group_id=group_id,
            limit=limit,
            location_city_query=location_city_query,
            location_city_weight=location_city_weight,
            location_country_query=location_country_query,
            location_country_weight=location_country_weight,
            location_region_query=location_region_query,
            location_region_weight=location_region_weight,
            metadata0key=metadata0key,
            metadata0query=metadata0query,
            metadata0weight=metadata0weight,
            metadata1key=metadata1key,
            metadata1query=metadata1query,
            metadata1weight=metadata1weight,
            metadata2key=metadata2key,
            metadata2query=metadata2query,
            metadata2weight=metadata2weight,
            offset=offset,
            position_organization_query=position_organization_query,
            position_organization_weight=position_organization_weight,
            position_role_query=position_role_query,
            position_role_weight=position_role_weight,
            position_summary_query=position_summary_query,
            position_summary_weight=position_summary_weight,
            profile_first_name_query=profile_first_name_query,
            profile_first_name_weight=profile_first_name_weight,
            profile_goals_query=profile_goals_query,
            profile_goals_weight=profile_goals_weight,
            profile_headline_query=profile_headline_query,
            profile_headline_weight=profile_headline_weight,
            profile_industry_query=profile_industry_query,
            profile_industry_weight=profile_industry_weight,
            profile_last_name_query=profile_last_name_query,
            profile_last_name_weight=profile_last_name_weight,
            profile_pitch_query=profile_pitch_query,
            profile_pitch_weight=profile_pitch_weight,
            request_options=request_options,
        )
        return _response.data

    def get_users_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersId:
        """
        Fetch an array of users. You can only retrieve users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersId
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id(
            id="ID",
        )
        """
        _response = self._raw_client.get_users_id(id, request_options=request_options)
        return _response.data

    def get_users_id_groups(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdGroups:
        """
        You can only retrieve groups that were created by users existing within the current access token's bubble.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdGroups
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_groups(
            id=1,
        )
        """
        _response = self._raw_client.get_users_id_groups(id, request_options=request_options)
        return _response.data

    def get_users_id_groups_messages(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetUsersIdGroupsMessages:
        """
        Paginated transcript of group messages authored by an individual user who exists within the current access token's bubble. Messages are sorted oldest to newest.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdGroupsMessages
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_groups_messages(
            id=1,
        )
        """
        _response = self._raw_client.get_users_id_groups_messages(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def post_users_id_messages(
        self,
        id: int,
        *,
        bubbled: typing.Optional[bool] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostUsersIdMessagesRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostUsersIdMessagesRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostUsersIdMessagesRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        text_emoticons: typing.Optional[bool] = OMIT,
        text_raw: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersIdMessages:
        """
        Initiate a conversation with a user who exists within the current access token's bubble by sending them an introductory message. If you aren't already in a conversation with them, this endpoint meets them first, and then sends the message. Note that if you aren't in an existing conversation, you still must meet the criteria to meet them, meaning the user must currently be free for you to meet. You will receive an error message unless it is currently free for you to meet the user. You can use the users/{:IDS}/synergies endpoint to first determine if the user isn't already in a conversation with you and is free for you to meet and, if they aren't, how to pay to meet them. If you don't specify a message, it defaults to your custom introductory message defined in your settings.

        Parameters
        ----------
        id : int

        bubbled : typing.Optional[bool]

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostUsersIdMessagesRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostUsersIdMessagesRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostUsersIdMessagesRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        text_emoticons : typing.Optional[bool]

        text_raw : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersIdMessages
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.post_users_id_messages(
            id=1,
        )
        """
        _response = self._raw_client.post_users_id_messages(
            id,
            bubbled=bubbled,
            metadata0key=metadata0key,
            metadata0privacy=metadata0privacy,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1privacy=metadata1privacy,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2privacy=metadata2privacy,
            metadata2values=metadata2values,
            text_emoticons=text_emoticons,
            text_raw=text_raw,
            request_options=request_options,
        )
        return _response.data

    def get_users_id_metadata(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetUsersIdMetadata:
        """
        Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token's bubble based on preknown metadata key/value pairs.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdMetadata
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_metadata(
            id=1,
        )
        """
        _response = self._raw_client.get_users_id_metadata(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def post_users_id_metadata(
        self,
        id: int,
        *,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostUsersIdMetadataRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostUsersIdMetadataRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostUsersIdMetadataRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersIdMetadata:
        """
        Attach one-to-many key/value pairs of metadata to a user, so long as the user exists within the current access token's bubble. You can set one key at a time, with one or many values. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user; Bubbled metadata by anyone using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user; Private metadata by you, so long as you are using an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostUsersIdMetadataRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostUsersIdMetadataRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostUsersIdMetadataRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersIdMetadata
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.post_users_id_metadata(
            id=1,
        )
        """
        _response = self._raw_client.post_users_id_metadata(
            id,
            metadata0key=metadata0key,
            metadata0privacy=metadata0privacy,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1privacy=metadata1privacy,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2privacy=metadata2privacy,
            metadata2values=metadata2values,
            request_options=request_options,
        )
        return _response.data

    def get_users_id_metadata_collections(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdMetadataCollections:
        """
        Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token's bubble based on preknown metadata key/value pairs. Metadata will be grouped by key.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdMetadataCollections
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_metadata_collections(
            id=1,
        )
        """
        _response = self._raw_client.get_users_id_metadata_collections(id, request_options=request_options)
        return _response.data

    def get_users_id_positions(
        self, id: int, *, bubbled: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdPositions:
        """
        Retrieve the CV of a user who exists within the current access token's bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. You can only record CV data to your own account. However, any app that you have OAuth'ed against can do so. By default, you will receive CV data that all apps have recorded for the user. Optionally, you can choose to only receive data that the current access token's bubble has recorded.

        Parameters
        ----------
        id : int

        bubbled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdPositions
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_positions(
            id=1,
        )
        """
        _response = self._raw_client.get_users_id_positions(id, bubbled=bubbled, request_options=request_options)
        return _response.data

    def get_users_id_synergies(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdSynergies:
        """
        Determine your match relationship with one or more users who exist within the current access token's bubble. Under some conditions, the price to meet the user will be $0. However, if this is not the case, the PayPal URL payment method will be provided along with the price to meet the user. The PayPal API can be leveraged to send payments programatically, provided the parameters passed in remain the same to ensure that the payment is correctly recorded. Once the payment has been recorded via PayPal IPN, the price to meet the user changes to $0. You can then call the users/{:ID}/meet endpoint to meet the user.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdSynergies
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_synergies(
            id="ID",
        )
        """
        _response = self._raw_client.get_users_id_synergies(id, request_options=request_options)
        return _response.data

    def patch_users_id_synergies(
        self,
        id: int,
        *,
        relationship_muted: typing.Optional[bool] = OMIT,
        relationship_skipped: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPatchUsersIdSynergies:
        """
        Skip, mute or unmute a user you've been matched with. Skipped matches are only presented as algorithmic matches after all other candidates have been exhausted. You cannot be matched with or meet muted users. You can only skip, mute or unmute users existing within the same bubble.

        Parameters
        ----------
        id : int

        relationship_muted : typing.Optional[bool]

        relationship_skipped : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchUsersIdSynergies
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.patch_users_id_synergies(
            id=1,
        )
        """
        _response = self._raw_client.patch_users_id_synergies(
            id,
            relationship_muted=relationship_muted,
            relationship_skipped=relationship_skipped,
            request_options=request_options,
        )
        return _response.data

    def patch_users(
        self,
        *,
        company: typing.Optional[str] = OMIT,
        company_size: typing.Optional[PatchUsersRequestCompanySize] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        goals: typing.Optional[typing.List[PatchUsersRequestGoalsItem]] = OMIT,
        headline: typing.Optional[str] = OMIT,
        industry: typing.Optional[PatchUsersRequestIndustry] = OMIT,
        introduction: typing.Optional[str] = OMIT,
        job_position: typing.Optional[PatchUsersRequestJobPosition] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        location_importance: typing.Optional[PatchUsersRequestLocationImportance] = OMIT,
        match_tags: typing.Optional[typing.List[str]] = OMIT,
        pitch: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.List[str]] = OMIT,
        targeted_industry: typing.Optional[PatchUsersRequestTargetedIndustry] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPatchUsers:
        """
        Update the OAuth'ed end user's account profile. At this time, for anti-spam reasons, restrictions preclude the ability to update email address and some other settings via the API.

        Parameters
        ----------
        company : typing.Optional[str]

        company_size : typing.Optional[PatchUsersRequestCompanySize]

        first_name : typing.Optional[str]

        goals : typing.Optional[typing.List[PatchUsersRequestGoalsItem]]

        headline : typing.Optional[str]

        industry : typing.Optional[PatchUsersRequestIndustry]

        introduction : typing.Optional[str]

        job_position : typing.Optional[PatchUsersRequestJobPosition]

        last_name : typing.Optional[str]

        location_importance : typing.Optional[PatchUsersRequestLocationImportance]

        match_tags : typing.Optional[typing.List[str]]

        pitch : typing.Optional[str]

        tags : typing.Optional[typing.List[str]]

        targeted_industry : typing.Optional[PatchUsersRequestTargetedIndustry]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchUsers
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.patch_users()
        """
        _response = self._raw_client.patch_users(
            company=company,
            company_size=company_size,
            first_name=first_name,
            goals=goals,
            headline=headline,
            industry=industry,
            introduction=introduction,
            job_position=job_position,
            last_name=last_name,
            location_importance=location_importance,
            match_tags=match_tags,
            pitch=pitch,
            tags=tags,
            targeted_industry=targeted_industry,
            url=url,
            request_options=request_options,
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointGetUsers:
        """
        Retrieve the currently OAuth'ed end-user, based on the access token being used, including private information and settings such as their email address.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsers
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(request_options=request_options)
        return _response.data

    async def post_users_invites(
        self,
        *,
        csv: typing.Optional[core.File] = OMIT,
        emails: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersInvites:
        """
        Invite users to into your current access token's bubble by having Dazah send out email invitations on your behalf. The invitation sends users to begin the OAuth flow for the current application (based on the settings specified in the application's profile), and therefore they will be redirected to the application upon signing up / logging in. Upon doing so, if they aren't already, they will automatically be connected with you as well. If your current access token does not escape the bubble, the invitation will specify you wish to connect within the application's name. If your current access token escapes the bubble, the invitation will specify you wish to connect within Dazah. Submit either a list of emails, or a LinkedIn or Outlook CSV file. You can retrieve your LinkedIn CSV file by exporting your LinkedIn Connections at https://www.linkedin.com/people/export-settings. You can retrieve your Outlook CSV file by using the Outlook Import and Export Wizard. This endpoint buckets the invitations into four categories: Existing invites are existing users who are already connected with you within the current bubble, and are therefore not emailed; Discovered invites are existing Dazah users who are available to be connected with within the current bubble, and are therefore not emailed. Now that they have been discovered, the users/{:ID}/meet API endpoint may be used to connect with them; Invalid invites are existing Dazah users who are unavailable to be connected with, because they have deactivated accounts, are muting you, etc., and are therefore not emailed; Emailed invites are queued to receive an invitation within approximately 1 hour. Note that if you are attempting to invite an existing Dazah user who does not currently exist within your current access token's bubble, they will fall within the Discovered bucket if your current access token escapes the bubble, but will be emailed an invitation to join the application if your current access token does not escape the bubble.

        Parameters
        ----------
        csv : typing.Optional[core.File]
            See core.File for more documentation

        emails : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersInvites
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.post_users_invites()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users_invites(csv=csv, emails=emails, request_options=request_options)
        return _response.data

    async def post_users_metadata_filters(
        self,
        *,
        limit: typing.Optional[int] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersMetadataFilters:
        """
        Paginated listing of users filtered by arbitrary metadata criteria. Users must match on all key/value pairs passed in. Users may only match on one value of an array passed in. However, users are sorted based on how many distinct values they match on (most matches first).

        Parameters
        ----------
        limit : typing.Optional[int]

        metadata0key : typing.Optional[str]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2values : typing.Optional[typing.List[str]]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersMetadataFilters
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.post_users_metadata_filters()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users_metadata_filters(
            limit=limit,
            metadata0key=metadata0key,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2values=metadata2values,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_users_nearby(
        self,
        *,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetUsersNearby:
        """
        Fetch an array of users that are geographically close to a set of coordinates. You can only retrieve users existing within the current access token's bubble.

        Parameters
        ----------
        latitude : typing.Optional[float]

        longitude : typing.Optional[float]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersNearby
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_nearby()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_nearby(
            latitude=latitude, longitude=longitude, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_users_searches(
        self,
        *,
        active_within_x_days: typing.Optional[int] = OMIT,
        audience_ids: typing.Optional[typing.List[int]] = OMIT,
        bubbled: typing.Optional[bool] = OMIT,
        exclude_connections: typing.Optional[bool] = OMIT,
        exclude_matches: typing.Optional[bool] = OMIT,
        exclude_muted: typing.Optional[bool] = OMIT,
        exclude_skipped: typing.Optional[bool] = OMIT,
        geo_latitude: typing.Optional[float] = OMIT,
        geo_longitude: typing.Optional[float] = OMIT,
        geo_miles_away: typing.Optional[float] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        location_city_query: typing.Optional[str] = OMIT,
        location_city_weight: typing.Optional[int] = OMIT,
        location_country_query: typing.Optional[str] = OMIT,
        location_country_weight: typing.Optional[int] = OMIT,
        location_region_query: typing.Optional[str] = OMIT,
        location_region_weight: typing.Optional[int] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0query: typing.Optional[str] = OMIT,
        metadata0weight: typing.Optional[int] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1query: typing.Optional[str] = OMIT,
        metadata1weight: typing.Optional[int] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2query: typing.Optional[str] = OMIT,
        metadata2weight: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        position_organization_query: typing.Optional[str] = OMIT,
        position_organization_weight: typing.Optional[int] = OMIT,
        position_role_query: typing.Optional[str] = OMIT,
        position_role_weight: typing.Optional[int] = OMIT,
        position_summary_query: typing.Optional[str] = OMIT,
        position_summary_weight: typing.Optional[int] = OMIT,
        profile_first_name_query: typing.Optional[str] = OMIT,
        profile_first_name_weight: typing.Optional[int] = OMIT,
        profile_goals_query: typing.Optional[str] = OMIT,
        profile_goals_weight: typing.Optional[str] = OMIT,
        profile_headline_query: typing.Optional[str] = OMIT,
        profile_headline_weight: typing.Optional[int] = OMIT,
        profile_industry_query: typing.Optional[str] = OMIT,
        profile_industry_weight: typing.Optional[int] = OMIT,
        profile_last_name_query: typing.Optional[str] = OMIT,
        profile_last_name_weight: typing.Optional[int] = OMIT,
        profile_pitch_query: typing.Optional[str] = OMIT,
        profile_pitch_weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersSearches:
        """
        Filter and perform a weighted search against user profile fields, CV fields, and metadata by specifying a string to search on for each individual field. By default, results are filtered such that all words in the string must exist, unless you seprate the words with OR. To perform a weighted search (as opposed to filtering), specify the weight (from 0-100) the search algorithm should assign to the field. You can optionally exclude users who you are already in or not in conversations with, exclude users who you previously skipped, or exclude users who you are muting. By doing so, you can effectively customize your own matching algorithm. You can specify geo coordinates to only find users a certain distance away from a specific location, or only find users within a certain distance from the OAuth'ed end-user's last known location. If your app utilizes multiple audience segments, you can specify which audiences you would like to search. You can also limit users to just those who have been recently active. You can also choose to only receive users originating from the current access token's bubble. Only users existing within the current access token's bubble will be matched, and you can only search within a group created by a bubbled user.

        Parameters
        ----------
        active_within_x_days : typing.Optional[int]

        audience_ids : typing.Optional[typing.List[int]]

        bubbled : typing.Optional[bool]

        exclude_connections : typing.Optional[bool]

        exclude_matches : typing.Optional[bool]

        exclude_muted : typing.Optional[bool]

        exclude_skipped : typing.Optional[bool]

        geo_latitude : typing.Optional[float]

        geo_longitude : typing.Optional[float]

        geo_miles_away : typing.Optional[float]

        group_id : typing.Optional[int]

        limit : typing.Optional[int]

        location_city_query : typing.Optional[str]

        location_city_weight : typing.Optional[int]

        location_country_query : typing.Optional[str]

        location_country_weight : typing.Optional[int]

        location_region_query : typing.Optional[str]

        location_region_weight : typing.Optional[int]

        metadata0key : typing.Optional[str]

        metadata0query : typing.Optional[str]

        metadata0weight : typing.Optional[int]

        metadata1key : typing.Optional[str]

        metadata1query : typing.Optional[str]

        metadata1weight : typing.Optional[int]

        metadata2key : typing.Optional[str]

        metadata2query : typing.Optional[str]

        metadata2weight : typing.Optional[int]

        offset : typing.Optional[int]

        position_organization_query : typing.Optional[str]

        position_organization_weight : typing.Optional[int]

        position_role_query : typing.Optional[str]

        position_role_weight : typing.Optional[int]

        position_summary_query : typing.Optional[str]

        position_summary_weight : typing.Optional[int]

        profile_first_name_query : typing.Optional[str]

        profile_first_name_weight : typing.Optional[int]

        profile_goals_query : typing.Optional[str]

        profile_goals_weight : typing.Optional[str]

        profile_headline_query : typing.Optional[str]

        profile_headline_weight : typing.Optional[int]

        profile_industry_query : typing.Optional[str]

        profile_industry_weight : typing.Optional[int]

        profile_last_name_query : typing.Optional[str]

        profile_last_name_weight : typing.Optional[int]

        profile_pitch_query : typing.Optional[str]

        profile_pitch_weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersSearches
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.post_users_searches()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users_searches(
            active_within_x_days=active_within_x_days,
            audience_ids=audience_ids,
            bubbled=bubbled,
            exclude_connections=exclude_connections,
            exclude_matches=exclude_matches,
            exclude_muted=exclude_muted,
            exclude_skipped=exclude_skipped,
            geo_latitude=geo_latitude,
            geo_longitude=geo_longitude,
            geo_miles_away=geo_miles_away,
            group_id=group_id,
            limit=limit,
            location_city_query=location_city_query,
            location_city_weight=location_city_weight,
            location_country_query=location_country_query,
            location_country_weight=location_country_weight,
            location_region_query=location_region_query,
            location_region_weight=location_region_weight,
            metadata0key=metadata0key,
            metadata0query=metadata0query,
            metadata0weight=metadata0weight,
            metadata1key=metadata1key,
            metadata1query=metadata1query,
            metadata1weight=metadata1weight,
            metadata2key=metadata2key,
            metadata2query=metadata2query,
            metadata2weight=metadata2weight,
            offset=offset,
            position_organization_query=position_organization_query,
            position_organization_weight=position_organization_weight,
            position_role_query=position_role_query,
            position_role_weight=position_role_weight,
            position_summary_query=position_summary_query,
            position_summary_weight=position_summary_weight,
            profile_first_name_query=profile_first_name_query,
            profile_first_name_weight=profile_first_name_weight,
            profile_goals_query=profile_goals_query,
            profile_goals_weight=profile_goals_weight,
            profile_headline_query=profile_headline_query,
            profile_headline_weight=profile_headline_weight,
            profile_industry_query=profile_industry_query,
            profile_industry_weight=profile_industry_weight,
            profile_last_name_query=profile_last_name_query,
            profile_last_name_weight=profile_last_name_weight,
            profile_pitch_query=profile_pitch_query,
            profile_pitch_weight=profile_pitch_weight,
            request_options=request_options,
        )
        return _response.data

    async def get_users_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersId:
        """
        Fetch an array of users. You can only retrieve users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersId
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id(id, request_options=request_options)
        return _response.data

    async def get_users_id_groups(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdGroups:
        """
        You can only retrieve groups that were created by users existing within the current access token's bubble.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdGroups
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_groups(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_groups(id, request_options=request_options)
        return _response.data

    async def get_users_id_groups_messages(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetUsersIdGroupsMessages:
        """
        Paginated transcript of group messages authored by an individual user who exists within the current access token's bubble. Messages are sorted oldest to newest.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdGroupsMessages
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_groups_messages(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_groups_messages(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_users_id_messages(
        self,
        id: int,
        *,
        bubbled: typing.Optional[bool] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostUsersIdMessagesRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostUsersIdMessagesRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostUsersIdMessagesRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        text_emoticons: typing.Optional[bool] = OMIT,
        text_raw: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersIdMessages:
        """
        Initiate a conversation with a user who exists within the current access token's bubble by sending them an introductory message. If you aren't already in a conversation with them, this endpoint meets them first, and then sends the message. Note that if you aren't in an existing conversation, you still must meet the criteria to meet them, meaning the user must currently be free for you to meet. You will receive an error message unless it is currently free for you to meet the user. You can use the users/{:IDS}/synergies endpoint to first determine if the user isn't already in a conversation with you and is free for you to meet and, if they aren't, how to pay to meet them. If you don't specify a message, it defaults to your custom introductory message defined in your settings.

        Parameters
        ----------
        id : int

        bubbled : typing.Optional[bool]

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostUsersIdMessagesRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostUsersIdMessagesRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostUsersIdMessagesRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        text_emoticons : typing.Optional[bool]

        text_raw : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersIdMessages
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.post_users_id_messages(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users_id_messages(
            id,
            bubbled=bubbled,
            metadata0key=metadata0key,
            metadata0privacy=metadata0privacy,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1privacy=metadata1privacy,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2privacy=metadata2privacy,
            metadata2values=metadata2values,
            text_emoticons=text_emoticons,
            text_raw=text_raw,
            request_options=request_options,
        )
        return _response.data

    async def get_users_id_metadata(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetUsersIdMetadata:
        """
        Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token's bubble based on preknown metadata key/value pairs.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdMetadata
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_metadata(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_metadata(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_users_id_metadata(
        self,
        id: int,
        *,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostUsersIdMetadataRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostUsersIdMetadataRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostUsersIdMetadataRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostUsersIdMetadata:
        """
        Attach one-to-many key/value pairs of metadata to a user, so long as the user exists within the current access token's bubble. You can set one key at a time, with one or many values. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user; Bubbled metadata by anyone using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user; Private metadata by you, so long as you are using an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostUsersIdMetadataRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostUsersIdMetadataRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostUsersIdMetadataRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostUsersIdMetadata
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.post_users_id_metadata(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_users_id_metadata(
            id,
            metadata0key=metadata0key,
            metadata0privacy=metadata0privacy,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1privacy=metadata1privacy,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2privacy=metadata2privacy,
            metadata2values=metadata2values,
            request_options=request_options,
        )
        return _response.data

    async def get_users_id_metadata_collections(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdMetadataCollections:
        """
        Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token's bubble based on preknown metadata key/value pairs. Metadata will be grouped by key.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdMetadataCollections
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_metadata_collections(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_metadata_collections(id, request_options=request_options)
        return _response.data

    async def get_users_id_positions(
        self, id: int, *, bubbled: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdPositions:
        """
        Retrieve the CV of a user who exists within the current access token's bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. You can only record CV data to your own account. However, any app that you have OAuth'ed against can do so. By default, you will receive CV data that all apps have recorded for the user. Optionally, you can choose to only receive data that the current access token's bubble has recorded.

        Parameters
        ----------
        id : int

        bubbled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdPositions
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_positions(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_positions(id, bubbled=bubbled, request_options=request_options)
        return _response.data

    async def get_users_id_synergies(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetUsersIdSynergies:
        """
        Determine your match relationship with one or more users who exist within the current access token's bubble. Under some conditions, the price to meet the user will be $0. However, if this is not the case, the PayPal URL payment method will be provided along with the price to meet the user. The PayPal API can be leveraged to send payments programatically, provided the parameters passed in remain the same to ensure that the payment is correctly recorded. Once the payment has been recorded via PayPal IPN, the price to meet the user changes to $0. You can then call the users/{:ID}/meet endpoint to meet the user.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetUsersIdSynergies
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_synergies(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_synergies(id, request_options=request_options)
        return _response.data

    async def patch_users_id_synergies(
        self,
        id: int,
        *,
        relationship_muted: typing.Optional[bool] = OMIT,
        relationship_skipped: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPatchUsersIdSynergies:
        """
        Skip, mute or unmute a user you've been matched with. Skipped matches are only presented as algorithmic matches after all other candidates have been exhausted. You cannot be matched with or meet muted users. You can only skip, mute or unmute users existing within the same bubble.

        Parameters
        ----------
        id : int

        relationship_muted : typing.Optional[bool]

        relationship_skipped : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchUsersIdSynergies
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.patch_users_id_synergies(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_users_id_synergies(
            id,
            relationship_muted=relationship_muted,
            relationship_skipped=relationship_skipped,
            request_options=request_options,
        )
        return _response.data

    async def patch_users(
        self,
        *,
        company: typing.Optional[str] = OMIT,
        company_size: typing.Optional[PatchUsersRequestCompanySize] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        goals: typing.Optional[typing.List[PatchUsersRequestGoalsItem]] = OMIT,
        headline: typing.Optional[str] = OMIT,
        industry: typing.Optional[PatchUsersRequestIndustry] = OMIT,
        introduction: typing.Optional[str] = OMIT,
        job_position: typing.Optional[PatchUsersRequestJobPosition] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        location_importance: typing.Optional[PatchUsersRequestLocationImportance] = OMIT,
        match_tags: typing.Optional[typing.List[str]] = OMIT,
        pitch: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.List[str]] = OMIT,
        targeted_industry: typing.Optional[PatchUsersRequestTargetedIndustry] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPatchUsers:
        """
        Update the OAuth'ed end user's account profile. At this time, for anti-spam reasons, restrictions preclude the ability to update email address and some other settings via the API.

        Parameters
        ----------
        company : typing.Optional[str]

        company_size : typing.Optional[PatchUsersRequestCompanySize]

        first_name : typing.Optional[str]

        goals : typing.Optional[typing.List[PatchUsersRequestGoalsItem]]

        headline : typing.Optional[str]

        industry : typing.Optional[PatchUsersRequestIndustry]

        introduction : typing.Optional[str]

        job_position : typing.Optional[PatchUsersRequestJobPosition]

        last_name : typing.Optional[str]

        location_importance : typing.Optional[PatchUsersRequestLocationImportance]

        match_tags : typing.Optional[typing.List[str]]

        pitch : typing.Optional[str]

        tags : typing.Optional[typing.List[str]]

        targeted_industry : typing.Optional[PatchUsersRequestTargetedIndustry]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchUsers
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.patch_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_users(
            company=company,
            company_size=company_size,
            first_name=first_name,
            goals=goals,
            headline=headline,
            industry=industry,
            introduction=introduction,
            job_position=job_position,
            last_name=last_name,
            location_importance=location_importance,
            match_tags=match_tags,
            pitch=pitch,
            tags=tags,
            targeted_industry=targeted_industry,
            url=url,
            request_options=request_options,
        )
        return _response.data
