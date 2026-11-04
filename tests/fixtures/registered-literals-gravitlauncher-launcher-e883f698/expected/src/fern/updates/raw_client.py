

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.build_secrets import BuildSecrets
from ..types.launcher_update_info import LauncherUpdateInfo
from ..types.updates_prepare_response import UpdatesPrepareResponse
from .types.post_updates_check_variant_request_variant import PostUpdatesCheckVariantRequestVariant
from .types.post_updates_upload_variant_request_variant import PostUpdatesUploadVariantRequestVariant
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUpdatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdatesPrepareResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdatesPrepareResponse]
            Challenge data.
        """
        _response = self._client_wrapper.httpx_client.request(
            "updates/prepare",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdatesPrepareResponse,
                    parse_obj_as(
                        type_=UpdatesPrepareResponse,
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

    def submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
        self,
        variant: PostUpdatesCheckVariantRequestVariant,
        *,
        signed_data: str,
        public_key: str,
        jwt_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LauncherUpdateInfo]:
        """
        Parameters
        ----------
        variant : PostUpdatesCheckVariantRequestVariant
            Update variant — identifies the target platform/binary.

        signed_data : str
            Base64-encoded ECDSA signature over the challenge data.

        public_key : str
            Base64-encoded DER-encoded ECDSA public key.

        jwt_token : str
            Token received from /updates/prepare.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LauncherUpdateInfo]
            Update info for the launcher itself.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"updates/check/{encode_path_param(variant)}",
            method="POST",
            json={
                "signedData": signed_data,
                "publicKey": public_key,
                "jwtToken": jwt_token,
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
                    LauncherUpdateInfo,
                    parse_obj_as(
                        type_=LauncherUpdateInfo,
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

    def upload_a_game_asset_update_file_admin_server_side_use(
        self,
        variant: PostUpdatesUploadVariantRequestVariant,
        *,
        secrets: BuildSecrets,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        variant : PostUpdatesUploadVariantRequestVariant
            Update variant — identifies the target platform/binary.

        secrets : BuildSecrets
            JSON-serialised BuildSecrets object (privateKey, publicKey).

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"updates/upload/{encode_path_param(variant)}",
            method="POST",
            data={},
            files={
                "secrets": (None, json.dumps(jsonable_encoder(secrets)), "application/json"),
                "file": core.with_content_type(file=file, default_content_type="image/png"),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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


class AsyncRawUpdatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdatesPrepareResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdatesPrepareResponse]
            Challenge data.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "updates/prepare",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdatesPrepareResponse,
                    parse_obj_as(
                        type_=UpdatesPrepareResponse,
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

    async def submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
        self,
        variant: PostUpdatesCheckVariantRequestVariant,
        *,
        signed_data: str,
        public_key: str,
        jwt_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LauncherUpdateInfo]:
        """
        Parameters
        ----------
        variant : PostUpdatesCheckVariantRequestVariant
            Update variant — identifies the target platform/binary.

        signed_data : str
            Base64-encoded ECDSA signature over the challenge data.

        public_key : str
            Base64-encoded DER-encoded ECDSA public key.

        jwt_token : str
            Token received from /updates/prepare.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LauncherUpdateInfo]
            Update info for the launcher itself.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"updates/check/{encode_path_param(variant)}",
            method="POST",
            json={
                "signedData": signed_data,
                "publicKey": public_key,
                "jwtToken": jwt_token,
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
                    LauncherUpdateInfo,
                    parse_obj_as(
                        type_=LauncherUpdateInfo,
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

    async def upload_a_game_asset_update_file_admin_server_side_use(
        self,
        variant: PostUpdatesUploadVariantRequestVariant,
        *,
        secrets: BuildSecrets,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        variant : PostUpdatesUploadVariantRequestVariant
            Update variant — identifies the target platform/binary.

        secrets : BuildSecrets
            JSON-serialised BuildSecrets object (privateKey, publicKey).

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"updates/upload/{encode_path_param(variant)}",
            method="POST",
            data={},
            files={
                "secrets": (None, json.dumps(jsonable_encoder(secrets)), "application/json"),
                "file": core.with_content_type(file=file, default_content_type="image/png"),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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
