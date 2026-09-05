

import json
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.endpoint_delete_groups_id_memberships import EndpointDeleteGroupsIdMemberships
from ..types.endpoint_delete_groups_messages_id import EndpointDeleteGroupsMessagesId
from ..types.endpoint_get_groups import EndpointGetGroups
from ..types.endpoint_get_groups_id import EndpointGetGroupsId
from ..types.endpoint_get_groups_id_memberships import EndpointGetGroupsIdMemberships
from ..types.endpoint_get_groups_id_messages import EndpointGetGroupsIdMessages
from ..types.endpoint_get_groups_id_statuses import EndpointGetGroupsIdStatuses
from ..types.endpoint_get_groups_messages_id import EndpointGetGroupsMessagesId
from ..types.endpoint_get_groups_messages_id_metadata import EndpointGetGroupsMessagesIdMetadata
from ..types.endpoint_get_groups_messages_id_metadata_collections import EndpointGetGroupsMessagesIdMetadataCollections
from ..types.endpoint_get_groups_statuses import EndpointGetGroupsStatuses
from ..types.endpoint_patch_groups_id import EndpointPatchGroupsId
from ..types.endpoint_patch_groups_id_memberships import EndpointPatchGroupsIdMemberships
from ..types.endpoint_post_groups import EndpointPostGroups
from ..types.endpoint_post_groups_id_memberships import EndpointPostGroupsIdMemberships
from ..types.endpoint_post_groups_id_messages import EndpointPostGroupsIdMessages
from ..types.endpoint_post_groups_id_schedules import EndpointPostGroupsIdSchedules
from ..types.endpoint_post_groups_messages_id_metadata import EndpointPostGroupsMessagesIdMetadata
from ..types.endpoint_post_groups_messages_metadata_filters import EndpointPostGroupsMessagesMetadataFilters
from ..types.endpoint_post_groups_schedules import EndpointPostGroupsSchedules
from .types.patch_groups_id_request_privacy import PatchGroupsIdRequestPrivacy
from .types.post_groups_id_messages_request_metadata0privacy import PostGroupsIdMessagesRequestMetadata0Privacy
from .types.post_groups_id_messages_request_metadata1privacy import PostGroupsIdMessagesRequestMetadata1Privacy
from .types.post_groups_id_messages_request_metadata2privacy import PostGroupsIdMessagesRequestMetadata2Privacy
from .types.post_groups_id_schedules_request_sort import PostGroupsIdSchedulesRequestSort
from .types.post_groups_messages_id_metadata_request_metadata0privacy import (
    PostGroupsMessagesIdMetadataRequestMetadata0Privacy,
)
from .types.post_groups_messages_id_metadata_request_metadata1privacy import (
    PostGroupsMessagesIdMetadataRequestMetadata1Privacy,
)
from .types.post_groups_messages_id_metadata_request_metadata2privacy import (
    PostGroupsMessagesIdMetadataRequestMetadata2Privacy,
)
from .types.post_groups_request_privacy import PostGroupsRequestPrivacy
from .types.post_groups_schedules_request_sort import PostGroupsSchedulesRequestSort
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_groups(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointGetGroups]:
        """
        Fetch an array of all groups that were created by users existing within the current access token's bubble. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed.

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroups]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroups,
                    parse_obj_as(
                        type_=EndpointGetGroups,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups(
        self,
        *,
        description: str,
        name: str,
        privacy: PostGroupsRequestPrivacy,
        slug: str,
        passphrase: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostGroups]:
        """
        Create a new group for other members to join. Any user who is using an access token whose bubble you exist in can join your group provided it is not a private group. Private groups can only be joined by members who know its passphrase. Unlisted groups can be joined by anybody as long as they know the Group ID, but they are not referenced anywhere to non-members. Public groups can be joined by anybody, are discoverable, and anyone can see the public groups a user is a member of, provided the group owner exists in their access token's bubble. Groups each have their own discussions, transcripts, schedules, and ability to list and search their members.

        Parameters
        ----------
        description : str

        name : str

        privacy : PostGroupsRequestPrivacy

        slug : str

        passphrase : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostGroups]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            data={
                "description": description,
                "name": name,
                "passphrase": passphrase,
                "privacy": privacy,
                "slug": slug,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroups,
                    parse_obj_as(
                        type_=EndpointPostGroups,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups_messages_metadata_filters(
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
    ) -> HttpResponse[EndpointPostGroupsMessagesMetadataFilters]:
        """
        Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

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
        HttpResponse[EndpointPostGroupsMessagesMetadataFilters]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups/messages/metadata/filters",
            method="POST",
            data={
                "limit": limit,
                "metadata_0_key": metadata0key,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
                "offset": offset,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsMessagesMetadataFilters,
                    parse_obj_as(
                        type_=EndpointPostGroupsMessagesMetadataFilters,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_messages_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetGroupsMessagesId]:
        """
        Fetch an array of group messages. You can only retrieve messages authored by you or by users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsMessagesId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsMessagesId,
                    parse_obj_as(
                        type_=EndpointGetGroupsMessagesId,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_groups_messages_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointDeleteGroupsMessagesId]:
        """
        Delete an array of group messages. You must be the owner or moderator of the group.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointDeleteGroupsMessagesId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointDeleteGroupsMessagesId,
                    parse_obj_as(
                        type_=EndpointDeleteGroupsMessagesId,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_messages_id_metadata(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointGetGroupsMessagesIdMetadata]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsMessagesIdMetadata]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}/metadata",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointGetGroupsMessagesIdMetadata,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups_messages_id_metadata(
        self,
        id: int,
        *,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostGroupsMessagesIdMetadata]:
        """
        Attach one-to-many key/value pairs of metadata to a group message, so long as the user who authored the message exists within the current access token's bubble and you are a member of their group. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user who authored the message and who is also a member of the group the message belongs to; Bubbled metadata by anyone using an access token existing within the current bubble who is also a member of the group the message belongs to; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message and you remain a member of the group; Private metadata by you, so long as you are using an access token existing within the current bubble and you remain a member of the group.

        Parameters
        ----------
        id : int

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostGroupsMessagesIdMetadata]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}/metadata",
            method="POST",
            data={
                "metadata_0_key": metadata0key,
                "metadata_0_privacy": metadata0privacy,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_privacy": metadata1privacy,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_privacy": metadata2privacy,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointPostGroupsMessagesIdMetadata,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_messages_id_metadata_collections(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetGroupsMessagesIdMetadataCollections]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsMessagesIdMetadataCollections]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}/metadata/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsMessagesIdMetadataCollections,
                    parse_obj_as(
                        type_=EndpointGetGroupsMessagesIdMetadataCollections,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups_schedules(
        self,
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostGroupsSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostGroupsSchedules]:
        """
        Paginated report of information about messages contributed by group and date. Only groups you're a member of and group messages authored by users the current access token has access to are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

        Parameters
        ----------
        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostGroupsSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostGroupsSchedules]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups/schedules",
            method="POST",
            data={
                "date": date,
                "limit": limit,
                "offset": offset,
                "roll_up": roll_up,
                "sort": sort,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsSchedules,
                    parse_obj_as(
                        type_=EndpointPostGroupsSchedules,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_statuses(
        self,
        *,
        existing_membership: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointGetGroupsStatuses]:
        """
        Retrieve groups that were created by users within the current access token's bubble, along with your current relationship with the groups. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed. Optionally only retrieve groups that you are a member of.

        Parameters
        ----------
        existing_membership : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsStatuses]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups/statuses",
            method="GET",
            params={
                "existing_membership": existing_membership,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsStatuses,
                    parse_obj_as(
                        type_=EndpointGetGroupsStatuses,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetGroupsId]:
        """
        Fetch an array of groups. You can only retrieve groups created by users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsId,
                    parse_obj_as(
                        type_=EndpointGetGroupsId,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_groups_id(
        self,
        id: int,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        passphrase: typing.Optional[str] = OMIT,
        privacy: typing.Optional[PatchGroupsIdRequestPrivacy] = OMIT,
        slug: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPatchGroupsId]:
        """
        Modify a group you previously created.

        Parameters
        ----------
        id : int

        description : typing.Optional[str]

        name : typing.Optional[str]

        passphrase : typing.Optional[str]

        privacy : typing.Optional[PatchGroupsIdRequestPrivacy]

        slug : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPatchGroupsId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}",
            method="PATCH",
            data={
                "description": description,
                "name": name,
                "passphrase": passphrase,
                "privacy": privacy,
                "slug": slug,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPatchGroupsId,
                    parse_obj_as(
                        type_=EndpointPatchGroupsId,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_id_memberships(
        self,
        id: typing.Sequence[int],
        *,
        moderators_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointGetGroupsIdMemberships]:
        """
        Fetch an array of users who are members of specific groups that you are also a member of. You can only retrieve users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        moderators_only : typing.Optional[bool]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsIdMemberships]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="GET",
            params={
                "moderators_only": moderators_only,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointGetGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups_id_memberships(
        self,
        id: int,
        *,
        passphrase: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostGroupsIdMemberships]:
        """
        Join a group that was created by a user who exists within the current access token's bubble, or join other users into a group that you created. If you are the group owner, you can pass in a user_id to create membership records for a user you are in a conversation with. The user must exist within the current access token's bubble. If the group is private, you must successfully pass in its passphrase in order to join. You can obtain the passphrase from the group's owner.

        Parameters
        ----------
        id : int

        passphrase : typing.Optional[str]

        user_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostGroupsIdMemberships]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="POST",
            data={
                "passphrase": passphrase,
                "user_id": user_id,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointPostGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_groups_id_memberships(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointDeleteGroupsIdMemberships]:
        """
        Leave a group that you are a member of and that was created by a user who exists within the current access token's bubble.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointDeleteGroupsIdMemberships]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointDeleteGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointDeleteGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_groups_id_memberships(
        self,
        id: int,
        *,
        user_id: int,
        moderator: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPatchGroupsIdMemberships]:
        """
        Promote or demote a member's privileges within a group that you created. The user must exist within the current access token's bubble and be an existing member of the group.

        Parameters
        ----------
        id : int

        user_id : int

        moderator : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPatchGroupsIdMemberships]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="PATCH",
            data={
                "moderator": moderator,
                "user_id": user_id,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPatchGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointPatchGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_id_messages(
        self,
        id: int,
        *,
        gt_message_id: typing.Optional[int] = None,
        exclude_self: typing.Optional[bool] = None,
        include_deleted: typing.Optional[bool] = None,
        date: typing.Optional[str] = None,
        bubbled: typing.Optional[bool] = None,
        record_seen: typing.Optional[bool] = None,
        timeout: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointGetGroupsIdMessages]:
        """
        Retrieve the last {limit} messages in the group, for messages authored by users within the current access token's bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you've seen with other group members. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by other members of the group, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token's bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the group is reset to zero.

        Parameters
        ----------
        id : int

        gt_message_id : typing.Optional[int]

        exclude_self : typing.Optional[bool]

        include_deleted : typing.Optional[bool]

        date : typing.Optional[str]

        bubbled : typing.Optional[bool]

        record_seen : typing.Optional[bool]

        timeout : typing.Optional[int]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsIdMessages]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/messages",
            method="GET",
            params={
                "gt_message_id": gt_message_id,
                "exclude_self": exclude_self,
                "include_deleted": include_deleted,
                "date": date,
                "bubbled": bubbled,
                "record_seen": record_seen,
                "timeout": timeout,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsIdMessages,
                    parse_obj_as(
                        type_=EndpointGetGroupsIdMessages,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups_id_messages(
        self,
        id: int,
        *,
        text_raw: str,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostGroupsIdMessagesRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostGroupsIdMessagesRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostGroupsIdMessagesRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostGroupsIdMessages]:
        """
        Post a message to a group that you are a member of and that was created by a user who exists within the current access token's bubble. Optionally specify whether emoticons should be parsed into smiley images. Additionally, optionally attach a single metadata key/value pair to the group message upon submission.

        Parameters
        ----------
        id : int

        text_raw : str

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostGroupsIdMessagesRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostGroupsIdMessagesRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostGroupsIdMessagesRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostGroupsIdMessages]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/messages",
            method="POST",
            data={
                "metadata_0_key": metadata0key,
                "metadata_0_privacy": metadata0privacy,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_privacy": metadata1privacy,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_privacy": metadata2privacy,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
                "text_emoticons": text_emoticons,
                "text_raw": text_raw,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsIdMessages,
                    parse_obj_as(
                        type_=EndpointPostGroupsIdMessages,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_groups_id_schedules(
        self,
        id: typing.Sequence[int],
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostGroupsIdSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostGroupsIdSchedules]:
        """
        Paginated report of information about group messages contributed by conversation and date. Only groups you're a member of and group messages authored by users existing within the current access token's bubble are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the group discussion(s).

        Parameters
        ----------
        id : typing.Sequence[int]

        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostGroupsIdSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostGroupsIdSchedules]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/schedules",
            method="POST",
            data={
                "date": date,
                "limit": limit,
                "offset": offset,
                "roll_up": roll_up,
                "sort": sort,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsIdSchedules,
                    parse_obj_as(
                        type_=EndpointPostGroupsIdSchedules,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_groups_id_statuses(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetGroupsIdStatuses]:
        """
        Status information about your current relationship with one or more groups you are a member of, provided the users who created the groups exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetGroupsIdStatuses]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/statuses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsIdStatuses,
                    parse_obj_as(
                        type_=EndpointGetGroupsIdStatuses,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_groups(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointGetGroups]:
        """
        Fetch an array of all groups that were created by users existing within the current access token's bubble. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed.

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroups]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroups,
                    parse_obj_as(
                        type_=EndpointGetGroups,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups(
        self,
        *,
        description: str,
        name: str,
        privacy: PostGroupsRequestPrivacy,
        slug: str,
        passphrase: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostGroups]:
        """
        Create a new group for other members to join. Any user who is using an access token whose bubble you exist in can join your group provided it is not a private group. Private groups can only be joined by members who know its passphrase. Unlisted groups can be joined by anybody as long as they know the Group ID, but they are not referenced anywhere to non-members. Public groups can be joined by anybody, are discoverable, and anyone can see the public groups a user is a member of, provided the group owner exists in their access token's bubble. Groups each have their own discussions, transcripts, schedules, and ability to list and search their members.

        Parameters
        ----------
        description : str

        name : str

        privacy : PostGroupsRequestPrivacy

        slug : str

        passphrase : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostGroups]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            data={
                "description": description,
                "name": name,
                "passphrase": passphrase,
                "privacy": privacy,
                "slug": slug,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroups,
                    parse_obj_as(
                        type_=EndpointPostGroups,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups_messages_metadata_filters(
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
    ) -> AsyncHttpResponse[EndpointPostGroupsMessagesMetadataFilters]:
        """
        Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

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
        AsyncHttpResponse[EndpointPostGroupsMessagesMetadataFilters]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups/messages/metadata/filters",
            method="POST",
            data={
                "limit": limit,
                "metadata_0_key": metadata0key,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
                "offset": offset,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsMessagesMetadataFilters,
                    parse_obj_as(
                        type_=EndpointPostGroupsMessagesMetadataFilters,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_messages_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetGroupsMessagesId]:
        """
        Fetch an array of group messages. You can only retrieve messages authored by you or by users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsMessagesId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsMessagesId,
                    parse_obj_as(
                        type_=EndpointGetGroupsMessagesId,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_groups_messages_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointDeleteGroupsMessagesId]:
        """
        Delete an array of group messages. You must be the owner or moderator of the group.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointDeleteGroupsMessagesId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointDeleteGroupsMessagesId,
                    parse_obj_as(
                        type_=EndpointDeleteGroupsMessagesId,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_messages_id_metadata(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointGetGroupsMessagesIdMetadata]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsMessagesIdMetadata]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}/metadata",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointGetGroupsMessagesIdMetadata,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups_messages_id_metadata(
        self,
        id: int,
        *,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostGroupsMessagesIdMetadata]:
        """
        Attach one-to-many key/value pairs of metadata to a group message, so long as the user who authored the message exists within the current access token's bubble and you are a member of their group. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user who authored the message and who is also a member of the group the message belongs to; Bubbled metadata by anyone using an access token existing within the current bubble who is also a member of the group the message belongs to; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message and you remain a member of the group; Private metadata by you, so long as you are using an access token existing within the current bubble and you remain a member of the group.

        Parameters
        ----------
        id : int

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostGroupsMessagesIdMetadataRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostGroupsMessagesIdMetadata]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}/metadata",
            method="POST",
            data={
                "metadata_0_key": metadata0key,
                "metadata_0_privacy": metadata0privacy,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_privacy": metadata1privacy,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_privacy": metadata2privacy,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointPostGroupsMessagesIdMetadata,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_messages_id_metadata_collections(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetGroupsMessagesIdMetadataCollections]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsMessagesIdMetadataCollections]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/messages/{encode_path_param(id)}/metadata/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsMessagesIdMetadataCollections,
                    parse_obj_as(
                        type_=EndpointGetGroupsMessagesIdMetadataCollections,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups_schedules(
        self,
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostGroupsSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostGroupsSchedules]:
        """
        Paginated report of information about messages contributed by group and date. Only groups you're a member of and group messages authored by users the current access token has access to are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

        Parameters
        ----------
        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostGroupsSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostGroupsSchedules]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups/schedules",
            method="POST",
            data={
                "date": date,
                "limit": limit,
                "offset": offset,
                "roll_up": roll_up,
                "sort": sort,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsSchedules,
                    parse_obj_as(
                        type_=EndpointPostGroupsSchedules,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_statuses(
        self,
        *,
        existing_membership: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointGetGroupsStatuses]:
        """
        Retrieve groups that were created by users within the current access token's bubble, along with your current relationship with the groups. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed. Optionally only retrieve groups that you are a member of.

        Parameters
        ----------
        existing_membership : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsStatuses]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups/statuses",
            method="GET",
            params={
                "existing_membership": existing_membership,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsStatuses,
                    parse_obj_as(
                        type_=EndpointGetGroupsStatuses,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetGroupsId]:
        """
        Fetch an array of groups. You can only retrieve groups created by users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsId,
                    parse_obj_as(
                        type_=EndpointGetGroupsId,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_groups_id(
        self,
        id: int,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        passphrase: typing.Optional[str] = OMIT,
        privacy: typing.Optional[PatchGroupsIdRequestPrivacy] = OMIT,
        slug: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPatchGroupsId]:
        """
        Modify a group you previously created.

        Parameters
        ----------
        id : int

        description : typing.Optional[str]

        name : typing.Optional[str]

        passphrase : typing.Optional[str]

        privacy : typing.Optional[PatchGroupsIdRequestPrivacy]

        slug : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPatchGroupsId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}",
            method="PATCH",
            data={
                "description": description,
                "name": name,
                "passphrase": passphrase,
                "privacy": privacy,
                "slug": slug,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPatchGroupsId,
                    parse_obj_as(
                        type_=EndpointPatchGroupsId,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_id_memberships(
        self,
        id: typing.Sequence[int],
        *,
        moderators_only: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointGetGroupsIdMemberships]:
        """
        Fetch an array of users who are members of specific groups that you are also a member of. You can only retrieve users existing within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        moderators_only : typing.Optional[bool]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsIdMemberships]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="GET",
            params={
                "moderators_only": moderators_only,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointGetGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups_id_memberships(
        self,
        id: int,
        *,
        passphrase: typing.Optional[str] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostGroupsIdMemberships]:
        """
        Join a group that was created by a user who exists within the current access token's bubble, or join other users into a group that you created. If you are the group owner, you can pass in a user_id to create membership records for a user you are in a conversation with. The user must exist within the current access token's bubble. If the group is private, you must successfully pass in its passphrase in order to join. You can obtain the passphrase from the group's owner.

        Parameters
        ----------
        id : int

        passphrase : typing.Optional[str]

        user_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostGroupsIdMemberships]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="POST",
            data={
                "passphrase": passphrase,
                "user_id": user_id,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointPostGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_groups_id_memberships(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointDeleteGroupsIdMemberships]:
        """
        Leave a group that you are a member of and that was created by a user who exists within the current access token's bubble.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointDeleteGroupsIdMemberships]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointDeleteGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointDeleteGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_groups_id_memberships(
        self,
        id: int,
        *,
        user_id: int,
        moderator: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPatchGroupsIdMemberships]:
        """
        Promote or demote a member's privileges within a group that you created. The user must exist within the current access token's bubble and be an existing member of the group.

        Parameters
        ----------
        id : int

        user_id : int

        moderator : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPatchGroupsIdMemberships]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/memberships",
            method="PATCH",
            data={
                "moderator": moderator,
                "user_id": user_id,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPatchGroupsIdMemberships,
                    parse_obj_as(
                        type_=EndpointPatchGroupsIdMemberships,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_id_messages(
        self,
        id: int,
        *,
        gt_message_id: typing.Optional[int] = None,
        exclude_self: typing.Optional[bool] = None,
        include_deleted: typing.Optional[bool] = None,
        date: typing.Optional[str] = None,
        bubbled: typing.Optional[bool] = None,
        record_seen: typing.Optional[bool] = None,
        timeout: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointGetGroupsIdMessages]:
        """
        Retrieve the last {limit} messages in the group, for messages authored by users within the current access token's bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you've seen with other group members. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by other members of the group, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token's bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the group is reset to zero.

        Parameters
        ----------
        id : int

        gt_message_id : typing.Optional[int]

        exclude_self : typing.Optional[bool]

        include_deleted : typing.Optional[bool]

        date : typing.Optional[str]

        bubbled : typing.Optional[bool]

        record_seen : typing.Optional[bool]

        timeout : typing.Optional[int]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsIdMessages]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/messages",
            method="GET",
            params={
                "gt_message_id": gt_message_id,
                "exclude_self": exclude_self,
                "include_deleted": include_deleted,
                "date": date,
                "bubbled": bubbled,
                "record_seen": record_seen,
                "timeout": timeout,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsIdMessages,
                    parse_obj_as(
                        type_=EndpointGetGroupsIdMessages,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups_id_messages(
        self,
        id: int,
        *,
        text_raw: str,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostGroupsIdMessagesRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostGroupsIdMessagesRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostGroupsIdMessagesRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostGroupsIdMessages]:
        """
        Post a message to a group that you are a member of and that was created by a user who exists within the current access token's bubble. Optionally specify whether emoticons should be parsed into smiley images. Additionally, optionally attach a single metadata key/value pair to the group message upon submission.

        Parameters
        ----------
        id : int

        text_raw : str

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostGroupsIdMessagesRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostGroupsIdMessagesRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostGroupsIdMessagesRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostGroupsIdMessages]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/messages",
            method="POST",
            data={
                "metadata_0_key": metadata0key,
                "metadata_0_privacy": metadata0privacy,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_privacy": metadata1privacy,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_privacy": metadata2privacy,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
                "text_emoticons": text_emoticons,
                "text_raw": text_raw,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsIdMessages,
                    parse_obj_as(
                        type_=EndpointPostGroupsIdMessages,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_groups_id_schedules(
        self,
        id: typing.Sequence[int],
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostGroupsIdSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostGroupsIdSchedules]:
        """
        Paginated report of information about group messages contributed by conversation and date. Only groups you're a member of and group messages authored by users existing within the current access token's bubble are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the group discussion(s).

        Parameters
        ----------
        id : typing.Sequence[int]

        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostGroupsIdSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostGroupsIdSchedules]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/schedules",
            method="POST",
            data={
                "date": date,
                "limit": limit,
                "offset": offset,
                "roll_up": roll_up,
                "sort": sort,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostGroupsIdSchedules,
                    parse_obj_as(
                        type_=EndpointPostGroupsIdSchedules,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_groups_id_statuses(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetGroupsIdStatuses]:
        """
        Status information about your current relationship with one or more groups you are a member of, provided the users who created the groups exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetGroupsIdStatuses]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/statuses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetGroupsIdStatuses,
                    parse_obj_as(
                        type_=EndpointGetGroupsIdStatuses,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
