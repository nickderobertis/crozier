

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.locked_error import LockedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.dataset import Dataset
from ..types.dataset_and_directories import DatasetAndDirectories
from ..types.dataset_permission import DatasetPermission
from ..types.dataset_size import DatasetSize
from ..types.paginated_datasets import PaginatedDatasets
from .types.dataset_patch_acls import DatasetPatchAcls
from .types.dataset_patch_openzgy_v1 import DatasetPatchOpenzgyV1
from .types.dataset_patch_segy_v1 import DatasetPatchSegyV1
from .types.dataset_patch_seismicmeta import DatasetPatchSeismicmeta
from .types.dataset_register_body_acls import DatasetRegisterBodyAcls
from .types.dataset_register_body_openzgy_v1 import DatasetRegisterBodyOpenzgyV1
from .types.dataset_register_body_segy_v1 import DatasetRegisterBodySegyV1
from .types.dataset_register_body_seismicmeta import DatasetRegisterBodySeismicmeta
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDatasetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        seismicmeta: typing.Optional[bool] = None,
        translate_user_info: typing.Optional[bool] = None,
        record_version: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
        """
        <ul> <li>Return the dataset metadata from seismic store.</li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        seismicmeta : typing.Optional[bool]
            Include the seismic storage metadata record if it exists.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        record_version : typing.Optional[str]
            Retrieve a specific version of the seismic storage metadata record

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Metadata of the dataset.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="GET",
            params={
                "path": path,
                "seismicmeta": seismicmeta,
                "translate-user-info": translate_user_info,
                "record-version": record_version,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def register(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        ltag: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        seismicmeta: typing.Optional[DatasetRegisterBodySeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetRegisterBodyOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetRegisterBodySegyV1] = OMIT,
        acls: typing.Optional[DatasetRegisterBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
        """
        <ul><li>Register a new dataset in the seismic store.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        ltag : typing.Optional[str]
            Legal tag of the dataset.

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        seismicmeta : typing.Optional[DatasetRegisterBodySeismicmeta]
            Seismic metadata to be stored as dataecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetRegisterBodyOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetRegisterBodySegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetRegisterBodyAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Registered dataset metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="POST",
            params={
                "path": path,
            },
            json={
                "type": type,
                "gtags": gtags,
                "seismicmeta": convert_and_respect_annotation_metadata(
                    object_=seismicmeta, annotation=DatasetRegisterBodySeismicmeta, direction="write"
                ),
                "openzgy_v1": convert_and_respect_annotation_metadata(
                    object_=openzgy_v1, annotation=DatasetRegisterBodyOpenzgyV1, direction="write"
                ),
                "segy_v1": convert_and_respect_annotation_metadata(
                    object_=segy_v1, annotation=DatasetRegisterBodySegyV1, direction="write"
                ),
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=DatasetRegisterBodyAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
                "ltag": str(ltag) if ltag is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        <ul> <li>Delete a dataset in the seismic store.</li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="DELETE",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def patch(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        close: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        dataset_new_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filemetadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_modified_date: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        ltag: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        seismicmeta: typing.Optional[DatasetPatchSeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetPatchOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetPatchSegyV1] = OMIT,
        acls: typing.Optional[DatasetPatchAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
        """
        <ul>
        <li>Update the dataset meta information in the seismic store or close (unlock) the dataset. If the endpoint is used without the close parameter, at least one body field is required or the endpoint will return an error.</li>
        <li>Required roles:
          <ul>
            <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
            <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
          </ul>
        </li>
        <li>Patchable fields: <ul>
        <li><b>dataset_new_name:</b> new name to use for the dataset (rename).</li>
        <li><b>filemetadata:</b> This is a seismic store specific field and describes how the physical data is stored in the cloud storage system (GCS/AzureContainer etc.). This metadata is mainly used by client libraries to correctly reconstruct the dataset. For example you can store a dataset as truncated in multiple objects of 64MB each, name them from 0 to N and save the filemetadata = “{nObject: N, totalSize: 1024, objsize: 64, sizeUnit: MB}”.</li>
        <li><b>last_modified_date:</b> Mark this field as true to update the dataset last modified date.</li>
        <li><b>gtags:</b> Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then new gtags are appended to this list.</li>
        <li><b>ltag:</b> Update the existing legalTag value.</b></li>
        <li><b>readonly:</b> Update the dataset mode to readonly (true) or to read/write (false).</li></ul></li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        close : typing.Optional[str]
            Non null sbit value of the dataset. Using this value here will close the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        dataset_new_name : typing.Optional[str]
            New name for the dataset.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Generic information about the dataset stored as key value pairs.

        filemetadata : typing.Optional[typing.Dict[str, typing.Any]]
            Number of objects and the size in bytes of the dataset.

        last_modified_date : typing.Optional[str]
            Date when the dataset was last modified.

        gtags : typing.Optional[typing.Sequence[str]]
            Array of tags associated with the dataset. After patching these tags, they can be used to filter the datasets.

        ltag : typing.Optional[str]
            Legal tag associated with the dataset.

        readonly : typing.Optional[bool]
            True if the dataset is read only.

        seismicmeta : typing.Optional[DatasetPatchSeismicmeta]
            Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetPatchOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetPatchSegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetPatchAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Metadata of the patched dataset.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="PATCH",
            params={
                "path": path,
                "close": close,
            },
            json={
                "dataset_new_name": dataset_new_name,
                "metadata": metadata,
                "filemetadata": filemetadata,
                "last_modified_date": last_modified_date,
                "gtags": gtags,
                "ltag": ltag,
                "readonly": readonly,
                "seismicmeta": convert_and_respect_annotation_metadata(
                    object_=seismicmeta, annotation=DatasetPatchSeismicmeta, direction="write"
                ),
                "openzgy_v1": convert_and_respect_annotation_metadata(
                    object_=openzgy_v1, annotation=DatasetPatchOpenzgyV1, direction="write"
                ),
                "segy_v1": convert_and_respect_annotation_metadata(
                    object_=segy_v1, annotation=DatasetPatchSegyV1, direction="write"
                ),
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=DatasetPatchAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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

    def acquire_a_lock_for_a_dataset_id(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        openmode: typing.Optional[str] = None,
        wid: typing.Optional[float] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
        """
        <ul>
          <li>Open a dataset for read or write and lock its state.</li>
          <li>Required roles open lock for write:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
          <li>Required roles open lock for read:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>
        operationId: dataset-lock

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        openmode : typing.Optional[str]
            Type of the lock which can be set to 'read' (default) or 'write'.

        wid : typing.Optional[float]
            Session identifier issued for a previous write lock acquisition operation.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Acquired a lock and the return value is the dataset metadata with session identifier stored in the 'sbit' attribute.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/lock",
            method="PUT",
            params={
                "path": path,
                "openmode": openmode,
                "wid": wid,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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

    def lock_rm(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        <ul>
          <li>Removes the lock for a dataset id.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/unlock",
            method="PUT",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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

    def permission(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DatasetPermission]:
        """
        <ul>
          <li>Retrieve the access permission of a user on a dataset.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetPermission]
            User access permission on the dataset.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/permission",
            method="GET",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetPermission,
                    parse_obj_as(
                        type_=DatasetPermission,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def ctag_check(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        ctag: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
        """
        <ul><li>Check if the provided dataset cTag match the one stored in the metadata catalog.</li><li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        ctag : str
            Ctag to be validated.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Return true if the ctag is valid or false if it is invalid.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/ctagcheck",
            method="GET",
            params={
                "path": path,
                "ctag": ctag,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def add_tag(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        <ul>
          <li>Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then  new gtags are appended to this list.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags array list.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/gtags",
            method="PUT",
            params={
                "path": path,
                "gtag": gtag,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def size(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DatasetSize]:
        """
        <ul>
        <li>Compute and retrieve the size of a dataset and the date of when the size was computed.</li>
        <li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetSize]
            Size of the dataset and the date of when the size was computed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/size",
            method="POST",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetSize,
                    parse_obj_as(
                        type_=DatasetSize,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def read_directory(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DatasetAndDirectories]:
        """
        <ul>
        <li>List datasets and sub-directories for a directory path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant project name.

        subprojectid : str
            The sub-project name.

        path : str
            The hierarchy path.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetAndDirectories]
            The list of datasets and directories in the requested directory path.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/readdsdirfulllist",
            method="GET",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetAndDirectories,
                    parse_obj_as(
                        type_=DatasetAndDirectories,
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

    def list(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedDatasets]:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags associated with dataset metadata.

        limit : typing.Optional[str]
            Limit the number of datasets in the response

        cursor : typing.Optional[str]
            Cursor for pagination on the datasets list

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedDatasets]
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="GET",
            params={
                "gtag": gtag,
                "limit": limit,
                "cursor": cursor,
                "translate-user-info": translate_user_info,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedDatasets,
                    parse_obj_as(
                        type_=PaginatedDatasets,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def list_post(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedDatasets]:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        limit : typing.Optional[float]
            the max limit of datasets in the response

        cursor : typing.Optional[str]
            the cursor value required to retrieve the next page of result

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedDatasets]
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="POST",
            params={
                "translate-user-info": translate_user_info,
            },
            json={
                "type": type,
                "gtags": gtags,
                "limit": limit,
                "cursor": cursor,
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedDatasets,
                    parse_obj_as(
                        type_=PaginatedDatasets,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def exist(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[bool]]:
        """
        <ul>
        <li>Check if the dataset exists.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasets : typing.Sequence[str]
            Array of datasets inside the subproject.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[bool]]
            A list of Boolean values for all the input datasets in the request body. If a value is true, then the corresponding dataset exists and if it is false, then the dataset does not exist.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/exist",
            method="POST",
            json={
                "datasets": datasets,
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[bool],
                    parse_obj_as(
                        type_=typing.List[bool],
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
            if _response.status_code == 403:
                raise ForbiddenError(
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


class AsyncRawDatasetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        seismicmeta: typing.Optional[bool] = None,
        translate_user_info: typing.Optional[bool] = None,
        record_version: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
        """
        <ul> <li>Return the dataset metadata from seismic store.</li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        seismicmeta : typing.Optional[bool]
            Include the seismic storage metadata record if it exists.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        record_version : typing.Optional[str]
            Retrieve a specific version of the seismic storage metadata record

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Metadata of the dataset.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="GET",
            params={
                "path": path,
                "seismicmeta": seismicmeta,
                "translate-user-info": translate_user_info,
                "record-version": record_version,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def register(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        ltag: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        seismicmeta: typing.Optional[DatasetRegisterBodySeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetRegisterBodyOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetRegisterBodySegyV1] = OMIT,
        acls: typing.Optional[DatasetRegisterBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
        """
        <ul><li>Register a new dataset in the seismic store.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        ltag : typing.Optional[str]
            Legal tag of the dataset.

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        seismicmeta : typing.Optional[DatasetRegisterBodySeismicmeta]
            Seismic metadata to be stored as dataecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetRegisterBodyOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetRegisterBodySegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetRegisterBodyAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Registered dataset metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="POST",
            params={
                "path": path,
            },
            json={
                "type": type,
                "gtags": gtags,
                "seismicmeta": convert_and_respect_annotation_metadata(
                    object_=seismicmeta, annotation=DatasetRegisterBodySeismicmeta, direction="write"
                ),
                "openzgy_v1": convert_and_respect_annotation_metadata(
                    object_=openzgy_v1, annotation=DatasetRegisterBodyOpenzgyV1, direction="write"
                ),
                "segy_v1": convert_and_respect_annotation_metadata(
                    object_=segy_v1, annotation=DatasetRegisterBodySegyV1, direction="write"
                ),
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=DatasetRegisterBodyAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
                "ltag": str(ltag) if ltag is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        <ul> <li>Delete a dataset in the seismic store.</li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="DELETE",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def patch(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        close: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        dataset_new_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filemetadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_modified_date: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        ltag: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        seismicmeta: typing.Optional[DatasetPatchSeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetPatchOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetPatchSegyV1] = OMIT,
        acls: typing.Optional[DatasetPatchAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
        """
        <ul>
        <li>Update the dataset meta information in the seismic store or close (unlock) the dataset. If the endpoint is used without the close parameter, at least one body field is required or the endpoint will return an error.</li>
        <li>Required roles:
          <ul>
            <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
            <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
          </ul>
        </li>
        <li>Patchable fields: <ul>
        <li><b>dataset_new_name:</b> new name to use for the dataset (rename).</li>
        <li><b>filemetadata:</b> This is a seismic store specific field and describes how the physical data is stored in the cloud storage system (GCS/AzureContainer etc.). This metadata is mainly used by client libraries to correctly reconstruct the dataset. For example you can store a dataset as truncated in multiple objects of 64MB each, name them from 0 to N and save the filemetadata = “{nObject: N, totalSize: 1024, objsize: 64, sizeUnit: MB}”.</li>
        <li><b>last_modified_date:</b> Mark this field as true to update the dataset last modified date.</li>
        <li><b>gtags:</b> Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then new gtags are appended to this list.</li>
        <li><b>ltag:</b> Update the existing legalTag value.</b></li>
        <li><b>readonly:</b> Update the dataset mode to readonly (true) or to read/write (false).</li></ul></li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        close : typing.Optional[str]
            Non null sbit value of the dataset. Using this value here will close the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        dataset_new_name : typing.Optional[str]
            New name for the dataset.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Generic information about the dataset stored as key value pairs.

        filemetadata : typing.Optional[typing.Dict[str, typing.Any]]
            Number of objects and the size in bytes of the dataset.

        last_modified_date : typing.Optional[str]
            Date when the dataset was last modified.

        gtags : typing.Optional[typing.Sequence[str]]
            Array of tags associated with the dataset. After patching these tags, they can be used to filter the datasets.

        ltag : typing.Optional[str]
            Legal tag associated with the dataset.

        readonly : typing.Optional[bool]
            True if the dataset is read only.

        seismicmeta : typing.Optional[DatasetPatchSeismicmeta]
            Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetPatchOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetPatchSegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetPatchAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Metadata of the patched dataset.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}",
            method="PATCH",
            params={
                "path": path,
                "close": close,
            },
            json={
                "dataset_new_name": dataset_new_name,
                "metadata": metadata,
                "filemetadata": filemetadata,
                "last_modified_date": last_modified_date,
                "gtags": gtags,
                "ltag": ltag,
                "readonly": readonly,
                "seismicmeta": convert_and_respect_annotation_metadata(
                    object_=seismicmeta, annotation=DatasetPatchSeismicmeta, direction="write"
                ),
                "openzgy_v1": convert_and_respect_annotation_metadata(
                    object_=openzgy_v1, annotation=DatasetPatchOpenzgyV1, direction="write"
                ),
                "segy_v1": convert_and_respect_annotation_metadata(
                    object_=segy_v1, annotation=DatasetPatchSegyV1, direction="write"
                ),
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=DatasetPatchAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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

    async def acquire_a_lock_for_a_dataset_id(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        openmode: typing.Optional[str] = None,
        wid: typing.Optional[float] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
        """
        <ul>
          <li>Open a dataset for read or write and lock its state.</li>
          <li>Required roles open lock for write:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
          <li>Required roles open lock for read:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>
        operationId: dataset-lock

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        openmode : typing.Optional[str]
            Type of the lock which can be set to 'read' (default) or 'write'.

        wid : typing.Optional[float]
            Session identifier issued for a previous write lock acquisition operation.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Acquired a lock and the return value is the dataset metadata with session identifier stored in the 'sbit' attribute.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/lock",
            method="PUT",
            params={
                "path": path,
                "openmode": openmode,
                "wid": wid,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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

    async def lock_rm(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        <ul>
          <li>Removes the lock for a dataset id.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/unlock",
            method="PUT",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 423:
                raise LockedError(
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

    async def permission(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DatasetPermission]:
        """
        <ul>
          <li>Retrieve the access permission of a user on a dataset.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetPermission]
            User access permission on the dataset.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/permission",
            method="GET",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetPermission,
                    parse_obj_as(
                        type_=DatasetPermission,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def ctag_check(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        ctag: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
        """
        <ul><li>Check if the provided dataset cTag match the one stored in the metadata catalog.</li><li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        ctag : str
            Ctag to be validated.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Return true if the ctag is valid or false if it is invalid.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/ctagcheck",
            method="GET",
            params={
                "path": path,
                "ctag": ctag,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def add_tag(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        <ul>
          <li>Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then  new gtags are appended to this list.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags array list.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/gtags",
            method="PUT",
            params={
                "path": path,
                "gtag": gtag,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def size(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DatasetSize]:
        """
        <ul>
        <li>Compute and retrieve the size of a dataset and the date of when the size was computed.</li>
        <li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetSize]
            Size of the dataset and the date of when the size was computed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/dataset/{encode_path_param(datasetid)}/size",
            method="POST",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetSize,
                    parse_obj_as(
                        type_=DatasetSize,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def read_directory(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DatasetAndDirectories]:
        """
        <ul>
        <li>List datasets and sub-directories for a directory path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant project name.

        subprojectid : str
            The sub-project name.

        path : str
            The hierarchy path.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetAndDirectories]
            The list of datasets and directories in the requested directory path.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/readdsdirfulllist",
            method="GET",
            params={
                "path": path,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetAndDirectories,
                    parse_obj_as(
                        type_=DatasetAndDirectories,
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

    async def list(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedDatasets]:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags associated with dataset metadata.

        limit : typing.Optional[str]
            Limit the number of datasets in the response

        cursor : typing.Optional[str]
            Cursor for pagination on the datasets list

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedDatasets]
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="GET",
            params={
                "gtag": gtag,
                "limit": limit,
                "cursor": cursor,
                "translate-user-info": translate_user_info,
            },
            headers={
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedDatasets,
                    parse_obj_as(
                        type_=PaginatedDatasets,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def list_post(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedDatasets]:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        limit : typing.Optional[float]
            the max limit of datasets in the response

        cursor : typing.Optional[str]
            the cursor value required to retrieve the next page of result

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedDatasets]
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="POST",
            params={
                "translate-user-info": translate_user_info,
            },
            json={
                "type": type,
                "gtags": gtags,
                "limit": limit,
                "cursor": cursor,
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedDatasets,
                    parse_obj_as(
                        type_=PaginatedDatasets,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def exist(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[bool]]:
        """
        <ul>
        <li>Check if the dataset exists.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasets : typing.Sequence[str]
            Array of datasets inside the subproject.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[bool]]
            A list of Boolean values for all the input datasets in the request body. If a value is true, then the corresponding dataset exists and if it is false, then the dataset does not exist.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/exist",
            method="POST",
            json={
                "datasets": datasets,
            },
            headers={
                "content-type": "application/json",
                "impersonation-token-context": str(impersonation_token_context)
                if impersonation_token_context is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[bool],
                    parse_obj_as(
                        type_=typing.List[bool],
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
