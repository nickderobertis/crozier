

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.done import Done
from ..types.global_config import GlobalConfig
from ..types.import_export import ImportExport
from ..types.import_export_admins_item import ImportExportAdminsItem
from ..types.import_export_api_keys_item import ImportExportApiKeysItem
from ..types.import_export_error_templates_item import ImportExportErrorTemplatesItem
from ..types.import_export_service_descriptors_item import ImportExportServiceDescriptorsItem
from ..types.import_export_service_groups_item import ImportExportServiceGroupsItem
from ..types.import_export_simple_admins_item import ImportExportSimpleAdminsItem
from ..types.import_export_stats import ImportExportStats
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def full_import_from_file(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Done]:
        """
        Import the full state of Otoroshi as a file

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/import",
            method="POST",
            json={
                "admins": convert_and_respect_annotation_metadata(
                    object_=admins, annotation=typing.Sequence[ImportExportAdminsItem], direction="write"
                ),
                "apiKeys": convert_and_respect_annotation_metadata(
                    object_=api_keys, annotation=typing.Sequence[ImportExportApiKeysItem], direction="write"
                ),
                "appConfig": app_config,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=GlobalConfig, direction="write"
                ),
                "date": date,
                "dateRaw": date_raw,
                "errorTemplates": convert_and_respect_annotation_metadata(
                    object_=error_templates,
                    annotation=typing.Sequence[ImportExportErrorTemplatesItem],
                    direction="write",
                ),
                "label": label,
                "serviceDescriptors": convert_and_respect_annotation_metadata(
                    object_=service_descriptors,
                    annotation=typing.Sequence[ImportExportServiceDescriptorsItem],
                    direction="write",
                ),
                "serviceGroups": convert_and_respect_annotation_metadata(
                    object_=service_groups, annotation=typing.Sequence[ImportExportServiceGroupsItem], direction="write"
                ),
                "simpleAdmins": convert_and_respect_annotation_metadata(
                    object_=simple_admins, annotation=typing.Sequence[ImportExportSimpleAdminsItem], direction="write"
                ),
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=ImportExportStats, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def full_export(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ImportExport]:
        """
        Export the full state of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportExport]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/otoroshi.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportExport,
                    parse_obj_as(
                        type_=ImportExport,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def full_import(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Done]:
        """
        Import the full state of Otoroshi

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/otoroshi.json",
            method="POST",
            json={
                "admins": convert_and_respect_annotation_metadata(
                    object_=admins, annotation=typing.Sequence[ImportExportAdminsItem], direction="write"
                ),
                "apiKeys": convert_and_respect_annotation_metadata(
                    object_=api_keys, annotation=typing.Sequence[ImportExportApiKeysItem], direction="write"
                ),
                "appConfig": app_config,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=GlobalConfig, direction="write"
                ),
                "date": date,
                "dateRaw": date_raw,
                "errorTemplates": convert_and_respect_annotation_metadata(
                    object_=error_templates,
                    annotation=typing.Sequence[ImportExportErrorTemplatesItem],
                    direction="write",
                ),
                "label": label,
                "serviceDescriptors": convert_and_respect_annotation_metadata(
                    object_=service_descriptors,
                    annotation=typing.Sequence[ImportExportServiceDescriptorsItem],
                    direction="write",
                ),
                "serviceGroups": convert_and_respect_annotation_metadata(
                    object_=service_groups, annotation=typing.Sequence[ImportExportServiceGroupsItem], direction="write"
                ),
                "simpleAdmins": convert_and_respect_annotation_metadata(
                    object_=simple_admins, annotation=typing.Sequence[ImportExportSimpleAdminsItem], direction="write"
                ),
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=ImportExportStats, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def full_import_from_file(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Done]:
        """
        Import the full state of Otoroshi as a file

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/import",
            method="POST",
            json={
                "admins": convert_and_respect_annotation_metadata(
                    object_=admins, annotation=typing.Sequence[ImportExportAdminsItem], direction="write"
                ),
                "apiKeys": convert_and_respect_annotation_metadata(
                    object_=api_keys, annotation=typing.Sequence[ImportExportApiKeysItem], direction="write"
                ),
                "appConfig": app_config,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=GlobalConfig, direction="write"
                ),
                "date": date,
                "dateRaw": date_raw,
                "errorTemplates": convert_and_respect_annotation_metadata(
                    object_=error_templates,
                    annotation=typing.Sequence[ImportExportErrorTemplatesItem],
                    direction="write",
                ),
                "label": label,
                "serviceDescriptors": convert_and_respect_annotation_metadata(
                    object_=service_descriptors,
                    annotation=typing.Sequence[ImportExportServiceDescriptorsItem],
                    direction="write",
                ),
                "serviceGroups": convert_and_respect_annotation_metadata(
                    object_=service_groups, annotation=typing.Sequence[ImportExportServiceGroupsItem], direction="write"
                ),
                "simpleAdmins": convert_and_respect_annotation_metadata(
                    object_=simple_admins, annotation=typing.Sequence[ImportExportSimpleAdminsItem], direction="write"
                ),
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=ImportExportStats, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def full_export(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportExport]:
        """
        Export the full state of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportExport]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/otoroshi.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportExport,
                    parse_obj_as(
                        type_=ImportExport,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def full_import(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Done]:
        """
        Import the full state of Otoroshi

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/otoroshi.json",
            method="POST",
            json={
                "admins": convert_and_respect_annotation_metadata(
                    object_=admins, annotation=typing.Sequence[ImportExportAdminsItem], direction="write"
                ),
                "apiKeys": convert_and_respect_annotation_metadata(
                    object_=api_keys, annotation=typing.Sequence[ImportExportApiKeysItem], direction="write"
                ),
                "appConfig": app_config,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=GlobalConfig, direction="write"
                ),
                "date": date,
                "dateRaw": date_raw,
                "errorTemplates": convert_and_respect_annotation_metadata(
                    object_=error_templates,
                    annotation=typing.Sequence[ImportExportErrorTemplatesItem],
                    direction="write",
                ),
                "label": label,
                "serviceDescriptors": convert_and_respect_annotation_metadata(
                    object_=service_descriptors,
                    annotation=typing.Sequence[ImportExportServiceDescriptorsItem],
                    direction="write",
                ),
                "serviceGroups": convert_and_respect_annotation_metadata(
                    object_=service_groups, annotation=typing.Sequence[ImportExportServiceGroupsItem], direction="write"
                ),
                "simpleAdmins": convert_and_respect_annotation_metadata(
                    object_=simple_admins, annotation=typing.Sequence[ImportExportSimpleAdminsItem], direction="write"
                ),
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=ImportExportStats, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
