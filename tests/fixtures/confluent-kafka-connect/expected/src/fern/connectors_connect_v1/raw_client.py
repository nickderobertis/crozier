

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
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.connect_v1connector import ConnectV1Connector
from ..types.connect_v1connector_error import ConnectV1ConnectorError
from ..types.connect_v1connector_expansion_map import ConnectV1ConnectorExpansionMap
from ..types.connect_v1connector_with_offsets import ConnectV1ConnectorWithOffsets
from ..types.inline_response200 import InlineResponse200
from .types.get_connectv1connector_config_response import GetConnectv1ConnectorConfigResponse
from .types.inline_object_config import InlineObjectConfig
from .types.inline_object_offsets_item import InlineObjectOffsetsItem
from .types.list_connectv1connectors_with_expansions_request_expand import (
    ListConnectv1ConnectorsWithExpansionsRequestExpand,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConnectorsConnectV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_connectv1connectors(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve a list of "names" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.

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
        HttpResponse[typing.List[str]]
            Connector.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def create_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[InlineObjectConfig] = OMIT,
        offsets: typing.Optional[typing.Sequence[InlineObjectOffsetsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectV1ConnectorWithOffsets]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Create a new connector. Returns the new connector information if successful.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        name : typing.Optional[str]
            Name of the connector to create.

        config : typing.Optional[InlineObjectConfig]
            Configuration parameters for the connector. All values should be strings.

        offsets : typing.Optional[typing.Sequence[InlineObjectOffsetsItem]]
            Array of offsets which are categorised into partitions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectV1ConnectorWithOffsets]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors",
            method="POST",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=InlineObjectConfig, direction="write"
                ),
                "offsets": convert_and_respect_annotation_metadata(
                    object_=offsets, annotation=typing.Sequence[InlineObjectOffsetsItem], direction="write"
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
                    ConnectV1ConnectorWithOffsets,
                    parse_obj_as(
                        type_=ConnectV1ConnectorWithOffsets,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def list_connectv1connectors_with_expansions(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        expand: typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectV1ConnectorExpansionMap]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        expand : typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand]
            - id : Returns metadata of each connector such as id and id type.
            - info : Returns metadata of each connector such as the configuration, task
            information, and type of connector.
            - status : Returns additional state information of each connector including their status and tasks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectV1ConnectorExpansionMap]
            Connector.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors?expand=info,status,id",
            method="GET",
            params={
                "expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectV1ConnectorExpansionMap,
                    parse_obj_as(
                        type_=ConnectV1ConnectorExpansionMap,
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

    def get_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConnectv1ConnectorConfigResponse]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get the configuration for the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetConnectv1ConnectorConfigResponse]
            Connector.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectv1ConnectorConfigResponse,
                    parse_obj_as(
                        type_=GetConnectv1ConnectorConfigResponse,
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

    def create_or_update_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        connector_class: str,
        name: str,
        kafka_api_key: str,
        kafka_api_secret: str,
        confluent_connector_type: typing.Optional[str] = OMIT,
        confluent_custom_plugin_id: typing.Optional[str] = OMIT,
        confluent_custom_connection_endpoints: typing.Optional[str] = OMIT,
        confluent_custom_schema_registry_auto: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectV1Connector]:
        """
        Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        connector_class : str
            \\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name. E.g. BigQuerySink, GcsSink, etc.

        name : str
            Name or alias of the class (plugin) for this connector.

        kafka_api_key : str
            The kafka cluster api key.

        kafka_api_secret : str
            The kafka cluster api secret key.

        confluent_connector_type : typing.Optional[str]
            \\[Required for Custom Connector\\] The connector type.

        confluent_custom_plugin_id : typing.Optional[str]
            \\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`

        confluent_custom_connection_endpoints : typing.Optional[str]
            \\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.

        confluent_custom_schema_registry_auto : typing.Optional[str]
            \\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectV1Connector]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}/config",
            method="PUT",
            json={
                "connector.class": connector_class,
                "name": name,
                "kafka.api.key": kafka_api_key,
                "kafka.api.secret": kafka_api_secret,
                "confluent.connector.type": confluent_connector_type,
                "confluent.custom.plugin.id": confluent_custom_plugin_id,
                "confluent.custom.connection.endpoints": confluent_custom_connection_endpoints,
                "confluent.custom.schema.registry.auto": confluent_custom_schema_registry_auto,
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
                    ConnectV1Connector,
                    parse_obj_as(
                        type_=ConnectV1Connector,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def read_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectV1Connector]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get information about the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectV1Connector]
            Connector.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectV1Connector,
                    parse_obj_as(
                        type_=ConnectV1Connector,
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

    def delete_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InlineResponse200]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Delete a connector. Halts all tasks and deletes the connector configuration.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InlineResponse200]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InlineResponse200,
                    parse_obj_as(
                        type_=InlineResponse200,
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


class AsyncRawConnectorsConnectV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_connectv1connectors(
        self, environment_id: str, kafka_cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve a list of "names" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.

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
        AsyncHttpResponse[typing.List[str]]
            Connector.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def create_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[InlineObjectConfig] = OMIT,
        offsets: typing.Optional[typing.Sequence[InlineObjectOffsetsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectV1ConnectorWithOffsets]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Create a new connector. Returns the new connector information if successful.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        name : typing.Optional[str]
            Name of the connector to create.

        config : typing.Optional[InlineObjectConfig]
            Configuration parameters for the connector. All values should be strings.

        offsets : typing.Optional[typing.Sequence[InlineObjectOffsetsItem]]
            Array of offsets which are categorised into partitions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectV1ConnectorWithOffsets]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors",
            method="POST",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=InlineObjectConfig, direction="write"
                ),
                "offsets": convert_and_respect_annotation_metadata(
                    object_=offsets, annotation=typing.Sequence[InlineObjectOffsetsItem], direction="write"
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
                    ConnectV1ConnectorWithOffsets,
                    parse_obj_as(
                        type_=ConnectV1ConnectorWithOffsets,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def list_connectv1connectors_with_expansions(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        *,
        expand: typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectV1ConnectorExpansionMap]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        expand : typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand]
            - id : Returns metadata of each connector such as id and id type.
            - info : Returns metadata of each connector such as the configuration, task
            information, and type of connector.
            - status : Returns additional state information of each connector including their status and tasks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectV1ConnectorExpansionMap]
            Connector.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors?expand=info,status,id",
            method="GET",
            params={
                "expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectV1ConnectorExpansionMap,
                    parse_obj_as(
                        type_=ConnectV1ConnectorExpansionMap,
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

    async def get_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetConnectv1ConnectorConfigResponse]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get the configuration for the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetConnectv1ConnectorConfigResponse]
            Connector.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectv1ConnectorConfigResponse,
                    parse_obj_as(
                        type_=GetConnectv1ConnectorConfigResponse,
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

    async def create_or_update_connectv1connector_config(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        connector_class: str,
        name: str,
        kafka_api_key: str,
        kafka_api_secret: str,
        confluent_connector_type: typing.Optional[str] = OMIT,
        confluent_custom_plugin_id: typing.Optional[str] = OMIT,
        confluent_custom_connection_endpoints: typing.Optional[str] = OMIT,
        confluent_custom_schema_registry_auto: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectV1Connector]:
        """
        Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        connector_class : str
            \\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name. E.g. BigQuerySink, GcsSink, etc.

        name : str
            Name or alias of the class (plugin) for this connector.

        kafka_api_key : str
            The kafka cluster api key.

        kafka_api_secret : str
            The kafka cluster api secret key.

        confluent_connector_type : typing.Optional[str]
            \\[Required for Custom Connector\\] The connector type.

        confluent_custom_plugin_id : typing.Optional[str]
            \\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`

        confluent_custom_connection_endpoints : typing.Optional[str]
            \\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.

        confluent_custom_schema_registry_auto : typing.Optional[str]
            \\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectV1Connector]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}/config",
            method="PUT",
            json={
                "connector.class": connector_class,
                "name": name,
                "kafka.api.key": kafka_api_key,
                "kafka.api.secret": kafka_api_secret,
                "confluent.connector.type": confluent_connector_type,
                "confluent.custom.plugin.id": confluent_custom_plugin_id,
                "confluent.custom.connection.endpoints": confluent_custom_connection_endpoints,
                "confluent.custom.schema.registry.auto": confluent_custom_schema_registry_auto,
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
                    ConnectV1Connector,
                    parse_obj_as(
                        type_=ConnectV1Connector,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def read_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectV1Connector]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Get information about the connector.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectV1Connector]
            Connector.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectV1Connector,
                    parse_obj_as(
                        type_=ConnectV1Connector,
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

    async def delete_connectv1connector(
        self,
        environment_id: str,
        kafka_cluster_id: str,
        connector_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InlineResponse200]:
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

        Delete a connector. Halts all tasks and deletes the connector configuration.

        Parameters
        ----------
        environment_id : str
            The unique identifier of the environment this resource belongs to.

        kafka_cluster_id : str
            The unique identifier for the Kafka cluster.

        connector_name : str
            The unique name of the connector.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InlineResponse200]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connect/v1/environments/{encode_path_param(environment_id)}/clusters/{encode_path_param(kafka_cluster_id)}/connectors/{encode_path_param(connector_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InlineResponse200,
                    parse_obj_as(
                        type_=InlineResponse200,
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
