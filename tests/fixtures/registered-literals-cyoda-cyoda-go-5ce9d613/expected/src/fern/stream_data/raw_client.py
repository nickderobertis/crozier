

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..types.abstract_condition import AbstractCondition
from ..types.index_configuration_dto import IndexConfigurationDto
from ..types.query_plan_dto import QueryPlanDto
from ..types.report_alias_def import ReportAliasDef
from ..types.stream_data_config_def import StreamDataConfigDef
from ..types.stream_data_config_def_container import StreamDataConfigDefContainer
from ..types.stream_data_def import StreamDataDef
from ..types.stream_data_delete_result import StreamDataDeleteResult
from ..types.stream_data_fetch_result import StreamDataFetchResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStreamDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StreamDataConfigDef]:
        """
        Retrieves a specific stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDataConfigDef]
            The requested stream data configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="GET",
            params={
                "configId": config_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDef,
                    parse_obj_as(
                        type_=StreamDataConfigDef,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def save_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates and persists a new stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            UUID of the created configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="POST",
            json={
                "streamDataDef": convert_and_respect_annotation_metadata(
                    object_=stream_data_def, annotation=StreamDataDef, direction="write"
                ),
                "name": name,
                "description": description,
                "createDate": create_date,
                "owner": owner,
                "id": id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def update_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates an existing stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="PUT",
            json={
                "streamDataDef": convert_and_respect_annotation_metadata(
                    object_=stream_data_def, annotation=StreamDataDef, direction="write"
                ),
                "name": name,
                "description": description,
                "createDate": create_date,
                "owner": owner,
                "id": id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def delete_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="DELETE",
            params={
                "configId": config_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_all_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[StreamDataConfigDef]]:
        """
        Returns all available stream data configurations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[StreamDataConfigDef]]
            List of all stream data configurations
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[StreamDataConfigDef],
                    parse_obj_as(
                        type_=typing.List[StreamDataConfigDef],
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def delete(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StreamDataDeleteResult]:
        """
        Deletes entities matching the stream data request criteria.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDataDeleteResult]
            Deletion result with counts and any errors
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/delete",
            method="DELETE",
            json={
                "sdDef": convert_and_respect_annotation_metadata(
                    object_=sd_def, annotation=StreamDataDef, direction="write"
                ),
                "pointTime": point_time,
                "offset": offset,
                "length": length,
                "fromPosIndex": from_pos_index,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataDeleteResult,
                    parse_obj_as(
                        type_=StreamDataDeleteResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def export_all1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StreamDataConfigDefContainer]:
        """
        Exports all stream data configurations as a container for backup or transfer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDataConfigDefContainer]
            Container with all stream data configurations
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/export-all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDefContainer,
                    parse_obj_as(
                        type_=StreamDataConfigDefContainer,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def export_all(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StreamDataConfigDefContainer]:
        """
        Exports all stream data configurations associated with a specific entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDataConfigDefContainer]
            Container with stream data configurations for the entity class
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/export-by-class",
            method="GET",
            params={
                "entityClass": entity_class,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDefContainer,
                    parse_obj_as(
                        type_=StreamDataConfigDefContainer,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def export_by_ids(
        self,
        *,
        include_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StreamDataConfigDefContainer]:
        """
        Exports specific stream data configurations identified by their UUIDs.

        Parameters
        ----------
        include_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of configuration UUIDs to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDataConfigDefContainer]
            Container with the requested stream data configurations
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/export-by-ids",
            method="GET",
            params={
                "includeIds": include_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDefContainer,
                    parse_obj_as(
                        type_=StreamDataConfigDefContainer,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_stream_data(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StreamDataFetchResult]:
        """
        Retrieves paginated stream data based on the provided request definition, including conditions, columns, and pagination parameters.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamDataFetchResult]
            Stream data fetch result containing rows and pagination info
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/get",
            method="POST",
            json={
                "sdDef": convert_and_respect_annotation_metadata(
                    object_=sd_def, annotation=StreamDataDef, direction="write"
                ),
                "pointTime": point_time,
                "offset": offset,
                "length": length,
                "fromPosIndex": from_pos_index,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataFetchResult,
                    parse_obj_as(
                        type_=StreamDataFetchResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def import_container(
        self,
        *,
        fail_on_exists: typing.Optional[bool] = None,
        data: typing.Optional[typing.Sequence[StreamDataConfigDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Imports stream data configurations from a container. Can optionally fail if configurations already exist.

        Parameters
        ----------
        fail_on_exists : typing.Optional[bool]
            If true, fail when a configuration already exists; if false, skip existing configurations

        data : typing.Optional[typing.Sequence[StreamDataConfigDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/import",
            method="POST",
            params={
                "failOnExists": fail_on_exists,
            },
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Sequence[StreamDataConfigDef], direction="write"
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
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_indexs(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[IndexConfigurationDto]]:
        """
        Returns all index configurations available for the specified entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[IndexConfigurationDto]]
            List of index configurations
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/index/list",
            method="GET",
            params={
                "entityClass": entity_class,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[IndexConfigurationDto],
                    parse_obj_as(
                        type_=typing.List[IndexConfigurationDto],
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_query_plan(
        self,
        *,
        condition: typing.Optional[AbstractCondition] = OMIT,
        alias_defs: typing.Optional[typing.Sequence[ReportAliasDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryPlanDto]:
        """
        Returns the original and optimized query execution plan for the given entity class, condition, and alias definitions.

        Parameters
        ----------
        condition : typing.Optional[AbstractCondition]

        alias_defs : typing.Optional[typing.Sequence[ReportAliasDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryPlanDto]
            Query plan with original and optimized versions
        """
        _response = self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/query-plan",
            method="POST",
            json={
                "condition": convert_and_respect_annotation_metadata(
                    object_=condition, annotation=AbstractCondition, direction="write"
                ),
                "aliasDefs": convert_and_respect_annotation_metadata(
                    object_=alias_defs, annotation=typing.Sequence[ReportAliasDef], direction="write"
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
                    QueryPlanDto,
                    parse_obj_as(
                        type_=QueryPlanDto,
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncRawStreamDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StreamDataConfigDef]:
        """
        Retrieves a specific stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDataConfigDef]
            The requested stream data configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="GET",
            params={
                "configId": config_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDef,
                    parse_obj_as(
                        type_=StreamDataConfigDef,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def save_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates and persists a new stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            UUID of the created configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="POST",
            json={
                "streamDataDef": convert_and_respect_annotation_metadata(
                    object_=stream_data_def, annotation=StreamDataDef, direction="write"
                ),
                "name": name,
                "description": description,
                "createDate": create_date,
                "owner": owner,
                "id": id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def update_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates an existing stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="PUT",
            json={
                "streamDataDef": convert_and_respect_annotation_metadata(
                    object_=stream_data_def, annotation=StreamDataDef, direction="write"
                ),
                "name": name,
                "description": description,
                "createDate": create_date,
                "owner": owner,
                "id": id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def delete_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config",
            method="DELETE",
            params={
                "configId": config_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_all_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[StreamDataConfigDef]]:
        """
        Returns all available stream data configurations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[StreamDataConfigDef]]
            List of all stream data configurations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/config/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[StreamDataConfigDef],
                    parse_obj_as(
                        type_=typing.List[StreamDataConfigDef],
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def delete(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StreamDataDeleteResult]:
        """
        Deletes entities matching the stream data request criteria.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDataDeleteResult]
            Deletion result with counts and any errors
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/delete",
            method="DELETE",
            json={
                "sdDef": convert_and_respect_annotation_metadata(
                    object_=sd_def, annotation=StreamDataDef, direction="write"
                ),
                "pointTime": point_time,
                "offset": offset,
                "length": length,
                "fromPosIndex": from_pos_index,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataDeleteResult,
                    parse_obj_as(
                        type_=StreamDataDeleteResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def export_all1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StreamDataConfigDefContainer]:
        """
        Exports all stream data configurations as a container for backup or transfer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDataConfigDefContainer]
            Container with all stream data configurations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/export-all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDefContainer,
                    parse_obj_as(
                        type_=StreamDataConfigDefContainer,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def export_all(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StreamDataConfigDefContainer]:
        """
        Exports all stream data configurations associated with a specific entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDataConfigDefContainer]
            Container with stream data configurations for the entity class
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/export-by-class",
            method="GET",
            params={
                "entityClass": entity_class,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDefContainer,
                    parse_obj_as(
                        type_=StreamDataConfigDefContainer,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def export_by_ids(
        self,
        *,
        include_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StreamDataConfigDefContainer]:
        """
        Exports specific stream data configurations identified by their UUIDs.

        Parameters
        ----------
        include_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of configuration UUIDs to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDataConfigDefContainer]
            Container with the requested stream data configurations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/export-by-ids",
            method="GET",
            params={
                "includeIds": include_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataConfigDefContainer,
                    parse_obj_as(
                        type_=StreamDataConfigDefContainer,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_stream_data(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StreamDataFetchResult]:
        """
        Retrieves paginated stream data based on the provided request definition, including conditions, columns, and pagination parameters.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamDataFetchResult]
            Stream data fetch result containing rows and pagination info
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/get",
            method="POST",
            json={
                "sdDef": convert_and_respect_annotation_metadata(
                    object_=sd_def, annotation=StreamDataDef, direction="write"
                ),
                "pointTime": point_time,
                "offset": offset,
                "length": length,
                "fromPosIndex": from_pos_index,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamDataFetchResult,
                    parse_obj_as(
                        type_=StreamDataFetchResult,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def import_container(
        self,
        *,
        fail_on_exists: typing.Optional[bool] = None,
        data: typing.Optional[typing.Sequence[StreamDataConfigDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Imports stream data configurations from a container. Can optionally fail if configurations already exist.

        Parameters
        ----------
        fail_on_exists : typing.Optional[bool]
            If true, fail when a configuration already exists; if false, skip existing configurations

        data : typing.Optional[typing.Sequence[StreamDataConfigDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/import",
            method="POST",
            params={
                "failOnExists": fail_on_exists,
            },
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Sequence[StreamDataConfigDef], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_indexs(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[IndexConfigurationDto]]:
        """
        Returns all index configurations available for the specified entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[IndexConfigurationDto]]
            List of index configurations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/index/list",
            method="GET",
            params={
                "entityClass": entity_class,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[IndexConfigurationDto],
                    parse_obj_as(
                        type_=typing.List[IndexConfigurationDto],
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_query_plan(
        self,
        *,
        condition: typing.Optional[AbstractCondition] = OMIT,
        alias_defs: typing.Optional[typing.Sequence[ReportAliasDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryPlanDto]:
        """
        Returns the original and optimized query execution plan for the given entity class, condition, and alias definitions.

        Parameters
        ----------
        condition : typing.Optional[AbstractCondition]

        alias_defs : typing.Optional[typing.Sequence[ReportAliasDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryPlanDto]
            Query plan with original and optimized versions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "platform-api/stream-data/query-plan",
            method="POST",
            json={
                "condition": convert_and_respect_annotation_metadata(
                    object_=condition, annotation=AbstractCondition, direction="write"
                ),
                "aliasDefs": convert_and_respect_annotation_metadata(
                    object_=alias_defs, annotation=typing.Sequence[ReportAliasDef], direction="write"
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
                    QueryPlanDto,
                    parse_obj_as(
                        type_=QueryPlanDto,
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
            if _response.status_code == 409:
                raise ConflictError(
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
