

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.wizard_config_policy import WizardConfigPolicy
from ..types.wizard_config_schemas_item import WizardConfigSchemasItem
from ..types.wizard_config_trust_chain_item import WizardConfigTrustChainItem
from .types.post_wizard_policy_id_config_response import PostWizardPolicyIdConfigResponse
from .types.post_wizard_policy_response import PostWizardPolicyResponse
from .types.wizard_api_set_policy_async_request_wizard_config import WizardApiSetPolicyAsyncRequestWizardConfig
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWizardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def creates_a_new_policy(
        self,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWizardPolicyResponse]:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostWizardPolicyResponse]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "wizard/policy",
            method="POST",
            json={
                "roles": roles,
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy, annotation=WizardConfigPolicy, direction="write"
                ),
                "schemas": convert_and_respect_annotation_metadata(
                    object_=schemas, annotation=typing.Sequence[WizardConfigSchemasItem], direction="write"
                ),
                "trustChain": convert_and_respect_annotation_metadata(
                    object_=trust_chain, annotation=typing.Sequence[WizardConfigTrustChainItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostWizardPolicyResponse,
                    parse_obj_as(
                        type_=PostWizardPolicyResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def wizard_api_set_policy_async(
        self,
        *,
        save_state: typing.Optional[bool] = OMIT,
        wizard_config: typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        save_state : typing.Optional[bool]

        wizard_config : typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "wizard/push/policy",
            method="POST",
            json={
                "saveState": save_state,
                "wizardConfig": convert_and_respect_annotation_metadata(
                    object_=wizard_config, annotation=WizardApiSetPolicyAsyncRequestWizardConfig, direction="write"
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
                    bool,
                    parse_obj_as(
                        type_=bool,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_policy_config(
        self,
        policy_id: str,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWizardPolicyIdConfigResponse]:
        """
        Get policy config by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier.

        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostWizardPolicyIdConfigResponse]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wizard/{encode_path_param(policy_id)}/config",
            method="POST",
            json={
                "roles": roles,
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy, annotation=WizardConfigPolicy, direction="write"
                ),
                "schemas": convert_and_respect_annotation_metadata(
                    object_=schemas, annotation=typing.Sequence[WizardConfigSchemasItem], direction="write"
                ),
                "trustChain": convert_and_respect_annotation_metadata(
                    object_=trust_chain, annotation=typing.Sequence[WizardConfigTrustChainItem], direction="write"
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
                    PostWizardPolicyIdConfigResponse,
                    parse_obj_as(
                        type_=PostWizardPolicyIdConfigResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawWizardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def creates_a_new_policy(
        self,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostWizardPolicyResponse]:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostWizardPolicyResponse]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wizard/policy",
            method="POST",
            json={
                "roles": roles,
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy, annotation=WizardConfigPolicy, direction="write"
                ),
                "schemas": convert_and_respect_annotation_metadata(
                    object_=schemas, annotation=typing.Sequence[WizardConfigSchemasItem], direction="write"
                ),
                "trustChain": convert_and_respect_annotation_metadata(
                    object_=trust_chain, annotation=typing.Sequence[WizardConfigTrustChainItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostWizardPolicyResponse,
                    parse_obj_as(
                        type_=PostWizardPolicyResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def wizard_api_set_policy_async(
        self,
        *,
        save_state: typing.Optional[bool] = OMIT,
        wizard_config: typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        save_state : typing.Optional[bool]

        wizard_config : typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wizard/push/policy",
            method="POST",
            json={
                "saveState": save_state,
                "wizardConfig": convert_and_respect_annotation_metadata(
                    object_=wizard_config, annotation=WizardApiSetPolicyAsyncRequestWizardConfig, direction="write"
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
                    bool,
                    parse_obj_as(
                        type_=bool,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_policy_config(
        self,
        policy_id: str,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostWizardPolicyIdConfigResponse]:
        """
        Get policy config by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier.

        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostWizardPolicyIdConfigResponse]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wizard/{encode_path_param(policy_id)}/config",
            method="POST",
            json={
                "roles": roles,
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy, annotation=WizardConfigPolicy, direction="write"
                ),
                "schemas": convert_and_respect_annotation_metadata(
                    object_=schemas, annotation=typing.Sequence[WizardConfigSchemasItem], direction="write"
                ),
                "trustChain": convert_and_respect_annotation_metadata(
                    object_=trust_chain, annotation=typing.Sequence[WizardConfigTrustChainItem], direction="write"
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
                    PostWizardPolicyIdConfigResponse,
                    parse_obj_as(
                        type_=PostWizardPolicyIdConfigResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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
