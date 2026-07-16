

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.data_exporter_config import DataExporterConfig
from ..types.data_exporter_config_config import DataExporterConfigConfig
from ..types.data_exporter_config_typ import DataExporterConfigTyp
from ..types.deleted import Deleted
from ..types.filtering import Filtering
from ..types.location import Location
from ..types.patch import Patch
from .types.create_bulk_data_exporter_configs_response_item import CreateBulkDataExporterConfigsResponseItem
from .types.deletebulk_data_exporter_config_response_item import DeletebulkDataExporterConfigResponseItem
from .types.patch_bulk_data_exporter_config_response_item import PatchBulkDataExporterConfigResponseItem
from .types.update_bulk_data_exporter_config_response_item import UpdateBulkDataExporterConfigResponseItem


OMIT = typing.cast(typing.Any, ...)


class RawDataExporterConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_all_data_exporters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[DataExporterConfig]]:
        """
        Get all data exporter configs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DataExporterConfig]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DataExporterConfig],
                    parse_obj_as(
                        type_=typing.List[DataExporterConfig],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def create_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DataExporterConfig]:
        """
        Create a new data exporter config

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs",
            method="POST",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def create_bulk_data_exporter_configs(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CreateBulkDataExporterConfigsResponseItem]]:
        """
        Create a new data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CreateBulkDataExporterConfigsResponseItem]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="POST",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
            },
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CreateBulkDataExporterConfigsResponseItem],
                    parse_obj_as(
                        type_=typing.List[CreateBulkDataExporterConfigsResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def update_bulk_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[UpdateBulkDataExporterConfigResponseItem]]:
        """
        Update a data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[UpdateBulkDataExporterConfigResponseItem]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="PUT",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
            },
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UpdateBulkDataExporterConfigResponseItem],
                    parse_obj_as(
                        type_=typing.List[UpdateBulkDataExporterConfigResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def deletebulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[DeletebulkDataExporterConfigResponseItem]]:
        """
        Delete a data exporter config

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DeletebulkDataExporterConfigResponseItem]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DeletebulkDataExporterConfigResponseItem],
                    parse_obj_as(
                        type_=typing.List[DeletebulkDataExporterConfigResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def patch_bulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PatchBulkDataExporterConfigResponseItem]]:
        """
        Update a data exporter configs with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PatchBulkDataExporterConfigResponseItem]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PatchBulkDataExporterConfigResponseItem],
                    parse_obj_as(
                        type_=typing.List[PatchBulkDataExporterConfigResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def data_exporter_template(
        self, *, type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DataExporterConfig]:
        """
        Get all data exporter configs

        Parameters
        ----------
        type : typing.Optional[str]
            The data exporter config type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_template",
            method="GET",
            params={
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def find_data_exporter_config_by_id(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DataExporterConfig]:
        """
        Get a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def update_data_exporter_config(
        self,
        data_exporter_config_id: str,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DataExporterConfig]:
        """
        Update a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="PUT",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
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
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_data_exporter_config(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
        """
        Delete a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def patch_data_exporter_config(
        self, data_exporter_config_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DataExporterConfig]:
        """
        Update a data exporter config with a diff

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawDataExporterConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find_all_data_exporters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[DataExporterConfig]]:
        """
        Get all data exporter configs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DataExporterConfig]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DataExporterConfig],
                    parse_obj_as(
                        type_=typing.List[DataExporterConfig],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def create_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DataExporterConfig]:
        """
        Create a new data exporter config

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs",
            method="POST",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def create_bulk_data_exporter_configs(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CreateBulkDataExporterConfigsResponseItem]]:
        """
        Create a new data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CreateBulkDataExporterConfigsResponseItem]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="POST",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
            },
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CreateBulkDataExporterConfigsResponseItem],
                    parse_obj_as(
                        type_=typing.List[CreateBulkDataExporterConfigsResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def update_bulk_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[UpdateBulkDataExporterConfigResponseItem]]:
        """
        Update a data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[UpdateBulkDataExporterConfigResponseItem]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="PUT",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
            },
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UpdateBulkDataExporterConfigResponseItem],
                    parse_obj_as(
                        type_=typing.List[UpdateBulkDataExporterConfigResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def deletebulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[DeletebulkDataExporterConfigResponseItem]]:
        """
        Delete a data exporter config

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DeletebulkDataExporterConfigResponseItem]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DeletebulkDataExporterConfigResponseItem],
                    parse_obj_as(
                        type_=typing.List[DeletebulkDataExporterConfigResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def patch_bulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PatchBulkDataExporterConfigResponseItem]]:
        """
        Update a data exporter configs with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PatchBulkDataExporterConfigResponseItem]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_bulk",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PatchBulkDataExporterConfigResponseItem],
                    parse_obj_as(
                        type_=typing.List[PatchBulkDataExporterConfigResponseItem],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def data_exporter_template(
        self, *, type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DataExporterConfig]:
        """
        Get all data exporter configs

        Parameters
        ----------
        type : typing.Optional[str]
            The data exporter config type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/data-exporter-configs/_template",
            method="GET",
            params={
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def find_data_exporter_config_by_id(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DataExporterConfig]:
        """
        Get a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def update_data_exporter_config(
        self,
        data_exporter_config_id: str,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DataExporterConfig]:
        """
        Update a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="PUT",
            json={
                "bufferSize": buffer_size,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=DataExporterConfigConfig, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "filtering": convert_and_respect_annotation_metadata(
                    object_=filtering, annotation=Filtering, direction="write"
                ),
                "groupDuration": group_duration,
                "groupSize": group_size,
                "id": id,
                "jsonWorkers": json_workers,
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
                ),
                "metadata": metadata,
                "name": name,
                "projection": projection,
                "sendWorkers": send_workers,
                "typ": typ,
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
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_data_exporter_config(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
        """
        Delete a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def patch_data_exporter_config(
        self, data_exporter_config_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DataExporterConfig]:
        """
        Update a data exporter config with a diff

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataExporterConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/data-exporter-configs/{jsonable_encoder(data_exporter_config_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DataExporterConfig,
                    parse_obj_as(
                        type_=DataExporterConfig,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
