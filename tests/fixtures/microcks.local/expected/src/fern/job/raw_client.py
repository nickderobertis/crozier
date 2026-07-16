

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.counter import Counter
from ..types.import_job import ImportJob
from ..types.metadata import Metadata
from ..types.secret_ref import SecretRef
from ..types.service_ref import ServiceRef


OMIT = typing.cast(typing.Any, ...)


class RawJobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_artifact(
        self, *, main_artifact: bool, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Uploads an artifact to be imported by Microcks.

        Parameters
        ----------
        main_artifact : bool
            Flag telling if this should be considered as primary or secondary artifact. Default to 'true'

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Artifact was imported and Service found
        """
        _response = self._client_wrapper.httpx_client.request(
            "artifact/upload",
            method="POST",
            params={
                "mainArtifact": main_artifact,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_import_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ImportJob]]:
        """
        Retrieve a list of ImportJobs

        Parameters
        ----------
        page : typing.Optional[int]
            Page of ImportJobs to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)

        name : typing.Optional[str]
            Name like criterion for query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ImportJob]]
            List of found ImportJobs
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "page": page,
                "size": size,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ImportJob],
                    parse_obj_as(
                        type_=typing.List[ImportJob],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_import_job(
        self,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImportJob]:
        """
        Create a new ImportJob

        Parameters
        ----------
        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportJob]
            Created ImportJob
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="POST",
            json={
                "active": active,
                "createdDate": created_date,
                "etag": etag,
                "frequency": frequency,
                "id": id,
                "lastImportDate": last_import_date,
                "lastImportError": last_import_error,
                "mainArtifact": main_artifact,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "name": name,
                "repositoryDisableSSLValidation": repository_disable_ssl_validation,
                "repositoryUrl": repository_url,
                "secretRef": convert_and_respect_annotation_metadata(
                    object_=secret_ref, annotation=SecretRef, direction="write"
                ),
                "serviceRefs": convert_and_respect_annotation_metadata(
                    object_=service_refs, annotation=typing.Sequence[ServiceRef], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_import_job_counter(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Counter]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Counter]
            Number of ImportJobs in datastore
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Counter,
                    parse_obj_as(
                        type_=Counter,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportJob]:
        """
        Retrieve an ImportJob using its identifier

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportJob]
            Found ImportJob
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_import_job(
        self,
        id_: str,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImportJob]:
        """
        Update an ImportJob

        Parameters
        ----------
        id_ : str
            Unique identifier of ImportJob to manage

        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportJob]
            Updated ImportJob
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id_)}",
            method="POST",
            json={
                "active": active,
                "createdDate": created_date,
                "etag": etag,
                "frequency": frequency,
                "id": id,
                "lastImportDate": last_import_date,
                "lastImportError": last_import_error,
                "mainArtifact": main_artifact,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "name": name,
                "repositoryDisableSSLValidation": repository_disable_ssl_validation,
                "repositoryUrl": repository_url,
                "secretRef": convert_and_respect_annotation_metadata(
                    object_=secret_ref, annotation=SecretRef, direction="write"
                ),
                "serviceRefs": convert_and_respect_annotation_metadata(
                    object_=service_refs, annotation=typing.Sequence[ServiceRef], direction="write"
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
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Delete an ImportJob

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            ImportJob deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def activate_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportJob]:
        """
        Make an ImportJob active, so that it is executed

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportJob]
            ImportJob is activated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}/activate",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def start_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportJob]:
        """
        Starting an ImportJob forces it to immediatly import mock definitions

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportJob]
            Started ImportJob
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}/start",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def stop_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImportJob]:
        """
        Stopping an ImportJob desactivate it, so that it won't execute at next schedule

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportJob]
            Stopped ImportJob
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}/stop",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_artifact(
        self, *, main_artifact: bool, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Uploads an artifact to be imported by Microcks.

        Parameters
        ----------
        main_artifact : bool
            Flag telling if this should be considered as primary or secondary artifact. Default to 'true'

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Artifact was imported and Service found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "artifact/upload",
            method="POST",
            params={
                "mainArtifact": main_artifact,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_import_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ImportJob]]:
        """
        Retrieve a list of ImportJobs

        Parameters
        ----------
        page : typing.Optional[int]
            Page of ImportJobs to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)

        name : typing.Optional[str]
            Name like criterion for query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ImportJob]]
            List of found ImportJobs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "page": page,
                "size": size,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ImportJob],
                    parse_obj_as(
                        type_=typing.List[ImportJob],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_import_job(
        self,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImportJob]:
        """
        Create a new ImportJob

        Parameters
        ----------
        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportJob]
            Created ImportJob
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="POST",
            json={
                "active": active,
                "createdDate": created_date,
                "etag": etag,
                "frequency": frequency,
                "id": id,
                "lastImportDate": last_import_date,
                "lastImportError": last_import_error,
                "mainArtifact": main_artifact,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "name": name,
                "repositoryDisableSSLValidation": repository_disable_ssl_validation,
                "repositoryUrl": repository_url,
                "secretRef": convert_and_respect_annotation_metadata(
                    object_=secret_ref, annotation=SecretRef, direction="write"
                ),
                "serviceRefs": convert_and_respect_annotation_metadata(
                    object_=service_refs, annotation=typing.Sequence[ServiceRef], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_import_job_counter(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Counter]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Counter]
            Number of ImportJobs in datastore
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Counter,
                    parse_obj_as(
                        type_=Counter,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportJob]:
        """
        Retrieve an ImportJob using its identifier

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportJob]
            Found ImportJob
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_import_job(
        self,
        id_: str,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImportJob]:
        """
        Update an ImportJob

        Parameters
        ----------
        id_ : str
            Unique identifier of ImportJob to manage

        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportJob]
            Updated ImportJob
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id_)}",
            method="POST",
            json={
                "active": active,
                "createdDate": created_date,
                "etag": etag,
                "frequency": frequency,
                "id": id,
                "lastImportDate": last_import_date,
                "lastImportError": last_import_error,
                "mainArtifact": main_artifact,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "name": name,
                "repositoryDisableSSLValidation": repository_disable_ssl_validation,
                "repositoryUrl": repository_url,
                "secretRef": convert_and_respect_annotation_metadata(
                    object_=secret_ref, annotation=SecretRef, direction="write"
                ),
                "serviceRefs": convert_and_respect_annotation_metadata(
                    object_=service_refs, annotation=typing.Sequence[ServiceRef], direction="write"
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
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Delete an ImportJob

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            ImportJob deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def activate_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportJob]:
        """
        Make an ImportJob active, so that it is executed

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportJob]
            ImportJob is activated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}/activate",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def start_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportJob]:
        """
        Starting an ImportJob forces it to immediatly import mock definitions

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportJob]
            Started ImportJob
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}/start",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def stop_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImportJob]:
        """
        Stopping an ImportJob desactivate it, so that it won't execute at next schedule

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportJob]
            Stopped ImportJob
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{jsonable_encoder(id)}/stop",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportJob,
                    parse_obj_as(
                        type_=ImportJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
