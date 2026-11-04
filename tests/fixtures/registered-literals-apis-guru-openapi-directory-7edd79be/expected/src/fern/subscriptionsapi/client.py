

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_credentials import ApiCredentials
from ..types.count_of import CountOf
from ..types.find_credentials import FindCredentials
from ..types.key_view import KeyView
from ..types.subscription_create_modify import SubscriptionCreateModify
from ..types.subscription_view import SubscriptionView
from .raw_client import AsyncRawSubscriptionsapiClient, RawSubscriptionsapiClient


OMIT = typing.cast(typing.Any, ...)


class SubscriptionsapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionsapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionsapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionsapiClient
        """
        return self._raw_client

    def putsubscription2(
        self,
        *,
        request: typing.Optional[SubscriptionCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[SubscriptionCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, SubscriptionCreateModify

        client = FernApi()
        client.subscriptionsapi.putsubscription2(
            request=SubscriptionCreateModify(
                action="action",
                frequency="frequency",
            ),
        )
        """
        _response = self._raw_client.putsubscription2(request=request, request_options=request_options)
        return _response.data

    def putsubscription(
        self,
        *,
        request: typing.Optional[SubscriptionCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[SubscriptionCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, SubscriptionCreateModify

        client = FernApi()
        client.subscriptionsapi.putsubscription(
            request=SubscriptionCreateModify(
                action="action",
                frequency="frequency",
            ),
        )
        """
        _response = self._raw_client.putsubscription(request=request, request_options=request_options)
        return _response.data

    def count(
        self,
        *,
        request: typing.Optional[ApiCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CountOf]:
        """
        Parameters
        ----------
        request : typing.Optional[ApiCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CountOf]


        Examples
        --------
        from fern import ApiCredentials, FernApi

        client = FernApi()
        client.subscriptionsapi.count(
            request=ApiCredentials(),
        )
        """
        _response = self._raw_client.count(request=request, request_options=request_options)
        return _response.data

    def disable2(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.subscriptionsapi.disable2(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.disable2(request=request, request_options=request_options)
        return _response.data

    def disable(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.subscriptionsapi.disable(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.disable(request=request, request_options=request_options)
        return _response.data

    def enable2(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.subscriptionsapi.enable2(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.enable2(request=request, request_options=request_options)
        return _response.data

    def enable(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.subscriptionsapi.enable(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.enable(request=request, request_options=request_options)
        return _response.data

    def find(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[SubscriptionView]:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SubscriptionView]


        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.subscriptionsapi.find(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.find(request=request, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[SubscriptionView]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[SubscriptionView]]


        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.subscriptionsapi.list(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.list(page=page, request=request, request_options=request_options)
        return _response.data

    def save(
        self,
        *,
        request: typing.Optional[SubscriptionCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[KeyView]:
        """
        Parameters
        ----------
        request : typing.Optional[SubscriptionCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[KeyView]


        Examples
        --------
        from fern import FernApi, SubscriptionCreateModify

        client = FernApi()
        client.subscriptionsapi.save(
            request=SubscriptionCreateModify(
                action="action",
                frequency="frequency",
            ),
        )
        """
        _response = self._raw_client.save(request=request, request_options=request_options)
        return _response.data

    def deletesubscription2(
        self,
        serial: str,
        *,
        api_key: str,
        keep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        keep : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptionsapi.deletesubscription2(
            serial="serial",
            api_key="X-Api-Key",
            keep=True,
        )
        """
        _response = self._raw_client.deletesubscription2(
            serial, api_key=api_key, keep=keep, request_options=request_options
        )
        return _response.data

    def deletesubscription(
        self,
        serial: str,
        *,
        api_key: str,
        keep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        keep : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptionsapi.deletesubscription(
            serial="serial",
            api_key="X-Api-Key",
            keep=True,
        )
        """
        _response = self._raw_client.deletesubscription(
            serial, api_key=api_key, keep=keep, request_options=request_options
        )
        return _response.data


class AsyncSubscriptionsapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionsapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionsapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionsapiClient
        """
        return self._raw_client

    async def putsubscription2(
        self,
        *,
        request: typing.Optional[SubscriptionCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[SubscriptionCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SubscriptionCreateModify

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.putsubscription2(
                request=SubscriptionCreateModify(
                    action="action",
                    frequency="frequency",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putsubscription2(request=request, request_options=request_options)
        return _response.data

    async def putsubscription(
        self,
        *,
        request: typing.Optional[SubscriptionCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[SubscriptionCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SubscriptionCreateModify

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.putsubscription(
                request=SubscriptionCreateModify(
                    action="action",
                    frequency="frequency",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putsubscription(request=request, request_options=request_options)
        return _response.data

    async def count(
        self,
        *,
        request: typing.Optional[ApiCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CountOf]:
        """
        Parameters
        ----------
        request : typing.Optional[ApiCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CountOf]


        Examples
        --------
        import asyncio

        from fern import ApiCredentials, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.count(
                request=ApiCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count(request=request, request_options=request_options)
        return _response.data

    async def disable2(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.disable2(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable2(request=request, request_options=request_options)
        return _response.data

    async def disable(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.disable(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable(request=request, request_options=request_options)
        return _response.data

    async def enable2(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.enable2(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable2(request=request, request_options=request_options)
        return _response.data

    async def enable(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.enable(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable(request=request, request_options=request_options)
        return _response.data

    async def find(
        self,
        *,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[SubscriptionView]:
        """
        Parameters
        ----------
        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SubscriptionView]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.find(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find(request=request, request_options=request_options)
        return _response.data

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[SubscriptionView]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[SubscriptionView]]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.list(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(page=page, request=request, request_options=request_options)
        return _response.data

    async def save(
        self,
        *,
        request: typing.Optional[SubscriptionCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[KeyView]:
        """
        Parameters
        ----------
        request : typing.Optional[SubscriptionCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[KeyView]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SubscriptionCreateModify

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptionsapi.save(
                request=SubscriptionCreateModify(
                    action="action",
                    frequency="frequency",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save(request=request, request_options=request_options)
        return _response.data

    async def deletesubscription2(
        self,
        serial: str,
        *,
        api_key: str,
        keep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        keep : typing.Optional[bool]

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
            await client.subscriptionsapi.deletesubscription2(
                serial="serial",
                api_key="X-Api-Key",
                keep=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletesubscription2(
            serial, api_key=api_key, keep=keep, request_options=request_options
        )
        return _response.data

    async def deletesubscription(
        self,
        serial: str,
        *,
        api_key: str,
        keep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        keep : typing.Optional[bool]

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
            await client.subscriptionsapi.deletesubscription(
                serial="serial",
                api_key="X-Api-Key",
                keep=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletesubscription(
            serial, api_key=api_key, keep=keep, request_options=request_options
        )
        return _response.data
