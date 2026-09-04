

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
from ..errors.unauthorized_error import UnauthorizedError
from .types.patch_client_client_id_request_request import PatchClientClientIdRequestRequest
from .types.patch_client_client_id_response import PatchClientClientIdResponse
from .types.post_client_mgmt_client_request_request import PostClientMgmtClientRequestRequest
from .types.post_client_mgmt_client_response import PostClientMgmtClientResponse
from .types.post_client_request_request import PostClientRequestRequest
from .types.post_client_response import PostClientResponse
from .types.post_oauth_client_request_request import PostOauthClientRequestRequest
from .types.post_oauth_client_response import PostOauthClientResponse
from .types.put_client_client_id_request_request import PutClientClientIdRequestRequest
from .types.put_client_client_id_response import PutClientClientIdResponse
from .types.put_oauth_client_client_id_request_request import PutOauthClientClientIdRequestRequest
from .types.put_oauth_client_client_id_response import PutOauthClientClientIdResponse
from .types.put_oidc_client_client_id_request_request import PutOidcClientClientIdRequestRequest
from .types.put_oidc_client_client_id_response import PutOidcClientClientIdResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostClientResponse]:
        """
        API to add new open ID connect (OIDC) clients, it can be invoked by other modules which manages the relying parties / partners.

        Each relying party can associate to one or multiple OIDC client ids.

        On create, OIDC client status will be by default set to "**active**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostClientResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "client-mgmt/oidc-client",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostClientRequestRequest, direction="write"
                ),
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
                    PostClientResponse,
                    parse_obj_as(
                        type_=PostClientResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_oauth_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostOauthClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostOauthClientResponse]:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostOauthClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostOauthClientResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "client-mgmt/oauth-client",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostOauthClientRequestRequest, direction="write"
                ),
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
                    PostOauthClientResponse,
                    parse_obj_as(
                        type_=PostOauthClientResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_client_mgmt_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientMgmtClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostClientMgmtClientResponse]:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientMgmtClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostClientMgmtClientResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "client-mgmt/client",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostClientMgmtClientRequestRequest, direction="write"
                ),
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
                    PostClientMgmtClientResponse,
                    parse_obj_as(
                        type_=PostClientMgmtClientResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_oidc_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOidcClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutOidcClientClientIdResponse]:
        """
        API to update existing Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOidcClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutOidcClientClientIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client-mgmt/oidc-client/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PutOidcClientClientIdRequestRequest, direction="write"
                ),
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
                    PutOidcClientClientIdResponse,
                    parse_obj_as(
                        type_=PutOidcClientClientIdResponse,
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

    def put_oauth_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOauthClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutOauthClientClientIdResponse]:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOauthClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutOauthClientClientIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client-mgmt/oauth-client/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PutOauthClientClientIdRequestRequest, direction="write"
                ),
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
                    PutOauthClientClientIdResponse,
                    parse_obj_as(
                        type_=PutOauthClientClientIdResponse,
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

    def put_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutClientClientIdResponse]:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutClientClientIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client-mgmt/client/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PutClientClientIdRequestRequest, direction="write"
                ),
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
                    PutClientClientIdResponse,
                    parse_obj_as(
                        type_=PutClientClientIdResponse,
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

    def patch_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PatchClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PatchClientClientIdResponse]:
        """
        API to partially update existing OAuth/Open ID Connect (OIDC) client. Only provided fields will be updated.

        **Special handling for encPublicKey:**
        - When set/updated: validates format and computes enc_public_key_hash
        - When explicitly set to null: clears both enc_public_key and enc_public_key_hash
        - When not present in request: leaves both fields unchanged

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PatchClientClientIdRequestRequest
            All fields are optional. Only provided fields will be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PatchClientClientIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client-mgmt/client/{encode_path_param(client_id)}",
            method="PATCH",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PatchClientClientIdRequestRequest, direction="write"
                ),
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
                    PatchClientClientIdResponse,
                    parse_obj_as(
                        type_=PatchClientClientIdResponse,
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


class AsyncRawManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostClientResponse]:
        """
        API to add new open ID connect (OIDC) clients, it can be invoked by other modules which manages the relying parties / partners.

        Each relying party can associate to one or multiple OIDC client ids.

        On create, OIDC client status will be by default set to "**active**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostClientResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "client-mgmt/oidc-client",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostClientRequestRequest, direction="write"
                ),
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
                    PostClientResponse,
                    parse_obj_as(
                        type_=PostClientResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_oauth_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostOauthClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostOauthClientResponse]:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostOauthClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostOauthClientResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "client-mgmt/oauth-client",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostOauthClientRequestRequest, direction="write"
                ),
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
                    PostOauthClientResponse,
                    parse_obj_as(
                        type_=PostOauthClientResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_client_mgmt_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientMgmtClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostClientMgmtClientResponse]:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientMgmtClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostClientMgmtClientResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "client-mgmt/client",
            method="POST",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostClientMgmtClientRequestRequest, direction="write"
                ),
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
                    PostClientMgmtClientResponse,
                    parse_obj_as(
                        type_=PostClientMgmtClientResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_oidc_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOidcClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutOidcClientClientIdResponse]:
        """
        API to update existing Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOidcClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutOidcClientClientIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client-mgmt/oidc-client/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PutOidcClientClientIdRequestRequest, direction="write"
                ),
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
                    PutOidcClientClientIdResponse,
                    parse_obj_as(
                        type_=PutOidcClientClientIdResponse,
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

    async def put_oauth_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOauthClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutOauthClientClientIdResponse]:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOauthClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutOauthClientClientIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client-mgmt/oauth-client/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PutOauthClientClientIdRequestRequest, direction="write"
                ),
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
                    PutOauthClientClientIdResponse,
                    parse_obj_as(
                        type_=PutOauthClientClientIdResponse,
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

    async def put_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutClientClientIdResponse]:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutClientClientIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client-mgmt/client/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PutClientClientIdRequestRequest, direction="write"
                ),
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
                    PutClientClientIdResponse,
                    parse_obj_as(
                        type_=PutClientClientIdResponse,
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

    async def patch_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PatchClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PatchClientClientIdResponse]:
        """
        API to partially update existing OAuth/Open ID Connect (OIDC) client. Only provided fields will be updated.

        **Special handling for encPublicKey:**
        - When set/updated: validates format and computes enc_public_key_hash
        - When explicitly set to null: clears both enc_public_key and enc_public_key_hash
        - When not present in request: leaves both fields unchanged

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PatchClientClientIdRequestRequest
            All fields are optional. Only provided fields will be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PatchClientClientIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client-mgmt/client/{encode_path_param(client_id)}",
            method="PATCH",
            json={
                "requestTime": request_time,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PatchClientClientIdRequestRequest, direction="write"
                ),
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
                    PatchClientClientIdResponse,
                    parse_obj_as(
                        type_=PatchClientClientIdResponse,
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
