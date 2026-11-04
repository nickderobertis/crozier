

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.enable_ask_ai_response import EnableAskAiResponse
from ..types.get_settings_response import GetSettingsResponse
from ..types.http_validation_error import HttpValidationError
from ..types.toggle_ask_ai_response import ToggleAskAiResponse
from ..types.toggle_status_response import ToggleStatusResponse
from .types.reindex_callback_request_status import ReindexCallbackRequestStatus
from .types.toggle_ask_ai_request_locations_item import ToggleAskAiRequestLocationsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_docs_settings(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSettingsResponse]:
        """
        Get settings for a domain and organization.

        Parameters
        ----------
        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSettingsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ask-ai/docs",
            method="GET",
            params={
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSettingsResponse,
                    parse_obj_as(
                        type_=GetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def enable_ask_ai(
        self,
        *,
        domains: typing.Sequence[str],
        org_name: str,
        locations: typing.Sequence[str],
        preview: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnableAskAiResponse]:
        """
        Enable Ask AI for multiple domains with specified locations and trigger reindex.

        Args:
            request: Request containing domains, org_name, and locations to enable

        Parameters
        ----------
        domains : typing.Sequence[str]
            List of domains to enable Ask AI for

        org_name : str
            Organization name

        locations : typing.Sequence[str]
            List of locations to enable (docs, slack)

        preview : typing.Optional[bool]
            Whether this is a preview domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnableAskAiResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ask-ai/enable",
            method="POST",
            json={
                "domains": domains,
                "org_name": org_name,
                "locations": locations,
                "preview": preview,
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
                    EnableAskAiResponse,
                    parse_obj_as(
                        type_=EnableAskAiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def toggle_ask_ai(
        self,
        *,
        domain: str,
        org_name: str,
        preview: typing.Optional[bool] = None,
        locations: typing.Optional[typing.Sequence[ToggleAskAiRequestLocationsItem]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToggleAskAiResponse]:
        """
        Toggle Ask AI setting and return job_id for tracking.

        Args:
            domain: Domain to toggle Ask AI for
            org_name: Organization name
            preview: Whether this is a preview deployment
            locations: Optional list of locations to enable. Valid values: docs, slack

        Parameters
        ----------
        domain : str

        org_name : str

        preview : typing.Optional[bool]

        locations : typing.Optional[typing.Sequence[ToggleAskAiRequestLocationsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToggleAskAiResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ask-ai/toggle",
            method="POST",
            params={
                "domain": domain,
                "org_name": org_name,
                "preview": preview,
                "locations": locations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleAskAiResponse,
                    parse_obj_as(
                        type_=ToggleAskAiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def reindex_ask_ai(
        self,
        *,
        domain: str,
        org_name: typing.Optional[str] = None,
        force_full_reindex: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToggleAskAiResponse]:
        """
        Manually trigger reindex for an already enabled Ask AI setup.

        Args:
            domain: Domain to reindex
            org_name: Organization name (unused, kept for backwards compatibility)
            force_full_reindex: If True, deletes all existing data and performs a fresh full index

        Parameters
        ----------
        domain : str

        org_name : typing.Optional[str]

        force_full_reindex : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToggleAskAiResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ask-ai/reindex",
            method="POST",
            params={
                "domain": domain,
                "org_name": org_name,
                "force_full_reindex": force_full_reindex,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleAskAiResponse,
                    parse_obj_as(
                        type_=ToggleAskAiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_toggle_status(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ToggleStatusResponse]:
        """
        Get the status of Ask AI toggle operation.

        Parameters
        ----------
        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToggleStatusResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ask-ai/toggle/status",
            method="GET",
            params={
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleStatusResponse,
                    parse_obj_as(
                        type_=ToggleStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def reindex_callback(
        self,
        *,
        status: ReindexCallbackRequestStatus,
        source_message_id: str,
        domain: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Handle callback from SQS reindexing worker when reindex completes.

        Parameters
        ----------
        status : ReindexCallbackRequestStatus

        source_message_id : str

        domain : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ask-ai/reindex-callback",
            method="POST",
            json={
                "status": status,
                "sourceMessageId": source_message_id,
                "domain": domain,
                "url": url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_docs_settings(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSettingsResponse]:
        """
        Get settings for a domain and organization.

        Parameters
        ----------
        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSettingsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ask-ai/docs",
            method="GET",
            params={
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSettingsResponse,
                    parse_obj_as(
                        type_=GetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def enable_ask_ai(
        self,
        *,
        domains: typing.Sequence[str],
        org_name: str,
        locations: typing.Sequence[str],
        preview: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnableAskAiResponse]:
        """
        Enable Ask AI for multiple domains with specified locations and trigger reindex.

        Args:
            request: Request containing domains, org_name, and locations to enable

        Parameters
        ----------
        domains : typing.Sequence[str]
            List of domains to enable Ask AI for

        org_name : str
            Organization name

        locations : typing.Sequence[str]
            List of locations to enable (docs, slack)

        preview : typing.Optional[bool]
            Whether this is a preview domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnableAskAiResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ask-ai/enable",
            method="POST",
            json={
                "domains": domains,
                "org_name": org_name,
                "locations": locations,
                "preview": preview,
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
                    EnableAskAiResponse,
                    parse_obj_as(
                        type_=EnableAskAiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def toggle_ask_ai(
        self,
        *,
        domain: str,
        org_name: str,
        preview: typing.Optional[bool] = None,
        locations: typing.Optional[typing.Sequence[ToggleAskAiRequestLocationsItem]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToggleAskAiResponse]:
        """
        Toggle Ask AI setting and return job_id for tracking.

        Args:
            domain: Domain to toggle Ask AI for
            org_name: Organization name
            preview: Whether this is a preview deployment
            locations: Optional list of locations to enable. Valid values: docs, slack

        Parameters
        ----------
        domain : str

        org_name : str

        preview : typing.Optional[bool]

        locations : typing.Optional[typing.Sequence[ToggleAskAiRequestLocationsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToggleAskAiResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ask-ai/toggle",
            method="POST",
            params={
                "domain": domain,
                "org_name": org_name,
                "preview": preview,
                "locations": locations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleAskAiResponse,
                    parse_obj_as(
                        type_=ToggleAskAiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def reindex_ask_ai(
        self,
        *,
        domain: str,
        org_name: typing.Optional[str] = None,
        force_full_reindex: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToggleAskAiResponse]:
        """
        Manually trigger reindex for an already enabled Ask AI setup.

        Args:
            domain: Domain to reindex
            org_name: Organization name (unused, kept for backwards compatibility)
            force_full_reindex: If True, deletes all existing data and performs a fresh full index

        Parameters
        ----------
        domain : str

        org_name : typing.Optional[str]

        force_full_reindex : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToggleAskAiResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ask-ai/reindex",
            method="POST",
            params={
                "domain": domain,
                "org_name": org_name,
                "force_full_reindex": force_full_reindex,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleAskAiResponse,
                    parse_obj_as(
                        type_=ToggleAskAiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_toggle_status(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ToggleStatusResponse]:
        """
        Get the status of Ask AI toggle operation.

        Parameters
        ----------
        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToggleStatusResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ask-ai/toggle/status",
            method="GET",
            params={
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleStatusResponse,
                    parse_obj_as(
                        type_=ToggleStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def reindex_callback(
        self,
        *,
        status: ReindexCallbackRequestStatus,
        source_message_id: str,
        domain: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Handle callback from SQS reindexing worker when reindex completes.

        Parameters
        ----------
        status : ReindexCallbackRequestStatus

        source_message_id : str

        domain : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ask-ai/reindex-callback",
            method="POST",
            json={
                "status": status,
                "sourceMessageId": source_message_id,
                "domain": domain,
                "url": url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
