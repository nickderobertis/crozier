

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.oauth_callback_url_create import OauthCallbackUrlCreate
from ..types.oauth_callback_url_delete import OauthCallbackUrlDelete
from ..types.oauth_callback_url_listing import OauthCallbackUrlListing
from ..types.oauth_callback_url_read import OauthCallbackUrlRead
from ..types.oauth_callback_url_update import OauthCallbackUrlUpdate


OMIT = typing.cast(typing.Any, ...)


class RawCallbackUrlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OauthCallbackUrlListing]]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OauthCallbackUrlListing]]
            Used for managing OAuth Client Callback URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OauthCallbackUrlListing],
                    parse_obj_as(
                        type_=typing.List[OauthCallbackUrlListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OauthCallbackUrlCreate]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OauthCallbackUrlCreate]
            Used for managing OAuth Client Callback URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url",
            method="POST",
            json={
                "url": url,
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
                    OauthCallbackUrlCreate,
                    parse_obj_as(
                        type_=OauthCallbackUrlCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OauthCallbackUrlRead]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OauthCallbackUrlRead]
            Used for managing OAuth Client Callback URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OauthCallbackUrlRead,
                    parse_obj_as(
                        type_=OauthCallbackUrlRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OauthCallbackUrlUpdate]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OauthCallbackUrlUpdate]
            Used for managing OAuth Client Callback URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "url": url,
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
                    OauthCallbackUrlUpdate,
                    parse_obj_as(
                        type_=OauthCallbackUrlUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OauthCallbackUrlDelete]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OauthCallbackUrlDelete]
            Used for managing OAuth Client Callback URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OauthCallbackUrlDelete,
                    parse_obj_as(
                        type_=OauthCallbackUrlDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCallbackUrlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OauthCallbackUrlListing]]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OauthCallbackUrlListing]]
            Used for managing OAuth Client Callback URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OauthCallbackUrlListing],
                    parse_obj_as(
                        type_=typing.List[OauthCallbackUrlListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_callback_url_for_user_oauth_client(
        self, user_id: int, oauth_client_id: int, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OauthCallbackUrlCreate]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OauthCallbackUrlCreate]
            Used for managing OAuth Client Callback URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url",
            method="POST",
            json={
                "url": url,
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
                    OauthCallbackUrlCreate,
                    parse_obj_as(
                        type_=OauthCallbackUrlCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OauthCallbackUrlRead]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OauthCallbackUrlRead]
            Used for managing OAuth Client Callback URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OauthCallbackUrlRead,
                    parse_obj_as(
                        type_=OauthCallbackUrlRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OauthCallbackUrlUpdate]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        url : str
            The URL for this callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OauthCallbackUrlUpdate]
            Used for managing OAuth Client Callback URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "url": url,
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
                    OauthCallbackUrlUpdate,
                    parse_obj_as(
                        type_=OauthCallbackUrlUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_callback_url_for_user_oauth_client(
        self,
        user_id: int,
        oauth_client_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OauthCallbackUrlDelete]:
        """
        Used for managing OAuth Client Callback URLs.

        Parameters
        ----------
        user_id : int


        oauth_client_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OauthCallbackUrlDelete]
            Used for managing OAuth Client Callback URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/oauth-client/{jsonable_encoder(oauth_client_id)}/callback-url/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OauthCallbackUrlDelete,
                    parse_obj_as(
                        type_=OauthCallbackUrlDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
