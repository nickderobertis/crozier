

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDatasetDeprecatedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def dataset_sizes(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[float]]:
        """
        <ul>
        <li>Return a list with the sizes of the requested datasets.</li>
        <li>The correctness is not guarantee since this API returns sizes stored by the user in the dataset manifest.</li>
        <li>This API is deprecated, please using /size endpoint to compute and retrieve the size information</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant

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
        HttpResponse[typing.List[float]]
            The list of sizes of all the datasets. If the dataset does not exist, the size returns -1.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/sizes",
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
                    typing.List[float],
                    parse_obj_as(
                        type_=typing.List[float],
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


class AsyncRawDatasetDeprecatedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def dataset_sizes(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[float]]:
        """
        <ul>
        <li>Return a list with the sizes of the requested datasets.</li>
        <li>The correctness is not guarantee since this API returns sizes stored by the user in the dataset manifest.</li>
        <li>This API is deprecated, please using /size endpoint to compute and retrieve the size information</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant

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
        AsyncHttpResponse[typing.List[float]]
            The list of sizes of all the datasets. If the dataset does not exist, the size returns -1.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dataset/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}/sizes",
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
                    typing.List[float],
                    parse_obj_as(
                        type_=typing.List[float],
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
