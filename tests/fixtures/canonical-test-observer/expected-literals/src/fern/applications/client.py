

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.application_response import ApplicationResponse
from ..types.permission import Permission
from .raw_client import AsyncRawApplicationsClient, RawApplicationsClient


OMIT = typing.cast(typing.Any, ...)


class ApplicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplicationsClient
        """
        return self._raw_client

    def get_applications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.get_applications()
        """
        _response = self._raw_client.get_applications(request_options=request_options)
        return _response.data

    def create_application(
        self,
        *,
        name: str,
        permissions: typing.Sequence[Permission],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        name : str

        permissions : typing.Sequence[Permission]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.create_application(
            name="name",
            permissions=["view_user"],
        )
        """
        _response = self._raw_client.create_application(
            name=name, permissions=permissions, request_options=request_options
        )
        return _response.data

    def rotate_own_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApplicationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.rotate_own_api_key()
        """
        _response = self._raw_client.rotate_own_api_key(request_options=request_options)
        return _response.data

    def rotate_api_key(
        self, application_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        application_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.rotate_api_key(
            application_id=1,
        )
        """
        _response = self._raw_client.rotate_api_key(application_id, request_options=request_options)
        return _response.data

    def get_authenticated_application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ApplicationResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.get_authenticated_application()
        """
        _response = self._raw_client.get_authenticated_application(request_options=request_options)
        return _response.data

    def get_application(
        self, application_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        application_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.get_application(
            application_id=1,
        )
        """
        _response = self._raw_client.get_application(application_id, request_options=request_options)
        return _response.data

    def delete_application(
        self, application_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        application_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.delete_application(
            application_id=1,
        )
        """
        _response = self._raw_client.delete_application(application_id, request_options=request_options)
        return _response.data

    def update_application(
        self,
        application_id: int,
        *,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        application_id : int

        permissions : typing.Optional[typing.Sequence[Permission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.update_application(
            application_id=1,
        )
        """
        _response = self._raw_client.update_application(
            application_id, permissions=permissions, request_options=request_options
        )
        return _response.data


class AsyncApplicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplicationsClient
        """
        return self._raw_client

    async def get_applications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.get_applications()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_applications(request_options=request_options)
        return _response.data

    async def create_application(
        self,
        *,
        name: str,
        permissions: typing.Sequence[Permission],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        name : str

        permissions : typing.Sequence[Permission]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.create_application(
                name="name",
                permissions=["view_user"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_application(
            name=name, permissions=permissions, request_options=request_options
        )
        return _response.data

    async def rotate_own_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.rotate_own_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.rotate_own_api_key(request_options=request_options)
        return _response.data

    async def rotate_api_key(
        self, application_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        application_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.rotate_api_key(
                application_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rotate_api_key(application_id, request_options=request_options)
        return _response.data

    async def get_authenticated_application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ApplicationResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.get_authenticated_application()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authenticated_application(request_options=request_options)
        return _response.data

    async def get_application(
        self, application_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        application_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.get_application(
                application_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application(application_id, request_options=request_options)
        return _response.data

    async def delete_application(
        self, application_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        application_id : int

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
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.delete_application(
                application_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_application(application_id, request_options=request_options)
        return _response.data

    async def update_application(
        self,
        application_id: int,
        *,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        application_id : int

        permissions : typing.Optional[typing.Sequence[Permission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.update_application(
                application_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_application(
            application_id, permissions=permissions, request_options=request_options
        )
        return _response.data
