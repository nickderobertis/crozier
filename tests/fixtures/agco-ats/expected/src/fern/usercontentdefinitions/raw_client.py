

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_content_submission_shared_business_entities_user_content_definition import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition,
)
from ..types.content_submission_shared_business_entities_user_content_definition import (
    ContentSubmissionSharedBusinessEntitiesUserContentDefinition,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsercontentdefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getusercontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition]:
        """
        Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UserContentDefinitions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "userID": user_id,
                "contentDefinitionID": content_definition_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition,
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

    def postusercontentdefinition(
        self,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        user_content_definition_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.
                    The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : typing.Optional[int]
            The ID of the ContentDefinition.

        user_content_definition_id : typing.Optional[int]
            Read Only. The ID of the User to ContentDefinition relationship.

        user_id : typing.Optional[int]
            The ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UserContentDefinitions",
            method="POST",
            json={
                "ContentDefinitionID": content_definition_id,
                "UserContentDefinitionID": user_content_definition_id,
                "UserID": user_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    def getusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentSubmissionSharedBusinessEntitiesUserContentDefinition]:
        """
        Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentSubmissionSharedBusinessEntitiesUserContentDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UserContentDefinitions/{encode_path_param(user_content_definition_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesUserContentDefinition,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesUserContentDefinition,
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

    def deleteusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UserContentDefinitions/{encode_path_param(user_content_definition_id)}",
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


class AsyncRawUsercontentdefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getusercontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition]:
        """
        Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UserContentDefinitions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "userID": user_id,
                "contentDefinitionID": content_definition_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition,
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

    async def postusercontentdefinition(
        self,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        user_content_definition_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.
                    The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : typing.Optional[int]
            The ID of the ContentDefinition.

        user_content_definition_id : typing.Optional[int]
            Read Only. The ID of the User to ContentDefinition relationship.

        user_id : typing.Optional[int]
            The ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UserContentDefinitions",
            method="POST",
            json={
                "ContentDefinitionID": content_definition_id,
                "UserContentDefinitionID": user_content_definition_id,
                "UserID": user_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def getusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesUserContentDefinition]:
        """
        Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesUserContentDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UserContentDefinitions/{encode_path_param(user_content_definition_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesUserContentDefinition,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesUserContentDefinition,
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

    async def deleteusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UserContentDefinitions/{encode_path_param(user_content_definition_id)}",
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
