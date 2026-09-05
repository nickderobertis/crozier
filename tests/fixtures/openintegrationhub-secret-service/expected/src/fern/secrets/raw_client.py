

import datetime as dt
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.mutable_secret_type import MutableSecretType
from ..types.mutable_secret_value import MutableSecretValue
from ..types.owner import Owner
from .types.create_secret_response import CreateSecretResponse
from .types.get_secret_by_id_response import GetSecretByIdResponse
from .types.get_secrets_response import GetSecretsResponse
from .types.update_secret_response import UpdateSecretResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSecretsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_secrets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSecretsResponse]:
        """
        Retrieve all secrets belonging to the current user.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of results to return per page

        page_number : typing.Optional[int]
            The page number to return (not zero indexed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSecretsResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/secrets/",
            method="GET",
            params={
                "page[size]": page_size,
                "page[number]": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSecretsResponse,
                    parse_obj_as(
                        type_=GetSecretsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_secret(
        self,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSecretResponse]:
        """
        Create a secret

        Parameters
        ----------
        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSecretResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/secrets/",
            method="POST",
            json={
                "name": name,
                "type": type,
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=MutableSecretValue, direction="write"
                ),
                "owners": convert_and_respect_annotation_metadata(
                    object_=owners, annotation=typing.Sequence[Owner], direction="write"
                ),
                "tenant": tenant,
                "domain": domain,
                "lockedAt": locked_at,
                "encryptedFields": encrypted_fields,
                "mixedProperties": mixed_properties,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSecretResponse,
                    parse_obj_as(
                        type_=CreateSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_secret_by_id(
        self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSecretByIdResponse]:
        """
        Returns a secret with given ID

        Parameters
        ----------
        secret_id : str
            ID of secret to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSecretByIdResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/secrets/{encode_path_param(secret_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSecretByIdResponse,
                    parse_obj_as(
                        type_=GetSecretByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def delete_secret(
        self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/secrets/{encode_path_param(secret_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def update_secret(
        self,
        secret_id: str,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSecretResponse]:
        """
        Update a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to update

        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSecretResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/secrets/{encode_path_param(secret_id)}",
            method="PATCH",
            json={
                "name": name,
                "type": type,
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=MutableSecretValue, direction="write"
                ),
                "owners": convert_and_respect_annotation_metadata(
                    object_=owners, annotation=typing.Sequence[Owner], direction="write"
                ),
                "tenant": tenant,
                "domain": domain,
                "lockedAt": locked_at,
                "encryptedFields": encrypted_fields,
                "mixedProperties": mixed_properties,
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
                    UpdateSecretResponse,
                    parse_obj_as(
                        type_=UpdateSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawSecretsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_secrets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSecretsResponse]:
        """
        Retrieve all secrets belonging to the current user.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of results to return per page

        page_number : typing.Optional[int]
            The page number to return (not zero indexed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSecretsResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/secrets/",
            method="GET",
            params={
                "page[size]": page_size,
                "page[number]": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSecretsResponse,
                    parse_obj_as(
                        type_=GetSecretsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_secret(
        self,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSecretResponse]:
        """
        Create a secret

        Parameters
        ----------
        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSecretResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/secrets/",
            method="POST",
            json={
                "name": name,
                "type": type,
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=MutableSecretValue, direction="write"
                ),
                "owners": convert_and_respect_annotation_metadata(
                    object_=owners, annotation=typing.Sequence[Owner], direction="write"
                ),
                "tenant": tenant,
                "domain": domain,
                "lockedAt": locked_at,
                "encryptedFields": encrypted_fields,
                "mixedProperties": mixed_properties,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSecretResponse,
                    parse_obj_as(
                        type_=CreateSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_secret_by_id(
        self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSecretByIdResponse]:
        """
        Returns a secret with given ID

        Parameters
        ----------
        secret_id : str
            ID of secret to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSecretByIdResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/secrets/{encode_path_param(secret_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSecretByIdResponse,
                    parse_obj_as(
                        type_=GetSecretByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def delete_secret(
        self, secret_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/secrets/{encode_path_param(secret_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def update_secret(
        self,
        secret_id: str,
        *,
        name: str,
        type: MutableSecretType,
        owners: typing.Sequence[Owner],
        value: typing.Optional[MutableSecretValue] = OMIT,
        tenant: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        locked_at: typing.Optional[dt.datetime] = OMIT,
        encrypted_fields: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        mixed_properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSecretResponse]:
        """
        Update a secret

        Parameters
        ----------
        secret_id : str
            ID of secret to update

        name : str
            Human readable secret name

        type : MutableSecretType

        owners : typing.Sequence[Owner]

        value : typing.Optional[MutableSecretValue]

        tenant : typing.Optional[str]

        domain : typing.Optional[str]

        locked_at : typing.Optional[dt.datetime]
            Datetime (UTC) when the secret was locked. Relevant for 3legged-oauth-2 during acesstoken updates.

        encrypted_fields : typing.Optional[typing.Sequence[typing.Any]]

        mixed_properties : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSecretResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/secrets/{encode_path_param(secret_id)}",
            method="PATCH",
            json={
                "name": name,
                "type": type,
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=MutableSecretValue, direction="write"
                ),
                "owners": convert_and_respect_annotation_metadata(
                    object_=owners, annotation=typing.Sequence[Owner], direction="write"
                ),
                "tenant": tenant,
                "domain": domain,
                "lockedAt": locked_at,
                "encryptedFields": encrypted_fields,
                "mixedProperties": mixed_properties,
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
                    UpdateSecretResponse,
                    parse_obj_as(
                        type_=UpdateSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
