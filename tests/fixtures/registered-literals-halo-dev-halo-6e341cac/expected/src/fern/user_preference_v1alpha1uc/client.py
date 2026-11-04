

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserPreferenceV1Alpha1UcClient, RawUserPreferenceV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class UserPreferenceV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserPreferenceV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserPreferenceV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserPreferenceV1Alpha1UcClient
        """
        return self._raw_client

    def get_my_preference(
        self, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get my preference by group.

        Parameters
        ----------
        group : str
            Group of user preference, e.g. `notification`.

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
        client.user_preference_v1alpha1uc.get_my_preference(
            group="group",
        )
        """
        _response = self._raw_client.get_my_preference(group, request_options=request_options)
        return _response.data

    def update_my_preference(
        self,
        group: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create or update my preference by group.

        Parameters
        ----------
        group : str
            Group of user preference, e.g. `notification`.

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
        client.user_preference_v1alpha1uc.update_my_preference(
            group="group",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_my_preference(group, request=request, request_options=request_options)
        return _response.data


class AsyncUserPreferenceV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserPreferenceV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserPreferenceV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserPreferenceV1Alpha1UcClient
        """
        return self._raw_client

    async def get_my_preference(
        self, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get my preference by group.

        Parameters
        ----------
        group : str
            Group of user preference, e.g. `notification`.

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
            await client.user_preference_v1alpha1uc.get_my_preference(
                group="group",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_preference(group, request_options=request_options)
        return _response.data

    async def update_my_preference(
        self,
        group: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create or update my preference by group.

        Parameters
        ----------
        group : str
            Group of user preference, e.g. `notification`.

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
            await client.user_preference_v1alpha1uc.update_my_preference(
                group="group",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_preference(group, request=request, request_options=request_options)
        return _response.data
