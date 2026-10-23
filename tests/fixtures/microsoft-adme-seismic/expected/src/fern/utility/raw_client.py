

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.locked_error import LockedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.access_token import AccessToken
from ..types.ls_datasets import LsDatasets
from pydantic import ValidationError


class RawUtilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ls(
        self,
        *,
        sdpath: str,
        wmode: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LsDatasets]:
        """
        <ul>
        <li>Return the list of datasets and sub-directories of a seismic store path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path, sd://tenant/sub-project/path.

        wmode : typing.Optional[str]
            Working mode, directories or datasets or undefined for both.

        limit : typing.Optional[float]
            Limits the total number of datasets to return.

        cursor : typing.Optional[str]
            Pagination token - this query parameter can be omitted on first call.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LsDatasets]
            Seismic store path content.
        """
        _response = self._client_wrapper.httpx_client.request(
            "utility/ls",
            method="GET",
            params={
                "sdpath": sdpath,
                "wmode": wmode,
                "limit": limit,
                "cursor": cursor,
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
                    LsDatasets,
                    parse_obj_as(
                        type_=LsDatasets,
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

    def storage_tiers(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        <ul><li>Return the list of storage tiers</ul>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "utility/storage-tiers",
            method="GET",
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

    def cp(
        self,
        *,
        sdpath_from: str,
        sdpath_to: str,
        lock: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        <ul>
        <li>Copy a seismic store dataset. The source and destination dataset must be in the same sub-project.</li>
        <li>Required roles:
          <ul>
            <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
            <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
          </ul>
        </li>
        </ul>

        Parameters
        ----------
        sdpath_from : str
            Seismic store source dataset path.

        sdpath_to : str
            Seismic store destination dataset path.

        lock : typing.Optional[bool]
            Lock source and destination while copying.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Copy operation succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "utility/cp",
            method="POST",
            params={
                "sdpath_from": sdpath_from,
                "sdpath_to": sdpath_to,
                "lock": lock,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def gcs_access_token(
        self,
        *,
        sdpath: str,
        readonly: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccessToken]:
        """
        <ul>
          <li>Generate a GCS access token for a specified seismic store resource. The source and destination dataset must be in the same sub-project.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/sub-project.

        readonly : typing.Optional[bool]
            Readonly access, true(default) or false.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessToken]
            The GCS access token.
        """
        _response = self._client_wrapper.httpx_client.request(
            "utility/gcs-access-token",
            method="GET",
            params={
                "sdpath": sdpath,
                "readonly": readonly,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
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

    def upload_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccessToken]:
        """
        <ul> <li>Generate the upload connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk upload.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessToken]
            The upload connection credential string.
        """
        _response = self._client_wrapper.httpx_client.request(
            "utility/upload-connection-string",
            method="GET",
            params={
                "sdpath": sdpath,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
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

    def download_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccessToken]:
        """
        <ul> <li>Generate the download connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk download.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessToken]
            The download connection credential string.
        """
        _response = self._client_wrapper.httpx_client.request(
            "utility/download-connection-string",
            method="GET",
            params={
                "sdpath": sdpath,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
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


class AsyncRawUtilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ls(
        self,
        *,
        sdpath: str,
        wmode: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LsDatasets]:
        """
        <ul>
        <li>Return the list of datasets and sub-directories of a seismic store path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path, sd://tenant/sub-project/path.

        wmode : typing.Optional[str]
            Working mode, directories or datasets or undefined for both.

        limit : typing.Optional[float]
            Limits the total number of datasets to return.

        cursor : typing.Optional[str]
            Pagination token - this query parameter can be omitted on first call.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LsDatasets]
            Seismic store path content.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "utility/ls",
            method="GET",
            params={
                "sdpath": sdpath,
                "wmode": wmode,
                "limit": limit,
                "cursor": cursor,
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
                    LsDatasets,
                    parse_obj_as(
                        type_=LsDatasets,
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

    async def storage_tiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        <ul><li>Return the list of storage tiers</ul>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "utility/storage-tiers",
            method="GET",
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

    async def cp(
        self,
        *,
        sdpath_from: str,
        sdpath_to: str,
        lock: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        <ul>
        <li>Copy a seismic store dataset. The source and destination dataset must be in the same sub-project.</li>
        <li>Required roles:
          <ul>
            <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
            <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
          </ul>
        </li>
        </ul>

        Parameters
        ----------
        sdpath_from : str
            Seismic store source dataset path.

        sdpath_to : str
            Seismic store destination dataset path.

        lock : typing.Optional[bool]
            Lock source and destination while copying.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Copy operation succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "utility/cp",
            method="POST",
            params={
                "sdpath_from": sdpath_from,
                "sdpath_to": sdpath_to,
                "lock": lock,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def gcs_access_token(
        self,
        *,
        sdpath: str,
        readonly: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccessToken]:
        """
        <ul>
          <li>Generate a GCS access token for a specified seismic store resource. The source and destination dataset must be in the same sub-project.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/sub-project.

        readonly : typing.Optional[bool]
            Readonly access, true(default) or false.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessToken]
            The GCS access token.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "utility/gcs-access-token",
            method="GET",
            params={
                "sdpath": sdpath,
                "readonly": readonly,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
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

    async def upload_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccessToken]:
        """
        <ul> <li>Generate the upload connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk upload.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessToken]
            The upload connection credential string.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "utility/upload-connection-string",
            method="GET",
            params={
                "sdpath": sdpath,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
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

    async def download_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccessToken]:
        """
        <ul> <li>Generate the download connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk download.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessToken]
            The download connection credential string.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "utility/download-connection-string",
            method="GET",
            params={
                "sdpath": sdpath,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
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
