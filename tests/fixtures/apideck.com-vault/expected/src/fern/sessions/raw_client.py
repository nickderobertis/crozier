

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
from ..types.consumer_metadata import ConsumerMetadata
from ..types.create_session_response import CreateSessionResponse
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from .types.session_settings import SessionSettings
from .types.session_theme import SessionTheme


OMIT = typing.cast(typing.Any, ...)


class RawSessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        apideck_consumer_id: str,
        consumer_metadata: typing.Optional[ConsumerMetadata] = OMIT,
        custom_consumer_settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        settings: typing.Optional[SessionSettings] = OMIT,
        theme: typing.Optional[SessionTheme] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSessionResponse]:
        """
        Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned
        URL to allow temporary access to manage their integrations and settings.

        Note: This is a short lived token that will expire after 1 hour (TTL: 3600).

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        consumer_metadata : typing.Optional[ConsumerMetadata]

        custom_consumer_settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Custom consumer settings that are passed as part of the session.

        redirect_uri : typing.Optional[str]
            The URL to redirect the user to after the session has been configured.

        settings : typing.Optional[SessionSettings]
            Settings to change the way the Vault is displayed.

        theme : typing.Optional[SessionTheme]
            Theming options to change the look and feel of Vault.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSessionResponse]
            Session created
        """
        _response = self._client_wrapper.httpx_client.request(
            "vault/sessions",
            method="POST",
            json={
                "consumer_metadata": convert_and_respect_annotation_metadata(
                    object_=consumer_metadata, annotation=ConsumerMetadata, direction="write"
                ),
                "custom_consumer_settings": custom_consumer_settings,
                "redirect_uri": redirect_uri,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=SessionSettings, direction="write"
                ),
                "theme": convert_and_respect_annotation_metadata(
                    object_=theme, annotation=SessionTheme, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSessionResponse,
                    parse_obj_as(
                        type_=CreateSessionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        apideck_consumer_id: str,
        consumer_metadata: typing.Optional[ConsumerMetadata] = OMIT,
        custom_consumer_settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        settings: typing.Optional[SessionSettings] = OMIT,
        theme: typing.Optional[SessionTheme] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSessionResponse]:
        """
        Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned
        URL to allow temporary access to manage their integrations and settings.

        Note: This is a short lived token that will expire after 1 hour (TTL: 3600).

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        consumer_metadata : typing.Optional[ConsumerMetadata]

        custom_consumer_settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Custom consumer settings that are passed as part of the session.

        redirect_uri : typing.Optional[str]
            The URL to redirect the user to after the session has been configured.

        settings : typing.Optional[SessionSettings]
            Settings to change the way the Vault is displayed.

        theme : typing.Optional[SessionTheme]
            Theming options to change the look and feel of Vault.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSessionResponse]
            Session created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "vault/sessions",
            method="POST",
            json={
                "consumer_metadata": convert_and_respect_annotation_metadata(
                    object_=consumer_metadata, annotation=ConsumerMetadata, direction="write"
                ),
                "custom_consumer_settings": custom_consumer_settings,
                "redirect_uri": redirect_uri,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=SessionSettings, direction="write"
                ),
                "theme": convert_and_respect_annotation_metadata(
                    object_=theme, annotation=SessionTheme, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSessionResponse,
                    parse_obj_as(
                        type_=CreateSessionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
