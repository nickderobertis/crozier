

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
from ..types.google_iam_v1policy import GoogleIamV1Policy
from ..types.google_iam_v1test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from .types.servicebroker_get_iam_policy_request_alt import ServicebrokerGetIamPolicyRequestAlt
from .types.servicebroker_get_iam_policy_request_xgafv import ServicebrokerGetIamPolicyRequestXgafv
from .types.servicebroker_set_iam_policy_request_alt import ServicebrokerSetIamPolicyRequestAlt
from .types.servicebroker_set_iam_policy_request_xgafv import ServicebrokerSetIamPolicyRequestXgafv
from .types.servicebroker_test_iam_permissions_request_alt import ServicebrokerTestIamPermissionsRequestAlt
from .types.servicebroker_test_iam_permissions_request_xgafv import ServicebrokerTestIamPermissionsRequestXgafv
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawV1Alpha1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def servicebroker_get_iam_policy(
        self,
        resource: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerGetIamPolicyRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerGetIamPolicyRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        options_requested_policy_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GoogleIamV1Policy]:
        """
        Gets the access control policy for a resource.
        Returns an empty policy if the resource exists and does not have a policy
        set.

        Parameters
        ----------
        resource : str
            REQUIRED: The resource for which the policy is being requested.
            See the operation documentation for the appropriate value for this field.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerGetIamPolicyRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerGetIamPolicyRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        options_requested_policy_version : typing.Optional[int]
            Optional. The policy format version to be returned.

            Valid values are 0, 1, and 3. Requests specifying an invalid value will be
            rejected.

            Requests for policies with any conditional bindings must specify version 3.
            Policies without any conditional bindings may specify any valid value or
            leave the field unset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GoogleIamV1Policy]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1alpha1/{encode_path_param(resource)}:getIamPolicy",
            method="GET",
            params={
                "upload_protocol": upload_protocol,
                "quotaUser": quota_user,
                "prettyPrint": pretty_print,
                "uploadType": upload_type,
                "fields": fields,
                "callback": callback,
                "oauth_token": oauth_token,
                "$.xgafv": xgafv,
                "alt": alt,
                "key": key,
                "access_token": access_token,
                "options.requestedPolicyVersion": options_requested_policy_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GoogleIamV1Policy,
                    parse_obj_as(
                        type_=GoogleIamV1Policy,
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

    def servicebroker_set_iam_policy(
        self,
        resource: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerSetIamPolicyRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerSetIamPolicyRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        policy: typing.Optional[GoogleIamV1Policy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GoogleIamV1Policy]:
        """
        Sets the access control policy on the specified resource. Replaces any
        existing policy.

        Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

        Parameters
        ----------
        resource : str
            REQUIRED: The resource for which the policy is being specified.
            See the operation documentation for the appropriate value for this field.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerSetIamPolicyRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerSetIamPolicyRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        policy : typing.Optional[GoogleIamV1Policy]
            REQUIRED: The complete policy to be applied to the `resource`. The size of
            the policy is limited to a few 10s of KB. An empty policy is a
            valid policy but certain Cloud Platform services (such as Projects)
            might reject them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GoogleIamV1Policy]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1alpha1/{encode_path_param(resource)}:setIamPolicy",
            method="POST",
            params={
                "upload_protocol": upload_protocol,
                "quotaUser": quota_user,
                "prettyPrint": pretty_print,
                "uploadType": upload_type,
                "fields": fields,
                "callback": callback,
                "oauth_token": oauth_token,
                "$.xgafv": xgafv,
                "alt": alt,
                "key": key,
                "access_token": access_token,
            },
            json={
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy, annotation=GoogleIamV1Policy, direction="write"
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
                    GoogleIamV1Policy,
                    parse_obj_as(
                        type_=GoogleIamV1Policy,
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

    def servicebroker_test_iam_permissions(
        self,
        resource: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerTestIamPermissionsRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerTestIamPermissionsRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        permissions: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GoogleIamV1TestIamPermissionsResponse]:
        """
        Returns permissions that a caller has on the specified resource.
        If the resource does not exist, this will return an empty set of
        permissions, not a NOT_FOUND error.

        Note: This operation is designed to be used for building permission-aware
        UIs and command-line tools, not for authorization checking. This operation
        may "fail open" without warning.

        Parameters
        ----------
        resource : str
            REQUIRED: The resource for which the policy detail is being requested.
            See the operation documentation for the appropriate value for this field.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerTestIamPermissionsRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerTestIamPermissionsRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        permissions : typing.Optional[typing.Sequence[str]]
            The set of permissions to check for the `resource`. Permissions with
            wildcards (such as '*' or 'storage.*') are not allowed. For more
            information see
            [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GoogleIamV1TestIamPermissionsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1alpha1/{encode_path_param(resource)}:testIamPermissions",
            method="POST",
            params={
                "upload_protocol": upload_protocol,
                "quotaUser": quota_user,
                "prettyPrint": pretty_print,
                "uploadType": upload_type,
                "fields": fields,
                "callback": callback,
                "oauth_token": oauth_token,
                "$.xgafv": xgafv,
                "alt": alt,
                "key": key,
                "access_token": access_token,
            },
            json={
                "permissions": permissions,
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
                    GoogleIamV1TestIamPermissionsResponse,
                    parse_obj_as(
                        type_=GoogleIamV1TestIamPermissionsResponse,
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


class AsyncRawV1Alpha1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def servicebroker_get_iam_policy(
        self,
        resource: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerGetIamPolicyRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerGetIamPolicyRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        options_requested_policy_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GoogleIamV1Policy]:
        """
        Gets the access control policy for a resource.
        Returns an empty policy if the resource exists and does not have a policy
        set.

        Parameters
        ----------
        resource : str
            REQUIRED: The resource for which the policy is being requested.
            See the operation documentation for the appropriate value for this field.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerGetIamPolicyRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerGetIamPolicyRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        options_requested_policy_version : typing.Optional[int]
            Optional. The policy format version to be returned.

            Valid values are 0, 1, and 3. Requests specifying an invalid value will be
            rejected.

            Requests for policies with any conditional bindings must specify version 3.
            Policies without any conditional bindings may specify any valid value or
            leave the field unset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GoogleIamV1Policy]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1alpha1/{encode_path_param(resource)}:getIamPolicy",
            method="GET",
            params={
                "upload_protocol": upload_protocol,
                "quotaUser": quota_user,
                "prettyPrint": pretty_print,
                "uploadType": upload_type,
                "fields": fields,
                "callback": callback,
                "oauth_token": oauth_token,
                "$.xgafv": xgafv,
                "alt": alt,
                "key": key,
                "access_token": access_token,
                "options.requestedPolicyVersion": options_requested_policy_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GoogleIamV1Policy,
                    parse_obj_as(
                        type_=GoogleIamV1Policy,
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

    async def servicebroker_set_iam_policy(
        self,
        resource: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerSetIamPolicyRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerSetIamPolicyRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        policy: typing.Optional[GoogleIamV1Policy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GoogleIamV1Policy]:
        """
        Sets the access control policy on the specified resource. Replaces any
        existing policy.

        Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

        Parameters
        ----------
        resource : str
            REQUIRED: The resource for which the policy is being specified.
            See the operation documentation for the appropriate value for this field.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerSetIamPolicyRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerSetIamPolicyRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        policy : typing.Optional[GoogleIamV1Policy]
            REQUIRED: The complete policy to be applied to the `resource`. The size of
            the policy is limited to a few 10s of KB. An empty policy is a
            valid policy but certain Cloud Platform services (such as Projects)
            might reject them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GoogleIamV1Policy]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1alpha1/{encode_path_param(resource)}:setIamPolicy",
            method="POST",
            params={
                "upload_protocol": upload_protocol,
                "quotaUser": quota_user,
                "prettyPrint": pretty_print,
                "uploadType": upload_type,
                "fields": fields,
                "callback": callback,
                "oauth_token": oauth_token,
                "$.xgafv": xgafv,
                "alt": alt,
                "key": key,
                "access_token": access_token,
            },
            json={
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy, annotation=GoogleIamV1Policy, direction="write"
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
                    GoogleIamV1Policy,
                    parse_obj_as(
                        type_=GoogleIamV1Policy,
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

    async def servicebroker_test_iam_permissions(
        self,
        resource: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerTestIamPermissionsRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerTestIamPermissionsRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        permissions: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GoogleIamV1TestIamPermissionsResponse]:
        """
        Returns permissions that a caller has on the specified resource.
        If the resource does not exist, this will return an empty set of
        permissions, not a NOT_FOUND error.

        Note: This operation is designed to be used for building permission-aware
        UIs and command-line tools, not for authorization checking. This operation
        may "fail open" without warning.

        Parameters
        ----------
        resource : str
            REQUIRED: The resource for which the policy detail is being requested.
            See the operation documentation for the appropriate value for this field.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerTestIamPermissionsRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerTestIamPermissionsRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        permissions : typing.Optional[typing.Sequence[str]]
            The set of permissions to check for the `resource`. Permissions with
            wildcards (such as '*' or 'storage.*') are not allowed. For more
            information see
            [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GoogleIamV1TestIamPermissionsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1alpha1/{encode_path_param(resource)}:testIamPermissions",
            method="POST",
            params={
                "upload_protocol": upload_protocol,
                "quotaUser": quota_user,
                "prettyPrint": pretty_print,
                "uploadType": upload_type,
                "fields": fields,
                "callback": callback,
                "oauth_token": oauth_token,
                "$.xgafv": xgafv,
                "alt": alt,
                "key": key,
                "access_token": access_token,
            },
            json={
                "permissions": permissions,
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
                    GoogleIamV1TestIamPermissionsResponse,
                    parse_obj_as(
                        type_=GoogleIamV1TestIamPermissionsResponse,
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
