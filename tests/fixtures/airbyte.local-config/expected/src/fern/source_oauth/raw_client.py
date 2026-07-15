

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.complete_o_auth_response import CompleteOAuthResponse
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.known_exception_info import KnownExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.o_auth_consent_read import OAuthConsentRead
from ..types.o_auth_input_configuration import OAuthInputConfiguration
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_id import SourceId
from ..types.workspace_id import WorkspaceId


OMIT = typing.cast(typing.Any, ...)


class RawSourceOauthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def complete_source_o_auth(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        query_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompleteOAuthResponse]:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        query_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The query parameters present in the redirect URL after a user granted consent e.g auth code

        redirect_url : typing.Optional[str]
            When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompleteOAuthResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/source_oauths/complete_oauth",
            method="POST",
            json={
                "oAuthInputConfiguration": o_auth_input_configuration,
                "queryParams": query_params,
                "redirectUrl": redirect_url,
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "workspaceId": workspace_id,
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
                    CompleteOAuthResponse,
                    parse_obj_as(
                        type_=CompleteOAuthResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_source_o_auth_consent(
        self,
        *,
        redirect_url: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OAuthConsentRead]:
        """
        Parameters
        ----------
        redirect_url : str
            The url to redirect to after getting the user consent

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OAuthConsentRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/source_oauths/get_consent_url",
            method="POST",
            json={
                "oAuthInputConfiguration": o_auth_input_configuration,
                "redirectUrl": redirect_url,
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "workspaceId": workspace_id,
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
                    OAuthConsentRead,
                    parse_obj_as(
                        type_=OAuthConsentRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_instancewide_source_oauth_params(
        self,
        *,
        params: typing.Dict[str, typing.Optional[typing.Any]],
        source_definition_id: SourceDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        params : typing.Dict[str, typing.Optional[typing.Any]]

        source_definition_id : SourceDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/source_oauths/oauth_params/create",
            method="POST",
            json={
                "params": params,
                "sourceDefinitionId": source_definition_id,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        KnownExceptionInfo,
                        parse_obj_as(
                            type_=KnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSourceOauthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def complete_source_o_auth(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        query_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompleteOAuthResponse]:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        query_params : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The query parameters present in the redirect URL after a user granted consent e.g auth code

        redirect_url : typing.Optional[str]
            When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompleteOAuthResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/source_oauths/complete_oauth",
            method="POST",
            json={
                "oAuthInputConfiguration": o_auth_input_configuration,
                "queryParams": query_params,
                "redirectUrl": redirect_url,
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "workspaceId": workspace_id,
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
                    CompleteOAuthResponse,
                    parse_obj_as(
                        type_=CompleteOAuthResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_source_o_auth_consent(
        self,
        *,
        redirect_url: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        o_auth_input_configuration: typing.Optional[OAuthInputConfiguration] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OAuthConsentRead]:
        """
        Parameters
        ----------
        redirect_url : str
            The url to redirect to after getting the user consent

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        o_auth_input_configuration : typing.Optional[OAuthInputConfiguration]

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OAuthConsentRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/source_oauths/get_consent_url",
            method="POST",
            json={
                "oAuthInputConfiguration": o_auth_input_configuration,
                "redirectUrl": redirect_url,
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "workspaceId": workspace_id,
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
                    OAuthConsentRead,
                    parse_obj_as(
                        type_=OAuthConsentRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_instancewide_source_oauth_params(
        self,
        *,
        params: typing.Dict[str, typing.Optional[typing.Any]],
        source_definition_id: SourceDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        params : typing.Dict[str, typing.Optional[typing.Any]]

        source_definition_id : SourceDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/source_oauths/oauth_params/create",
            method="POST",
            json={
                "params": params,
                "sourceDefinitionId": source_definition_id,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        KnownExceptionInfo,
                        parse_obj_as(
                            type_=KnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
