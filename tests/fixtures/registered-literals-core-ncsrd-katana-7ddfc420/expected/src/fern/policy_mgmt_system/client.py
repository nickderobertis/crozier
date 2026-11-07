

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.policy import Policy
from ..types.sbi_ls import SbiLs
from .raw_client import AsyncRawPolicyMgmtSystemClient, RawPolicyMgmtSystemClient


OMIT = typing.cast(typing.Any, ...)


class PolicyMgmtSystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPolicyMgmtSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPolicyMgmtSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPolicyMgmtSystemClient
        """
        return self._raw_client

    def returns_a_list_of_registered_policy_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policy_mgmt_system.returns_a_list_of_registered_policy_systems()
        """
        _response = self._raw_client.returns_a_list_of_registered_policy_systems(request_options=request_options)
        return _response.data

    def adds_a_new_policy_mgmt_system(
        self,
        *,
        id: str,
        url: str,
        type: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        url : str
            The URL of the Policy Management System

        type : str
            The type for new Policy Management System

        description : typing.Optional[str]
            A description for the Policy Management System

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policy_mgmt_system.adds_a_new_policy_mgmt_system(
            id="id",
            url="url",
            type="type",
        )
        """
        _response = self._raw_client.adds_a_new_policy_mgmt_system(
            id=id, url=url, type=type, description=description, request_options=request_options
        )
        return _response.data

    def returns_information_about_the_given_policy_mgmt_system(
        self, policy_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Policy:
        """
        Parameters
        ----------
        policy_system_id : str
            ID of System to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Policy
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policy_mgmt_system.returns_information_about_the_given_policy_mgmt_system(
            policy_system_id="policy_system_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_given_policy_mgmt_system(
            policy_system_id, request_options=request_options
        )
        return _response.data

    def updates_the_given_policy_mgmt_system(
        self, policy_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_system_id : str
            ID of Policy Mgmt System to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policy_mgmt_system.updates_the_given_policy_mgmt_system(
            policy_system_id="policy_system_id",
        )
        """
        _response = self._raw_client.updates_the_given_policy_mgmt_system(
            policy_system_id, request_options=request_options
        )
        return _response.data

    def deletes_the_given_policy_mgmt_system(
        self, policy_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_system_id : str
            ID of Policy Mgmt System to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policy_mgmt_system.deletes_the_given_policy_mgmt_system(
            policy_system_id="policy_system_id",
        )
        """
        _response = self._raw_client.deletes_the_given_policy_mgmt_system(
            policy_system_id, request_options=request_options
        )
        return _response.data

    def sends_the_slice_parameters_to_the_neat_ue_policy_system(
        self, slice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.policy_mgmt_system.sends_the_slice_parameters_to_the_neat_ue_policy_system(
            slice_id="slice_id",
        )
        """
        _response = self._raw_client.sends_the_slice_parameters_to_the_neat_ue_policy_system(
            slice_id, request_options=request_options
        )
        return _response.data


class AsyncPolicyMgmtSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPolicyMgmtSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPolicyMgmtSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPolicyMgmtSystemClient
        """
        return self._raw_client

    async def returns_a_list_of_registered_policy_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.policy_mgmt_system.returns_a_list_of_registered_policy_systems()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_registered_policy_systems(request_options=request_options)
        return _response.data

    async def adds_a_new_policy_mgmt_system(
        self,
        *,
        id: str,
        url: str,
        type: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        url : str
            The URL of the Policy Management System

        type : str
            The type for new Policy Management System

        description : typing.Optional[str]
            A description for the Policy Management System

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
            await client.policy_mgmt_system.adds_a_new_policy_mgmt_system(
                id="id",
                url="url",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adds_a_new_policy_mgmt_system(
            id=id, url=url, type=type, description=description, request_options=request_options
        )
        return _response.data

    async def returns_information_about_the_given_policy_mgmt_system(
        self, policy_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Policy:
        """
        Parameters
        ----------
        policy_system_id : str
            ID of System to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Policy
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.policy_mgmt_system.returns_information_about_the_given_policy_mgmt_system(
                policy_system_id="policy_system_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_given_policy_mgmt_system(
            policy_system_id, request_options=request_options
        )
        return _response.data

    async def updates_the_given_policy_mgmt_system(
        self, policy_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_system_id : str
            ID of Policy Mgmt System to be updated

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
            await client.policy_mgmt_system.updates_the_given_policy_mgmt_system(
                policy_system_id="policy_system_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_given_policy_mgmt_system(
            policy_system_id, request_options=request_options
        )
        return _response.data

    async def deletes_the_given_policy_mgmt_system(
        self, policy_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_system_id : str
            ID of Policy Mgmt System to be deleted

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
            await client.policy_mgmt_system.deletes_the_given_policy_mgmt_system(
                policy_system_id="policy_system_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_given_policy_mgmt_system(
            policy_system_id, request_options=request_options
        )
        return _response.data

    async def sends_the_slice_parameters_to_the_neat_ue_policy_system(
        self, slice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        slice_id : str
            ID of slice

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
            await client.policy_mgmt_system.sends_the_slice_parameters_to_the_neat_ue_policy_system(
                slice_id="slice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sends_the_slice_parameters_to_the_neat_ue_policy_system(
            slice_id, request_options=request_options
        )
        return _response.data
