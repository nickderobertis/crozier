

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.conditions import Conditions
from ..types.http_validation_error import HttpValidationError
from ..types.license_types import LicenseTypes
from ..types.limitations import Limitations
from ..types.permissions import Permissions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChangingTheLicenseOntologyForAdminsOnlyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_license(
        self,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Adds a license to the ontology. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "licenses/add/",
            method="POST",
            json={
                "id": id,
                "name": name,
                "url": url,
                "type": convert_and_respect_annotation_metadata(
                    object_=type, annotation=LicenseTypes, direction="write"
                ),
                "conditions": convert_and_respect_annotation_metadata(
                    object_=conditions, annotation=typing.Sequence[Conditions], direction="write"
                ),
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=typing.Sequence[Permissions], direction="write"
                ),
                "limitations": convert_and_respect_annotation_metadata(
                    object_=limitations, annotation=typing.Sequence[Limitations], direction="write"
                ),
                "compatibility": compatibility,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_license(
        self,
        license_id: str,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Changes the properties of a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"licenses/{encode_path_param(license_id)}",
            method="PUT",
            json={
                "id": id,
                "name": name,
                "url": url,
                "type": convert_and_respect_annotation_metadata(
                    object_=type, annotation=LicenseTypes, direction="write"
                ),
                "conditions": convert_and_respect_annotation_metadata(
                    object_=conditions, annotation=typing.Sequence[Conditions], direction="write"
                ),
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=typing.Sequence[Permissions], direction="write"
                ),
                "limitations": convert_and_respect_annotation_metadata(
                    object_=limitations, annotation=typing.Sequence[Limitations], direction="write"
                ),
                "compatibility": compatibility,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_license(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Deletes a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"licenses/{encode_path_param(license_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawChangingTheLicenseOntologyForAdminsOnlyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_license(
        self,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Adds a license to the ontology. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "licenses/add/",
            method="POST",
            json={
                "id": id,
                "name": name,
                "url": url,
                "type": convert_and_respect_annotation_metadata(
                    object_=type, annotation=LicenseTypes, direction="write"
                ),
                "conditions": convert_and_respect_annotation_metadata(
                    object_=conditions, annotation=typing.Sequence[Conditions], direction="write"
                ),
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=typing.Sequence[Permissions], direction="write"
                ),
                "limitations": convert_and_respect_annotation_metadata(
                    object_=limitations, annotation=typing.Sequence[Limitations], direction="write"
                ),
                "compatibility": compatibility,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_license(
        self,
        license_id: str,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Changes the properties of a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"licenses/{encode_path_param(license_id)}",
            method="PUT",
            json={
                "id": id,
                "name": name,
                "url": url,
                "type": convert_and_respect_annotation_metadata(
                    object_=type, annotation=LicenseTypes, direction="write"
                ),
                "conditions": convert_and_respect_annotation_metadata(
                    object_=conditions, annotation=typing.Sequence[Conditions], direction="write"
                ),
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=typing.Sequence[Permissions], direction="write"
                ),
                "limitations": convert_and_respect_annotation_metadata(
                    object_=limitations, annotation=typing.Sequence[Limitations], direction="write"
                ),
                "compatibility": compatibility,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_license(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Deletes a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"licenses/{encode_path_param(license_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
