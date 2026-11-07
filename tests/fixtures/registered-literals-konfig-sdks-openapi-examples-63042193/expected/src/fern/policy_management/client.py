

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bundle_diff import BundleDiff
from ..types.decision import Decision
from ..types.decision_log import DecisionLog
from ..types.decision_settings import DecisionSettings
from ..types.policy import Policy
from ..types.policy_bundle import PolicyBundle
from ..types.policy_management_get_decision_audit_logs_response import PolicyManagementGetDecisionAuditLogsResponse
from .raw_client import AsyncRawPolicyManagementClient, RawPolicyManagementClient


OMIT = typing.cast(typing.Any, ...)


class PolicyManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPolicyManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPolicyManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPolicyManagementClient
        """
        return self._raw_client

    def policy_management_get_decision_audit_logs(
        self,
        owner_id: str,
        context: str,
        *,
        status: typing.Optional[str] = None,
        after: typing.Optional[dt.datetime] = None,
        before: typing.Optional[dt.datetime] = None,
        branch: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        build_number: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyManagementGetDecisionAuditLogsResponse:
        """
        This endpoint will return a list of decision audit logs that were made using this owner's policies.

        Parameters
        ----------
        owner_id : str

        context : str

        status : typing.Optional[str]
            Return decisions matching this decision status.

        after : typing.Optional[dt.datetime]
            Return decisions made after this date.

        before : typing.Optional[dt.datetime]
            Return decisions made before this date.

        branch : typing.Optional[str]
            Return decisions made on this branch.

        project_id : typing.Optional[str]
            Return decisions made for this project.

        build_number : typing.Optional[str]
            Return decisions made for this build number.

        offset : typing.Optional[int]
            Sets the offset when retrieving the decisions, for paging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyManagementGetDecisionAuditLogsResponse
            Decision logs successfully retrieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_get_decision_audit_logs(
            owner_id="ownerID",
            context="context",
        )
        """
        _response = self._raw_client.policy_management_get_decision_audit_logs(
            owner_id,
            context,
            status=status,
            after=after,
            before=before,
            branch=branch,
            project_id=project_id,
            build_number=build_number,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def policy_management_evaluate_input_data(
        self,
        owner_id: str,
        context: str,
        *,
        input: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Decision:
        """
        This endpoint will evaluate input data (config+metadata) against owner's stored policies and return a decision.

        Parameters
        ----------
        owner_id : str

        context : str

        input : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Decision
            Decision rendered by applying the policy against the provided data. Response will be modeled by the data and rego processed.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_evaluate_input_data(
            owner_id="ownerID",
            context="context",
            input="input",
        )
        """
        _response = self._raw_client.policy_management_evaluate_input_data(
            owner_id, context, input=input, metadata=metadata, request_options=request_options
        )
        return _response.data

    def policy_management_get_decision_settings(
        self, owner_id: str, context: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DecisionSettings:
        """
        This endpoint retrieves the current decision settings (eg enable/disable policy evaluation)

        Parameters
        ----------
        owner_id : str

        context : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecisionSettings
            Decision settings successfully retrieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_get_decision_settings(
            owner_id="ownerID",
            context="context",
        )
        """
        _response = self._raw_client.policy_management_get_decision_settings(
            owner_id, context, request_options=request_options
        )
        return _response.data

    def policy_management_modify_decision_settings(
        self,
        owner_id: str,
        context: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DecisionSettings:
        """
        This endpoint allows modifying decision settings (eg enable/disable policy evaluation)

        Parameters
        ----------
        owner_id : str

        context : str

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecisionSettings
            Decision settings successfully set.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_modify_decision_settings(
            owner_id="ownerID",
            context="context",
        )
        """
        _response = self._raw_client.policy_management_modify_decision_settings(
            owner_id, context, enabled=enabled, request_options=request_options
        )
        return _response.data

    def policy_management_get_decision_audit_log_by_given_id(
        self, owner_id: str, context: str, decision_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DecisionLog:
        """
        This endpoint will retrieve a decision for a given decision log ID

        Parameters
        ----------
        owner_id : str

        context : str

        decision_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecisionLog
            Decision log successfully retrieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_get_decision_audit_log_by_given_id(
            owner_id="ownerID",
            context="context",
            decision_id="decisionID",
        )
        """
        _response = self._raw_client.policy_management_get_decision_audit_log_by_given_id(
            owner_id, context, decision_id, request_options=request_options
        )
        return _response.data

    def policy_management_get_policy_bundle_for_decision(
        self, owner_id: str, context: str, decision_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBundle:
        """
        This endpoint will retrieve a policy bundle for a given decision log ID

        Parameters
        ----------
        owner_id : str

        context : str

        decision_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundle
            Policy-Bundle retrieved successfully for given decision log ID

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_get_policy_bundle_for_decision(
            owner_id="ownerID",
            context="context",
            decision_id="decisionID",
        )
        """
        _response = self._raw_client.policy_management_get_policy_bundle_for_decision(
            owner_id, context, decision_id, request_options=request_options
        )
        return _response.data

    def policy_management_get_policy_bundle(
        self, owner_id: str, context: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBundle:
        """
        This endpoint will retrieve a policy bundle

        Parameters
        ----------
        owner_id : str

        context : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundle
            Policy-Bundle retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_get_policy_bundle(
            owner_id="ownerID",
            context="context",
        )
        """
        _response = self._raw_client.policy_management_get_policy_bundle(
            owner_id, context, request_options=request_options
        )
        return _response.data

    def policy_management_create_policy_bundle_for_context(
        self,
        owner_id: str,
        context: str,
        *,
        dry: typing.Optional[bool] = None,
        policies: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BundleDiff:
        """
        This endpoint replaces the current policy bundle with the provided policy bundle

        Parameters
        ----------
        owner_id : str

        context : str

        dry : typing.Optional[bool]

        policies : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BundleDiff
            Policy-Bundle diff successfully returned.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_create_policy_bundle_for_context(
            owner_id="ownerID",
            context="context",
        )
        """
        _response = self._raw_client.policy_management_create_policy_bundle_for_context(
            owner_id, context, dry=dry, policies=policies, request_options=request_options
        )
        return _response.data

    def policy_management_get_document(
        self, owner_id: str, context: str, policy_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Policy:
        """
        This endpoint will retrieve a policy document.

        Parameters
        ----------
        owner_id : str

        context : str

        policy_name : str
            the policy name set by the rego policy_name rule

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Policy
            Policy retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.policy_management.policy_management_get_document(
            owner_id="ownerID",
            context="context",
            policy_name="policyName",
        )
        """
        _response = self._raw_client.policy_management_get_document(
            owner_id, context, policy_name, request_options=request_options
        )
        return _response.data


class AsyncPolicyManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPolicyManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPolicyManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPolicyManagementClient
        """
        return self._raw_client

    async def policy_management_get_decision_audit_logs(
        self,
        owner_id: str,
        context: str,
        *,
        status: typing.Optional[str] = None,
        after: typing.Optional[dt.datetime] = None,
        before: typing.Optional[dt.datetime] = None,
        branch: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        build_number: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyManagementGetDecisionAuditLogsResponse:
        """
        This endpoint will return a list of decision audit logs that were made using this owner's policies.

        Parameters
        ----------
        owner_id : str

        context : str

        status : typing.Optional[str]
            Return decisions matching this decision status.

        after : typing.Optional[dt.datetime]
            Return decisions made after this date.

        before : typing.Optional[dt.datetime]
            Return decisions made before this date.

        branch : typing.Optional[str]
            Return decisions made on this branch.

        project_id : typing.Optional[str]
            Return decisions made for this project.

        build_number : typing.Optional[str]
            Return decisions made for this build number.

        offset : typing.Optional[int]
            Sets the offset when retrieving the decisions, for paging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyManagementGetDecisionAuditLogsResponse
            Decision logs successfully retrieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_get_decision_audit_logs(
                owner_id="ownerID",
                context="context",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_get_decision_audit_logs(
            owner_id,
            context,
            status=status,
            after=after,
            before=before,
            branch=branch,
            project_id=project_id,
            build_number=build_number,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def policy_management_evaluate_input_data(
        self,
        owner_id: str,
        context: str,
        *,
        input: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Decision:
        """
        This endpoint will evaluate input data (config+metadata) against owner's stored policies and return a decision.

        Parameters
        ----------
        owner_id : str

        context : str

        input : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Decision
            Decision rendered by applying the policy against the provided data. Response will be modeled by the data and rego processed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_evaluate_input_data(
                owner_id="ownerID",
                context="context",
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_evaluate_input_data(
            owner_id, context, input=input, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def policy_management_get_decision_settings(
        self, owner_id: str, context: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DecisionSettings:
        """
        This endpoint retrieves the current decision settings (eg enable/disable policy evaluation)

        Parameters
        ----------
        owner_id : str

        context : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecisionSettings
            Decision settings successfully retrieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_get_decision_settings(
                owner_id="ownerID",
                context="context",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_get_decision_settings(
            owner_id, context, request_options=request_options
        )
        return _response.data

    async def policy_management_modify_decision_settings(
        self,
        owner_id: str,
        context: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DecisionSettings:
        """
        This endpoint allows modifying decision settings (eg enable/disable policy evaluation)

        Parameters
        ----------
        owner_id : str

        context : str

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecisionSettings
            Decision settings successfully set.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_modify_decision_settings(
                owner_id="ownerID",
                context="context",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_modify_decision_settings(
            owner_id, context, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def policy_management_get_decision_audit_log_by_given_id(
        self, owner_id: str, context: str, decision_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DecisionLog:
        """
        This endpoint will retrieve a decision for a given decision log ID

        Parameters
        ----------
        owner_id : str

        context : str

        decision_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecisionLog
            Decision log successfully retrieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_get_decision_audit_log_by_given_id(
                owner_id="ownerID",
                context="context",
                decision_id="decisionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_get_decision_audit_log_by_given_id(
            owner_id, context, decision_id, request_options=request_options
        )
        return _response.data

    async def policy_management_get_policy_bundle_for_decision(
        self, owner_id: str, context: str, decision_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBundle:
        """
        This endpoint will retrieve a policy bundle for a given decision log ID

        Parameters
        ----------
        owner_id : str

        context : str

        decision_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundle
            Policy-Bundle retrieved successfully for given decision log ID

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_get_policy_bundle_for_decision(
                owner_id="ownerID",
                context="context",
                decision_id="decisionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_get_policy_bundle_for_decision(
            owner_id, context, decision_id, request_options=request_options
        )
        return _response.data

    async def policy_management_get_policy_bundle(
        self, owner_id: str, context: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBundle:
        """
        This endpoint will retrieve a policy bundle

        Parameters
        ----------
        owner_id : str

        context : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundle
            Policy-Bundle retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_get_policy_bundle(
                owner_id="ownerID",
                context="context",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_get_policy_bundle(
            owner_id, context, request_options=request_options
        )
        return _response.data

    async def policy_management_create_policy_bundle_for_context(
        self,
        owner_id: str,
        context: str,
        *,
        dry: typing.Optional[bool] = None,
        policies: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BundleDiff:
        """
        This endpoint replaces the current policy bundle with the provided policy bundle

        Parameters
        ----------
        owner_id : str

        context : str

        dry : typing.Optional[bool]

        policies : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BundleDiff
            Policy-Bundle diff successfully returned.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_create_policy_bundle_for_context(
                owner_id="ownerID",
                context="context",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_create_policy_bundle_for_context(
            owner_id, context, dry=dry, policies=policies, request_options=request_options
        )
        return _response.data

    async def policy_management_get_document(
        self, owner_id: str, context: str, policy_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Policy:
        """
        This endpoint will retrieve a policy document.

        Parameters
        ----------
        owner_id : str

        context : str

        policy_name : str
            the policy name set by the rego policy_name rule

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Policy
            Policy retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.policy_management.policy_management_get_document(
                owner_id="ownerID",
                context="context",
                policy_name="policyName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_management_get_document(
            owner_id, context, policy_name, request_options=request_options
        )
        return _response.data
