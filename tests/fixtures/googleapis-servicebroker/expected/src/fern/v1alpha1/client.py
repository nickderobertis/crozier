

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.google_iam_v1policy import GoogleIamV1Policy
from ..types.google_iam_v1test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from .raw_client import AsyncRawV1Alpha1Client, RawV1Alpha1Client
from .types.servicebroker_get_iam_policy_request_alt import ServicebrokerGetIamPolicyRequestAlt
from .types.servicebroker_get_iam_policy_request_xgafv import ServicebrokerGetIamPolicyRequestXgafv
from .types.servicebroker_set_iam_policy_request_alt import ServicebrokerSetIamPolicyRequestAlt
from .types.servicebroker_set_iam_policy_request_xgafv import ServicebrokerSetIamPolicyRequestXgafv
from .types.servicebroker_test_iam_permissions_request_alt import ServicebrokerTestIamPermissionsRequestAlt
from .types.servicebroker_test_iam_permissions_request_xgafv import ServicebrokerTestIamPermissionsRequestXgafv


OMIT = typing.cast(typing.Any, ...)


class V1Alpha1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1Alpha1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1Alpha1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1Alpha1Client
        """
        return self._raw_client

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
    ) -> GoogleIamV1Policy:
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
        GoogleIamV1Policy
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.v1alpha1.servicebroker_get_iam_policy(
            resource="resource",
        )
        """
        _response = self._raw_client.servicebroker_get_iam_policy(
            resource,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            options_requested_policy_version=options_requested_policy_version,
            request_options=request_options,
        )
        return _response.data

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
    ) -> GoogleIamV1Policy:
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
        GoogleIamV1Policy
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.v1alpha1.servicebroker_set_iam_policy(
            resource="resource",
        )
        """
        _response = self._raw_client.servicebroker_set_iam_policy(
            resource,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            policy=policy,
            request_options=request_options,
        )
        return _response.data

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
    ) -> GoogleIamV1TestIamPermissionsResponse:
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
        GoogleIamV1TestIamPermissionsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.v1alpha1.servicebroker_test_iam_permissions(
            resource="resource",
        )
        """
        _response = self._raw_client.servicebroker_test_iam_permissions(
            resource,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            permissions=permissions,
            request_options=request_options,
        )
        return _response.data


class AsyncV1Alpha1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1Alpha1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1Alpha1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1Alpha1Client
        """
        return self._raw_client

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
    ) -> GoogleIamV1Policy:
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
        GoogleIamV1Policy
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.v1alpha1.servicebroker_get_iam_policy(
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_get_iam_policy(
            resource,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            options_requested_policy_version=options_requested_policy_version,
            request_options=request_options,
        )
        return _response.data

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
    ) -> GoogleIamV1Policy:
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
        GoogleIamV1Policy
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.v1alpha1.servicebroker_set_iam_policy(
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_set_iam_policy(
            resource,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            policy=policy,
            request_options=request_options,
        )
        return _response.data

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
    ) -> GoogleIamV1TestIamPermissionsResponse:
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
        GoogleIamV1TestIamPermissionsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.v1alpha1.servicebroker_test_iam_permissions(
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_test_iam_permissions(
            resource,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            permissions=permissions,
            request_options=request_options,
        )
        return _response.data
