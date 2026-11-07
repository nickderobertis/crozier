

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPolicyAlpha1ConsoleClient, RawPolicyAlpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class PolicyAlpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPolicyAlpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPolicyAlpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPolicyAlpha1ConsoleClient
        """
        return self._raw_client

    def get_policy_config_by_group(
        self, name: str, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get policy config by group

        Parameters
        ----------
        name : str
            metadata.name of the policy

        group : str
            Config group name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.policy_alpha1console.get_policy_config_by_group(
            name="name",
            group="group",
        )
        """
        _response = self._raw_client.get_policy_config_by_group(name, group, request_options=request_options)
        return _response.data

    def update_policy_config_by_group(
        self,
        name: str,
        group: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update policy config by group

        Parameters
        ----------
        name : str
            metadata.name of the policy

        group : str
            Config group name

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.policy_alpha1console.update_policy_config_by_group(
            name="name",
            group="group",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_policy_config_by_group(
            name, group, request=request, request_options=request_options
        )
        return _response.data


class AsyncPolicyAlpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPolicyAlpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPolicyAlpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPolicyAlpha1ConsoleClient
        """
        return self._raw_client

    async def get_policy_config_by_group(
        self, name: str, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get policy config by group

        Parameters
        ----------
        name : str
            metadata.name of the policy

        group : str
            Config group name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.policy_alpha1console.get_policy_config_by_group(
                name="name",
                group="group",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_policy_config_by_group(name, group, request_options=request_options)
        return _response.data

    async def update_policy_config_by_group(
        self,
        name: str,
        group: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update policy config by group

        Parameters
        ----------
        name : str
            metadata.name of the policy

        group : str
            Config group name

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.policy_alpha1console.update_policy_config_by_group(
                name="name",
                group="group",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_policy_config_by_group(
            name, group, request=request, request_options=request_options
        )
        return _response.data
