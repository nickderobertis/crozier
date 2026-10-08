

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.connect_v1connector_error import ConnectV1ConnectorError
from ..types.inline_response2002 import InlineResponse2002
from ..types.inline_response2003 import InlineResponse2003
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagedConnectorPluginsConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_connectv1connector_plugins(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[InlineResponse2002]]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Return a list of Managed Connector plugins installed in the Kafka Connect cluster.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[InlineResponse2002]]
            Connector Plugin.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connector-plugins",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InlineResponse2002],
                    parse_obj_as(
                        type_=typing.List[InlineResponse2002],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def validate_connectv1connector_plugin(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        plugin_name: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InlineResponse2003]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        plugin_name : str
            The unique name of the connector plugin.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InlineResponse2003]
            Connector Plugin.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connector-plugins/{encode_path_param(plugin_name)}/config/validate",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InlineResponse2003,
                    parse_obj_as(
                        type_=InlineResponse2003,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawManagedConnectorPluginsConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_connectv1connector_plugins(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[InlineResponse2002]]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Return a list of Managed Connector plugins installed in the Kafka Connect cluster.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[InlineResponse2002]]
            Connector Plugin.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connector-plugins",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InlineResponse2002],
                    parse_obj_as(
                        type_=typing.List[InlineResponse2002],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def validate_connectv1connector_plugin(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        plugin_name: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InlineResponse2003]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        plugin_name : str
            The unique name of the connector plugin.

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InlineResponse2003]
            Connector Plugin.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connector-plugins/{encode_path_param(plugin_name)}/config/validate",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InlineResponse2003,
                    parse_obj_as(
                        type_=InlineResponse2003,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConnectV1ConnectorError,
                        parse_obj_as(
                            type_=ConnectV1ConnectorError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
