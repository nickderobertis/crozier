

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


class RawOsamServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_and_delete_obs_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role.
        It triggers the synchronization of the creation and deletion of S3 Object Storage (OBS) accounts for all RS users,
        associated to their Keycloak account.

        How it works:

        1. When a new Keycloak user account is created, an associated OBS access account **with no rights** is created
        and linked to it.

        2. When a Keycloak user account is deleted, the associated OBS access account is also deleted.

        NOTE: to synchronize OBS user rights from Keycloak you then need to call the endpoint
        * /storage/account/{user}/update*.

        ### Returns:
        JSONResponse — Always a success message saying that the synchronization algorithm of the accounts started.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "storage/accounts/update",
            method="POST",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_obs_user_rights(
        self, user: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role. It updates the S3 Object Storage (OBS)
        rights of any user, calculated from their associated Keycloak account.

        When called, this endpoint will:

        1. Read the user's roles from their Keycloak account.

        2. Calculate the associated OBS access policy rights: they describe the buckets, paths, and permission levels
        (such as read, write and download) that the user has access to.

        3. Apply the access policy to the user's OBS account.

        The operation ensures that the user's OBS permissions match their Keycloak permissions.

        ### Args
        user (str) — The Keycloak username for which the access policy should be applied.

        ### Returns
        JSONResponse — A JSON response confirming that the access policy has been applied.

        ### Raises
        404 — If the user does not exist in Keycloak.<br>
        400 — If the policy could not be applied by the Object Storage provider.

        Parameters
        ----------
        user : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/account/{encode_path_param(user)}/update",
            method="POST",
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

    def get_your_s3credentials(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        This endpoint is called by any anthenticated user.
        It returns your personnal S3 credentials, so you can connect to the bucket where your products have been generated.

        ### Returns
        dict — A dictionary containing 'access_key', 'secret_key', 'endpoint', 'region' for the user's S3 storage.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "storage/account/credentials",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawOsamServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_and_delete_obs_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role.
        It triggers the synchronization of the creation and deletion of S3 Object Storage (OBS) accounts for all RS users,
        associated to their Keycloak account.

        How it works:

        1. When a new Keycloak user account is created, an associated OBS access account **with no rights** is created
        and linked to it.

        2. When a Keycloak user account is deleted, the associated OBS access account is also deleted.

        NOTE: to synchronize OBS user rights from Keycloak you then need to call the endpoint
        * /storage/account/{user}/update*.

        ### Returns:
        JSONResponse — Always a success message saying that the synchronization algorithm of the accounts started.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "storage/accounts/update",
            method="POST",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_obs_user_rights(
        self, user: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role. It updates the S3 Object Storage (OBS)
        rights of any user, calculated from their associated Keycloak account.

        When called, this endpoint will:

        1. Read the user's roles from their Keycloak account.

        2. Calculate the associated OBS access policy rights: they describe the buckets, paths, and permission levels
        (such as read, write and download) that the user has access to.

        3. Apply the access policy to the user's OBS account.

        The operation ensures that the user's OBS permissions match their Keycloak permissions.

        ### Args
        user (str) — The Keycloak username for which the access policy should be applied.

        ### Returns
        JSONResponse — A JSON response confirming that the access policy has been applied.

        ### Raises
        404 — If the user does not exist in Keycloak.<br>
        400 — If the policy could not be applied by the Object Storage provider.

        Parameters
        ----------
        user : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/account/{encode_path_param(user)}/update",
            method="POST",
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

    async def get_your_s3credentials(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        This endpoint is called by any anthenticated user.
        It returns your personnal S3 credentials, so you can connect to the bucket where your products have been generated.

        ### Returns
        dict — A dictionary containing 'access_key', 'secret_key', 'endpoint', 'region' for the user's S3 storage.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "storage/account/credentials",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
