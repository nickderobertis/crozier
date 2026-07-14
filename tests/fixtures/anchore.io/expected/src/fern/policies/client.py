

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.image_selection_rule import ImageSelectionRule
from ..types.mapping_rule import MappingRule
from ..types.policy import Policy
from ..types.policy_bundle import PolicyBundle
from ..types.policy_bundle_list import PolicyBundleList
from ..types.policy_bundle_record import PolicyBundleRecord
from ..types.whitelist import Whitelist
from .raw_client import AsyncRawPoliciesClient, RawPoliciesClient


OMIT = typing.cast(typing.Any, ...)


class PoliciesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPoliciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPoliciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPoliciesClient
        """
        return self._raw_client

    def list_policies(
        self,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleList:
        """
        List all saved policy bundles

        Parameters
        ----------
        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleList
            Policy listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policies.list_policies()
        """
        _response = self._raw_client.list_policies(
            detail=detail, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def add_policy(
        self,
        *,
        id: str,
        mappings: typing.Sequence[MappingRule],
        policies: typing.Sequence[Policy],
        version: str,
        anchore_account: typing.Optional[str] = None,
        blacklisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        whitelisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        whitelists: typing.Optional[typing.Sequence[Whitelist]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleRecord:
        """
        Adds a new policy bundle to the system

        Parameters
        ----------
        id : str
            Id of the bundle

        mappings : typing.Sequence[MappingRule]
            Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order.

        policies : typing.Sequence[Policy]
            Policies which define the go/stop/warn status of an image using rule matches on image properties

        version : str
            Version id for this bundle format

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        blacklisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images

        comment : typing.Optional[str]
            Description of the bundle, human readable

        name : typing.Optional[str]
            Human readable name for the bundle

        whitelisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result.

        whitelists : typing.Optional[typing.Sequence[Whitelist]]
            Whitelists which define which policy matches to disregard explicitly in the final policy decision

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleRecord
            Saved bundle

        Examples
        --------
        from fern import FernApi, ImageRef, ImageRefType, MappingRule, Policy

        client = FernApi()
        client.policies.add_policy(
            id="id",
            mappings=[
                MappingRule(
                    image=ImageRef(
                        type=ImageRefType.TAG,
                        value="value",
                    ),
                    name="name",
                    registry="registry",
                    repository="repository",
                )
            ],
            policies=[
                Policy(
                    id="id",
                    version="version",
                )
            ],
            version="version",
        )
        """
        _response = self._raw_client.add_policy(
            id=id,
            mappings=mappings,
            policies=policies,
            version=version,
            anchore_account=anchore_account,
            blacklisted_images=blacklisted_images,
            comment=comment,
            name=name,
            whitelisted_images=whitelisted_images,
            whitelists=whitelists,
            request_options=request_options,
        )
        return _response.data

    def get_policy(
        self,
        policy_id: str,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleList:
        """
        Get the policy bundle content

        Parameters
        ----------
        policy_id : str

        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleList
            A list with a single fetched policy bundle record

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policies.get_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.get_policy(
            policy_id, detail=detail, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def update_policy(
        self,
        policy_id_: str,
        *,
        active: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        policy_bundle_record_active: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        policy_source: typing.Optional[str] = OMIT,
        policybundle: typing.Optional[PolicyBundle] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleList:
        """
        Update/replace and existing policy

        Parameters
        ----------
        policy_id_ : str

        active : typing.Optional[bool]
            Mark policy as active

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        policy_bundle_record_active : typing.Optional[bool]
            True if the bundle is currently defined to be used automatically

        created_at : typing.Optional[dt.datetime]

        last_updated : typing.Optional[dt.datetime]

        policy_id : typing.Optional[str]
            The bundle's identifier

        policy_source : typing.Optional[str]
            Source location of where the policy bundle originated

        policybundle : typing.Optional[PolicyBundle]

        user_id : typing.Optional[str]
            UserId of the user that owns the bundle

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleList
            A list with a single updated policy bundle record

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policies.update_policy(
            policy_id_="policyId",
        )
        """
        _response = self._raw_client.update_policy(
            policy_id_,
            active=active,
            anchore_account=anchore_account,
            policy_bundle_record_active=policy_bundle_record_active,
            created_at=created_at,
            last_updated=last_updated,
            policy_id=policy_id,
            policy_source=policy_source,
            policybundle=policybundle,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def delete_policy(
        self,
        policy_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete the specified policy

        Parameters
        ----------
        policy_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policies.delete_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.delete_policy(
            policy_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data


class AsyncPoliciesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPoliciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPoliciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPoliciesClient
        """
        return self._raw_client

    async def list_policies(
        self,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleList:
        """
        List all saved policy bundles

        Parameters
        ----------
        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleList
            Policy listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.policies.list_policies()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_policies(
            detail=detail, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def add_policy(
        self,
        *,
        id: str,
        mappings: typing.Sequence[MappingRule],
        policies: typing.Sequence[Policy],
        version: str,
        anchore_account: typing.Optional[str] = None,
        blacklisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        whitelisted_images: typing.Optional[typing.Sequence[ImageSelectionRule]] = OMIT,
        whitelists: typing.Optional[typing.Sequence[Whitelist]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleRecord:
        """
        Adds a new policy bundle to the system

        Parameters
        ----------
        id : str
            Id of the bundle

        mappings : typing.Sequence[MappingRule]
            Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order.

        policies : typing.Sequence[Policy]
            Policies which define the go/stop/warn status of an image using rule matches on image properties

        version : str
            Version id for this bundle format

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        blacklisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images

        comment : typing.Optional[str]
            Description of the bundle, human readable

        name : typing.Optional[str]
            Human readable name for the bundle

        whitelisted_images : typing.Optional[typing.Sequence[ImageSelectionRule]]
            List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result.

        whitelists : typing.Optional[typing.Sequence[Whitelist]]
            Whitelists which define which policy matches to disregard explicitly in the final policy decision

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleRecord
            Saved bundle

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ImageRef, ImageRefType, MappingRule, Policy

        client = AsyncFernApi()


        async def main() -> None:
            await client.policies.add_policy(
                id="id",
                mappings=[
                    MappingRule(
                        image=ImageRef(
                            type=ImageRefType.TAG,
                            value="value",
                        ),
                        name="name",
                        registry="registry",
                        repository="repository",
                    )
                ],
                policies=[
                    Policy(
                        id="id",
                        version="version",
                    )
                ],
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_policy(
            id=id,
            mappings=mappings,
            policies=policies,
            version=version,
            anchore_account=anchore_account,
            blacklisted_images=blacklisted_images,
            comment=comment,
            name=name,
            whitelisted_images=whitelisted_images,
            whitelists=whitelists,
            request_options=request_options,
        )
        return _response.data

    async def get_policy(
        self,
        policy_id: str,
        *,
        detail: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleList:
        """
        Get the policy bundle content

        Parameters
        ----------
        policy_id : str

        detail : typing.Optional[bool]
            Include policy bundle detail in the form of the full bundle content for each entry

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleList
            A list with a single fetched policy bundle record

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.policies.get_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_policy(
            policy_id, detail=detail, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def update_policy(
        self,
        policy_id_: str,
        *,
        active: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        policy_bundle_record_active: typing.Optional[bool] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        policy_source: typing.Optional[str] = OMIT,
        policybundle: typing.Optional[PolicyBundle] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBundleList:
        """
        Update/replace and existing policy

        Parameters
        ----------
        policy_id_ : str

        active : typing.Optional[bool]
            Mark policy as active

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        policy_bundle_record_active : typing.Optional[bool]
            True if the bundle is currently defined to be used automatically

        created_at : typing.Optional[dt.datetime]

        last_updated : typing.Optional[dt.datetime]

        policy_id : typing.Optional[str]
            The bundle's identifier

        policy_source : typing.Optional[str]
            Source location of where the policy bundle originated

        policybundle : typing.Optional[PolicyBundle]

        user_id : typing.Optional[str]
            UserId of the user that owns the bundle

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBundleList
            A list with a single updated policy bundle record

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.policies.update_policy(
                policy_id_="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_policy(
            policy_id_,
            active=active,
            anchore_account=anchore_account,
            policy_bundle_record_active=policy_bundle_record_active,
            created_at=created_at,
            last_updated=last_updated,
            policy_id=policy_id,
            policy_source=policy_source,
            policybundle=policybundle,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_policy(
        self,
        policy_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete the specified policy

        Parameters
        ----------
        policy_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.policies.delete_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_policy(
            policy_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data
