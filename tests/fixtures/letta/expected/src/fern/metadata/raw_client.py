

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from .types.metadata_get_status_response import MetadataGetStatusResponse
from .types.metadata_get_user_response import MetadataGetUserResponse
from .types.metadata_retrieve_current_balances_response import MetadataRetrieveCurrentBalancesResponse
from .types.metadata_send_feedback_request_feature import MetadataSendFeedbackRequestFeature
from .types.metadata_send_feedback_response import MetadataSendFeedbackResponse
from .types.metadata_send_telemetry_request_events_item import MetadataSendTelemetryRequestEventsItem
from .types.metadata_send_telemetry_request_service import MetadataSendTelemetryRequestService
from .types.metadata_send_telemetry_response import MetadataSendTelemetryResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrievecurrentbalances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MetadataRetrieveCurrentBalancesResponse]:
        """
        Retrieve the current usage balances for the organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataRetrieveCurrentBalancesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/metadata/balance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataRetrieveCurrentBalancesResponse,
                    parse_obj_as(
                        type_=MetadataRetrieveCurrentBalancesResponse,
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

    def sendfeedback(
        self,
        *,
        message: str,
        feature: typing.Optional[MetadataSendFeedbackRequestFeature] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        settings: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MetadataSendFeedbackResponse]:
        """
        Send feedback from users to improve our services.

        Parameters
        ----------
        message : str

        feature : typing.Optional[MetadataSendFeedbackRequestFeature]

        agent_id : typing.Optional[str]

        session_id : typing.Optional[str]

        version : typing.Optional[str]

        platform : typing.Optional[str]

        settings : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataSendFeedbackResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/metadata/feedback",
            method="POST",
            json={
                "message": message,
                "feature": feature,
                "agent_id": agent_id,
                "session_id": session_id,
                "version": version,
                "platform": platform,
                "settings": settings,
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
                    MetadataSendFeedbackResponse,
                    parse_obj_as(
                        type_=MetadataSendFeedbackResponse,
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

    def sendtelemetry(
        self,
        *,
        service: MetadataSendTelemetryRequestService,
        events: typing.Sequence[MetadataSendTelemetryRequestEventsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MetadataSendTelemetryResponse]:
        """
        Send telemetry events for usage tracking and analysis.

        Parameters
        ----------
        service : MetadataSendTelemetryRequestService

        events : typing.Sequence[MetadataSendTelemetryRequestEventsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataSendTelemetryResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/metadata/telemetry",
            method="POST",
            json={
                "service": service,
                "events": convert_and_respect_annotation_metadata(
                    object_=events,
                    annotation=typing.Sequence[MetadataSendTelemetryRequestEventsItem],
                    direction="write",
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
                    MetadataSendTelemetryResponse,
                    parse_obj_as(
                        type_=MetadataSendTelemetryResponse,
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

    def getstatus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MetadataGetStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataGetStatusResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/metadata/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataGetStatusResponse,
                    parse_obj_as(
                        type_=MetadataGetStatusResponse,
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

    def getuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MetadataGetUserResponse]:
        """
        Retrieve information about the current authenticated user including email, name, organization, and current project.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetadataGetUserResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/metadata/user",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataGetUserResponse,
                    parse_obj_as(
                        type_=MetadataGetUserResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrievecurrentbalances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MetadataRetrieveCurrentBalancesResponse]:
        """
        Retrieve the current usage balances for the organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataRetrieveCurrentBalancesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/metadata/balance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataRetrieveCurrentBalancesResponse,
                    parse_obj_as(
                        type_=MetadataRetrieveCurrentBalancesResponse,
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

    async def sendfeedback(
        self,
        *,
        message: str,
        feature: typing.Optional[MetadataSendFeedbackRequestFeature] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        settings: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MetadataSendFeedbackResponse]:
        """
        Send feedback from users to improve our services.

        Parameters
        ----------
        message : str

        feature : typing.Optional[MetadataSendFeedbackRequestFeature]

        agent_id : typing.Optional[str]

        session_id : typing.Optional[str]

        version : typing.Optional[str]

        platform : typing.Optional[str]

        settings : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataSendFeedbackResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/metadata/feedback",
            method="POST",
            json={
                "message": message,
                "feature": feature,
                "agent_id": agent_id,
                "session_id": session_id,
                "version": version,
                "platform": platform,
                "settings": settings,
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
                    MetadataSendFeedbackResponse,
                    parse_obj_as(
                        type_=MetadataSendFeedbackResponse,
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

    async def sendtelemetry(
        self,
        *,
        service: MetadataSendTelemetryRequestService,
        events: typing.Sequence[MetadataSendTelemetryRequestEventsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MetadataSendTelemetryResponse]:
        """
        Send telemetry events for usage tracking and analysis.

        Parameters
        ----------
        service : MetadataSendTelemetryRequestService

        events : typing.Sequence[MetadataSendTelemetryRequestEventsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataSendTelemetryResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/metadata/telemetry",
            method="POST",
            json={
                "service": service,
                "events": convert_and_respect_annotation_metadata(
                    object_=events,
                    annotation=typing.Sequence[MetadataSendTelemetryRequestEventsItem],
                    direction="write",
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
                    MetadataSendTelemetryResponse,
                    parse_obj_as(
                        type_=MetadataSendTelemetryResponse,
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

    async def getstatus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MetadataGetStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataGetStatusResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/metadata/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataGetStatusResponse,
                    parse_obj_as(
                        type_=MetadataGetStatusResponse,
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

    async def getuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MetadataGetUserResponse]:
        """
        Retrieve information about the current authenticated user including email, name, organization, and current project.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetadataGetUserResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/metadata/user",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetadataGetUserResponse,
                    parse_obj_as(
                        type_=MetadataGetUserResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
