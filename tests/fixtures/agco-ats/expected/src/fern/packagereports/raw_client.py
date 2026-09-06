

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.update_system_models_category import UpdateSystemModelsCategory
from ..types.update_system_models_package_report import UpdateSystemModelsPackageReport
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPackagereportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def default(
        self,
        client_id: str,
        *,
        categories: typing.Optional[typing.Sequence[UpdateSystemModelsCategory]] = OMIT,
        package_description: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        categories : typing.Optional[typing.Sequence[UpdateSystemModelsCategory]]
            The package report's categories.

        package_description : typing.Optional[str]
            Read Only. The package description

        package_id : typing.Optional[str]
            The PackageID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(client_id)}/PackageReports",
            method="PUT",
            json={
                "Categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[UpdateSystemModelsCategory], direction="write"
                ),
                "PackageDescription": package_description,
                "PackageID": package_id,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def batch(
        self,
        client_id: str,
        *,
        request: typing.Sequence[UpdateSystemModelsPackageReport],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request : typing.Sequence[UpdateSystemModelsPackageReport]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(client_id)}/PackageReports/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[UpdateSystemModelsPackageReport], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPackagereportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def default(
        self,
        client_id: str,
        *,
        categories: typing.Optional[typing.Sequence[UpdateSystemModelsCategory]] = OMIT,
        package_description: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        categories : typing.Optional[typing.Sequence[UpdateSystemModelsCategory]]
            The package report's categories.

        package_description : typing.Optional[str]
            Read Only. The package description

        package_id : typing.Optional[str]
            The PackageID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(client_id)}/PackageReports",
            method="PUT",
            json={
                "Categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[UpdateSystemModelsCategory], direction="write"
                ),
                "PackageDescription": package_description,
                "PackageID": package_id,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def batch(
        self,
        client_id: str,
        *,
        request: typing.Sequence[UpdateSystemModelsPackageReport],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request : typing.Sequence[UpdateSystemModelsPackageReport]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(client_id)}/PackageReports/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[UpdateSystemModelsPackageReport], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
