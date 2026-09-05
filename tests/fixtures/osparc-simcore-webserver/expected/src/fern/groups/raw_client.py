

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.description_safe_str import DescriptionSafeStr
from ..types.envelope_dict_str_any import EnvelopeDictStrAny
from ..types.envelope_group_get import EnvelopeGroupGet
from ..types.envelope_group_user_get import EnvelopeGroupUserGet
from ..types.envelope_list_group_user_get import EnvelopeListGroupUserGet
from ..types.envelope_list_resource_hit import EnvelopeListResourceHit
from ..types.envelope_my_groups_get import EnvelopeMyGroupsGet
from ..types.envelope_research_resource import EnvelopeResearchResource
from ..types.group_access_rights import GroupAccessRights
from ..types.group_id_int import GroupIdInt
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.name_safe_str import NameSafeStr
from ..types.user_id_int import UserIdInt
from ..types.user_name_safe_id import UserNameSafeId
from .types.get_group_classifiers_request_tree_view import GetGroupClassifiersRequestTreeView
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeMyGroupsGet]:
        """
        List all groups (organizations, primary, everyone and products) I belong to

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeMyGroupsGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyGroupsGet,
                    parse_obj_as(
                        type_=EnvelopeMyGroupsGet,
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

    def create_group(
        self,
        *,
        label: NameSafeStr,
        description: DescriptionSafeStr,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeGroupGet]:
        """
        Creates an organization group

        Parameters
        ----------
        label : NameSafeStr

        description : DescriptionSafeStr

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/groups",
            method="POST",
            json={
                "label": label,
                "description": description,
                "thumbnail": thumbnail,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupGet,
                    parse_obj_as(
                        type_=EnvelopeGroupGet,
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

    def get_group(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeGroupGet]:
        """
        Get an organization group

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupGet,
                    parse_obj_as(
                        type_=EnvelopeGroupGet,
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

    def delete_group(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes organization groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_group(
        self,
        gid: GroupIdInt,
        *,
        label: typing.Optional[NameSafeStr] = OMIT,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeGroupGet]:
        """
        Updates organization groups

        Parameters
        ----------
        gid : GroupIdInt

        label : typing.Optional[NameSafeStr]

        description : typing.Optional[DescriptionSafeStr]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}",
            method="PATCH",
            json={
                "label": label,
                "description": description,
                "thumbnail": thumbnail,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupGet,
                    parse_obj_as(
                        type_=EnvelopeGroupGet,
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

    def get_all_group_users(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListGroupUserGet]:
        """
        Gets users in organization or primary groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListGroupUserGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListGroupUserGet,
                    parse_obj_as(
                        type_=EnvelopeListGroupUserGet,
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

    def add_group_user(
        self,
        gid: GroupIdInt,
        *,
        uid: typing.Optional[UserIdInt] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        email: typing.Optional[LowerCaseEmailStr] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Adds a user to an organization group using their username, user ID, or email (subject to privacy settings)

        Parameters
        ----------
        gid : GroupIdInt

        uid : typing.Optional[UserIdInt]

        user_name : typing.Optional[UserNameSafeId]

        email : typing.Optional[LowerCaseEmailStr]
            Accessible only if the user has opted to share their email in privacy settings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users",
            method="POST",
            json={
                "uid": uid,
                "userName": user_name,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeGroupUserGet]:
        """
        Gets specific user in an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGroupUserGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users/{encode_path_param(uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupUserGet,
                    parse_obj_as(
                        type_=EnvelopeGroupUserGet,
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

    def delete_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Removes a user from an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users/{encode_path_param(uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_group_user(
        self,
        gid: GroupIdInt,
        uid: UserIdInt,
        *,
        access_rights: GroupAccessRights,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeGroupUserGet]:
        """
        Updates user (access-rights) to an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        access_rights : GroupAccessRights

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGroupUserGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users/{encode_path_param(uid)}",
            method="PATCH",
            json={
                "accessRights": convert_and_respect_annotation_metadata(
                    object_=access_rights, annotation=GroupAccessRights, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupUserGet,
                    parse_obj_as(
                        type_=EnvelopeGroupUserGet,
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

    def get_group_classifiers(
        self,
        gid: GroupIdInt,
        *,
        tree_view: typing.Optional[GetGroupClassifiersRequestTreeView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeDictStrAny]:
        """
        Parameters
        ----------
        gid : GroupIdInt

        tree_view : typing.Optional[GetGroupClassifiersRequestTreeView]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictStrAny]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/classifiers",
            method="GET",
            params={
                "tree_view": tree_view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictStrAny,
                    parse_obj_as(
                        type_=EnvelopeDictStrAny,
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

    def get_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeResearchResource]:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeResearchResource]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/sparc/classifiers/scicrunch-resources/{encode_path_param(rrid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeResearchResource,
                    parse_obj_as(
                        type_=EnvelopeResearchResource,
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

    def add_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeResearchResource]:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeResearchResource]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/groups/sparc/classifiers/scicrunch-resources/{encode_path_param(rrid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeResearchResource,
                    parse_obj_as(
                        type_=EnvelopeResearchResource,
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

    def search_scicrunch_resources(
        self, *, guess_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListResourceHit]:
        """
        Parameters
        ----------
        guess_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListResourceHit]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/groups/sparc/classifiers/scicrunch-resources:search",
            method="GET",
            params={
                "guess_name": guess_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListResourceHit,
                    parse_obj_as(
                        type_=EnvelopeListResourceHit,
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

    async def list_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeMyGroupsGet]:
        """
        List all groups (organizations, primary, everyone and products) I belong to

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeMyGroupsGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeMyGroupsGet,
                    parse_obj_as(
                        type_=EnvelopeMyGroupsGet,
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

    async def create_group(
        self,
        *,
        label: NameSafeStr,
        description: DescriptionSafeStr,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeGroupGet]:
        """
        Creates an organization group

        Parameters
        ----------
        label : NameSafeStr

        description : DescriptionSafeStr

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/groups",
            method="POST",
            json={
                "label": label,
                "description": description,
                "thumbnail": thumbnail,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupGet,
                    parse_obj_as(
                        type_=EnvelopeGroupGet,
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

    async def get_group(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeGroupGet]:
        """
        Get an organization group

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupGet,
                    parse_obj_as(
                        type_=EnvelopeGroupGet,
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

    async def delete_group(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes organization groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_group(
        self,
        gid: GroupIdInt,
        *,
        label: typing.Optional[NameSafeStr] = OMIT,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeGroupGet]:
        """
        Updates organization groups

        Parameters
        ----------
        gid : GroupIdInt

        label : typing.Optional[NameSafeStr]

        description : typing.Optional[DescriptionSafeStr]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}",
            method="PATCH",
            json={
                "label": label,
                "description": description,
                "thumbnail": thumbnail,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupGet,
                    parse_obj_as(
                        type_=EnvelopeGroupGet,
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

    async def get_all_group_users(
        self, gid: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListGroupUserGet]:
        """
        Gets users in organization or primary groups

        Parameters
        ----------
        gid : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListGroupUserGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListGroupUserGet,
                    parse_obj_as(
                        type_=EnvelopeListGroupUserGet,
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

    async def add_group_user(
        self,
        gid: GroupIdInt,
        *,
        uid: typing.Optional[UserIdInt] = OMIT,
        user_name: typing.Optional[UserNameSafeId] = OMIT,
        email: typing.Optional[LowerCaseEmailStr] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Adds a user to an organization group using their username, user ID, or email (subject to privacy settings)

        Parameters
        ----------
        gid : GroupIdInt

        uid : typing.Optional[UserIdInt]

        user_name : typing.Optional[UserNameSafeId]

        email : typing.Optional[LowerCaseEmailStr]
            Accessible only if the user has opted to share their email in privacy settings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users",
            method="POST",
            json={
                "uid": uid,
                "userName": user_name,
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeGroupUserGet]:
        """
        Gets specific user in an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGroupUserGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users/{encode_path_param(uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupUserGet,
                    parse_obj_as(
                        type_=EnvelopeGroupUserGet,
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

    async def delete_group_user(
        self, gid: GroupIdInt, uid: UserIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Removes a user from an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users/{encode_path_param(uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_group_user(
        self,
        gid: GroupIdInt,
        uid: UserIdInt,
        *,
        access_rights: GroupAccessRights,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeGroupUserGet]:
        """
        Updates user (access-rights) to an organization group

        Parameters
        ----------
        gid : GroupIdInt

        uid : UserIdInt

        access_rights : GroupAccessRights

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGroupUserGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/users/{encode_path_param(uid)}",
            method="PATCH",
            json={
                "accessRights": convert_and_respect_annotation_metadata(
                    object_=access_rights, annotation=GroupAccessRights, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGroupUserGet,
                    parse_obj_as(
                        type_=EnvelopeGroupUserGet,
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

    async def get_group_classifiers(
        self,
        gid: GroupIdInt,
        *,
        tree_view: typing.Optional[GetGroupClassifiersRequestTreeView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeDictStrAny]:
        """
        Parameters
        ----------
        gid : GroupIdInt

        tree_view : typing.Optional[GetGroupClassifiersRequestTreeView]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictStrAny]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/{encode_path_param(gid)}/classifiers",
            method="GET",
            params={
                "tree_view": tree_view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictStrAny,
                    parse_obj_as(
                        type_=EnvelopeDictStrAny,
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

    async def get_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeResearchResource]:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeResearchResource]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/sparc/classifiers/scicrunch-resources/{encode_path_param(rrid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeResearchResource,
                    parse_obj_as(
                        type_=EnvelopeResearchResource,
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

    async def add_scicrunch_resource(
        self, rrid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeResearchResource]:
        """
        Parameters
        ----------
        rrid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeResearchResource]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/groups/sparc/classifiers/scicrunch-resources/{encode_path_param(rrid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeResearchResource,
                    parse_obj_as(
                        type_=EnvelopeResearchResource,
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

    async def search_scicrunch_resources(
        self, *, guess_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListResourceHit]:
        """
        Parameters
        ----------
        guess_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListResourceHit]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/groups/sparc/classifiers/scicrunch-resources:search",
            method="GET",
            params={
                "guess_name": guess_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListResourceHit,
                    parse_obj_as(
                        type_=EnvelopeListResourceHit,
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
