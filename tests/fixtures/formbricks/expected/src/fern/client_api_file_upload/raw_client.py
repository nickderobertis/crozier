

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.bad_request_error_body import BadRequestErrorBody
from .types.post_client_workspace_id_storage_response import PostClientWorkspaceIdStorageResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClientApiFileUploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_private_file(
        self,
        workspace_id: str,
        *,
        survey_id: str,
        file_name: str,
        file_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostClientWorkspaceIdStorageResponse]:
        """
        API endpoint for uploading private files. Uploaded files are kept private so that only users with access to the specified Workspace can retrieve them. The endpoint validates the survey ID, file name, and file type from the request body, and returns a signed URL for S3 uploads along with a local upload URL. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        survey_id : str
            The ID of the survey associated with the file.

        file_name : str
            The name of the file to be uploaded.

        file_type : str
            The MIME type of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostClientWorkspaceIdStorageResponse]
            OK - Returns the signed URL, presigned fields, updated file name, and file URL.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(workspace_id)}/storage",
            method="POST",
            json={
                "surveyId": survey_id,
                "fileName": file_name,
                "fileType": file_type,
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
                    PostClientWorkspaceIdStorageResponse,
                    parse_obj_as(
                        type_=PostClientWorkspaceIdStorageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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


class AsyncRawClientApiFileUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_private_file(
        self,
        workspace_id: str,
        *,
        survey_id: str,
        file_name: str,
        file_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostClientWorkspaceIdStorageResponse]:
        """
        API endpoint for uploading private files. Uploaded files are kept private so that only users with access to the specified Workspace can retrieve them. The endpoint validates the survey ID, file name, and file type from the request body, and returns a signed URL for S3 uploads along with a local upload URL. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        survey_id : str
            The ID of the survey associated with the file.

        file_name : str
            The name of the file to be uploaded.

        file_type : str
            The MIME type of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostClientWorkspaceIdStorageResponse]
            OK - Returns the signed URL, presigned fields, updated file name, and file URL.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(workspace_id)}/storage",
            method="POST",
            json={
                "surveyId": survey_id,
                "fileName": file_name,
                "fileType": file_type,
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
                    PostClientWorkspaceIdStorageResponse,
                    parse_obj_as(
                        type_=PostClientWorkspaceIdStorageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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
