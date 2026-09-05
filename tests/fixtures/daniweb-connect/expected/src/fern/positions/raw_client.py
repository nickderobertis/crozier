

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.endpoint_delete_positions_id import EndpointDeletePositionsId
from ..types.endpoint_patch_positions_id import EndpointPatchPositionsId
from ..types.endpoint_post_positions import EndpointPostPositions
from .types.patch_positions_id_request_category import PatchPositionsIdRequestCategory
from .types.patch_positions_id_request_organization_size import PatchPositionsIdRequestOrganizationSize
from .types.patch_positions_id_request_position import PatchPositionsIdRequestPosition
from .types.post_positions_request_category import PostPositionsRequestCategory
from .types.post_positions_request_organization_size import PostPositionsRequestOrganizationSize
from .types.post_positions_request_position import PostPositionsRequestPosition
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPositionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_positions(
        self,
        *,
        category: PostPositionsRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PostPositionsRequestOrganizationSize] = OMIT,
        position: typing.Optional[PostPositionsRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostPositions]:
        """
        Update the OAuth'ed end user's Curriculum Vitae by adding a position.

        Parameters
        ----------
        category : PostPositionsRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PostPositionsRequestOrganizationSize]

        position : typing.Optional[PostPositionsRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostPositions]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "positions",
            method="POST",
            data={
                "category": category,
                "end_date": end_date,
                "organization": organization,
                "organization_size": organization_size,
                "position": position,
                "role": role,
                "start_date": start_date,
                "summary": summary,
                "url": url,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostPositions,
                    parse_obj_as(
                        type_=EndpointPostPositions,
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

    def delete_positions_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointDeletePositionsId]:
        """
        Remove an item from the OAuth'ed end user's Curriculum Vitae.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointDeletePositionsId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"positions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointDeletePositionsId,
                    parse_obj_as(
                        type_=EndpointDeletePositionsId,
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

    def patch_positions_id(
        self,
        id: int,
        *,
        category: PatchPositionsIdRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PatchPositionsIdRequestOrganizationSize] = OMIT,
        position: typing.Optional[PatchPositionsIdRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPatchPositionsId]:
        """
        Update the OAuth'ed end user's Curriculum Vitae by modifying an existing position.

        Parameters
        ----------
        id : int

        category : PatchPositionsIdRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PatchPositionsIdRequestOrganizationSize]

        position : typing.Optional[PatchPositionsIdRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPatchPositionsId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"positions/{encode_path_param(id)}",
            method="PATCH",
            data={
                "category": category,
                "end_date": end_date,
                "organization": organization,
                "organization_size": organization_size,
                "position": position,
                "role": role,
                "start_date": start_date,
                "summary": summary,
                "url": url,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPatchPositionsId,
                    parse_obj_as(
                        type_=EndpointPatchPositionsId,
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


class AsyncRawPositionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_positions(
        self,
        *,
        category: PostPositionsRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PostPositionsRequestOrganizationSize] = OMIT,
        position: typing.Optional[PostPositionsRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostPositions]:
        """
        Update the OAuth'ed end user's Curriculum Vitae by adding a position.

        Parameters
        ----------
        category : PostPositionsRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PostPositionsRequestOrganizationSize]

        position : typing.Optional[PostPositionsRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostPositions]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "positions",
            method="POST",
            data={
                "category": category,
                "end_date": end_date,
                "organization": organization,
                "organization_size": organization_size,
                "position": position,
                "role": role,
                "start_date": start_date,
                "summary": summary,
                "url": url,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostPositions,
                    parse_obj_as(
                        type_=EndpointPostPositions,
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

    async def delete_positions_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointDeletePositionsId]:
        """
        Remove an item from the OAuth'ed end user's Curriculum Vitae.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointDeletePositionsId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"positions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointDeletePositionsId,
                    parse_obj_as(
                        type_=EndpointDeletePositionsId,
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

    async def patch_positions_id(
        self,
        id: int,
        *,
        category: PatchPositionsIdRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PatchPositionsIdRequestOrganizationSize] = OMIT,
        position: typing.Optional[PatchPositionsIdRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPatchPositionsId]:
        """
        Update the OAuth'ed end user's Curriculum Vitae by modifying an existing position.

        Parameters
        ----------
        id : int

        category : PatchPositionsIdRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PatchPositionsIdRequestOrganizationSize]

        position : typing.Optional[PatchPositionsIdRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPatchPositionsId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"positions/{encode_path_param(id)}",
            method="PATCH",
            data={
                "category": category,
                "end_date": end_date,
                "organization": organization,
                "organization_size": organization_size,
                "position": position,
                "role": role,
                "start_date": start_date,
                "summary": summary,
                "url": url,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPatchPositionsId,
                    parse_obj_as(
                        type_=EndpointPatchPositionsId,
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
