

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.internal_server_error_body import InternalServerErrorBody
from .types.post_v3connections_google_docs_token_response import PostV3ConnectionsGoogleDocsTokenResponse
from .types.post_v3connections_slack_token_response import PostV3ConnectionsSlackTokenResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_v3connections_slack_token(
        self, *, team_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV3ConnectionsSlackTokenResponse]:
        """
        Get a valid Slack access token for a connected workspace. Automatically refreshes the token if expired.

        Parameters
        ----------
        team_id : str
            The Slack team/workspace ID (e.g., 'T9TK3CUKW')

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV3ConnectionsSlackTokenResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/connections/slack/token",
            method="POST",
            json={
                "team_id": team_id,
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
                    PostV3ConnectionsSlackTokenResponse,
                    parse_obj_as(
                        type_=PostV3ConnectionsSlackTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_v3connections_google_docs_token(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV3ConnectionsGoogleDocsTokenResponse]:
        """
        Get a valid Google access token for a connected Google account. Automatically refreshes the token if expired.

        Parameters
        ----------
        email : str
            The Google account email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV3ConnectionsGoogleDocsTokenResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/connections/google-docs/token",
            method="POST",
            json={
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
                _data = typing.cast(
                    PostV3ConnectionsGoogleDocsTokenResponse,
                    parse_obj_as(
                        type_=PostV3ConnectionsGoogleDocsTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_v3connections_slack_token(
        self, *, team_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV3ConnectionsSlackTokenResponse]:
        """
        Get a valid Slack access token for a connected workspace. Automatically refreshes the token if expired.

        Parameters
        ----------
        team_id : str
            The Slack team/workspace ID (e.g., 'T9TK3CUKW')

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV3ConnectionsSlackTokenResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/connections/slack/token",
            method="POST",
            json={
                "team_id": team_id,
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
                    PostV3ConnectionsSlackTokenResponse,
                    parse_obj_as(
                        type_=PostV3ConnectionsSlackTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_v3connections_google_docs_token(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV3ConnectionsGoogleDocsTokenResponse]:
        """
        Get a valid Google access token for a connected Google account. Automatically refreshes the token if expired.

        Parameters
        ----------
        email : str
            The Google account email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV3ConnectionsGoogleDocsTokenResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/connections/google-docs/token",
            method="POST",
            json={
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
                _data = typing.cast(
                    PostV3ConnectionsGoogleDocsTokenResponse,
                    parse_obj_as(
                        type_=PostV3ConnectionsGoogleDocsTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
