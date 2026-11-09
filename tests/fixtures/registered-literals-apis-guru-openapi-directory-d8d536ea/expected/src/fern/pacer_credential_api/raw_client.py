

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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.exception import Exception
from ..types.pacer_credential import PacerCredential
from ..types.pacer_credential_list_response import PacerCredentialListResponse
from ..types.success import Success
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPacerCredentialApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_pacer_credential(
        self, *, page_number: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PacerCredentialListResponse]:
        """
        List registered PACER credentials.

        Parameters
        ----------
        page_number : typing.Optional[int]
            The page number of the PACER credentials to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PacerCredentialListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCredential",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PacerCredentialListResponse,
                    parse_obj_as(
                        type_=PacerCredentialListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def add_pacer_credential(
        self,
        *,
        pacer_user_id: str,
        password: str,
        default_pacer_client_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Success]:
        """
        Register PACER credentials with UniCourt.

        Parameters
        ----------
        pacer_user_id : str
            Pacer User Id.

        password : str
            Password.

        default_pacer_client_code : typing.Optional[str]
            Pacer Client Code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Success]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCredential",
            method="PUT",
            json={
                "defaultPacerClientCode": default_pacer_client_code,
                "pacerUserId": pacer_user_id,
                "password": password,
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
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def get_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PacerCredential]:
        """
        Retrieve the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PacerCredential]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pacerCredential/{encode_path_param(pacer_user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PacerCredential,
                    parse_obj_as(
                        type_=PacerCredential,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def remove_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Success]:
        """
        De-register the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Success]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pacerCredential/{encode_path_param(pacer_user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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


class AsyncRawPacerCredentialApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_pacer_credential(
        self, *, page_number: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PacerCredentialListResponse]:
        """
        List registered PACER credentials.

        Parameters
        ----------
        page_number : typing.Optional[int]
            The page number of the PACER credentials to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PacerCredentialListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCredential",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PacerCredentialListResponse,
                    parse_obj_as(
                        type_=PacerCredentialListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def add_pacer_credential(
        self,
        *,
        pacer_user_id: str,
        password: str,
        default_pacer_client_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Success]:
        """
        Register PACER credentials with UniCourt.

        Parameters
        ----------
        pacer_user_id : str
            Pacer User Id.

        password : str
            Password.

        default_pacer_client_code : typing.Optional[str]
            Pacer Client Code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Success]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCredential",
            method="PUT",
            json={
                "defaultPacerClientCode": default_pacer_client_code,
                "pacerUserId": pacer_user_id,
                "password": password,
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
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def get_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PacerCredential]:
        """
        Retrieve the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PacerCredential]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pacerCredential/{encode_path_param(pacer_user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PacerCredential,
                    parse_obj_as(
                        type_=PacerCredential,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def remove_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Success]:
        """
        De-register the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Success]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pacerCredential/{encode_path_param(pacer_user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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
