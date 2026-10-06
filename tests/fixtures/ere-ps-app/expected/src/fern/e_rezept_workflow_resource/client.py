

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_cards_response import GetCardsResponse
from ..types.get_signature_mode_response_event import GetSignatureModeResponseEvent
from .raw_client import AsyncRawERezeptWorkflowResourceClient, RawERezeptWorkflowResourceClient


OMIT = typing.cast(typing.Any, ...)


class ERezeptWorkflowResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawERezeptWorkflowResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawERezeptWorkflowResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawERezeptWorkflowResourceClient
        """
        return self._raw_client

    def post_workflow_abort(
        self,
        *,
        task_id: typing.Optional[str] = OMIT,
        access_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        task_id : typing.Optional[str]

        access_code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_abort()
        """
        _response = self._raw_client.post_workflow_abort(
            task_id=task_id, access_code=access_code, request_options=request_options
        )
        return _response.data

    def post_workflow_batch_sign(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_batch_sign()
        """
        _response = self._raw_client.post_workflow_batch_sign(request_options=request_options)
        return _response.data

    def get_workflow_cards(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetCardsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCardsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.get_workflow_cards()
        """
        _response = self._raw_client.get_workflow_cards(request_options=request_options)
        return _response.data

    def post_workflow_comfortsignature_activate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_comfortsignature_activate()
        """
        _response = self._raw_client.post_workflow_comfortsignature_activate(request_options=request_options)
        return _response.data

    def post_workflow_comfortsignature_deactivate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_comfortsignature_deactivate()
        """
        _response = self._raw_client.post_workflow_comfortsignature_deactivate(request_options=request_options)
        return _response.data

    def get_workflow_comfortsignature_user_id(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.get_workflow_comfortsignature_user_id()
        """
        _response = self._raw_client.get_workflow_comfortsignature_user_id(request_options=request_options)
        return _response.data

    def post_workflow_comfortsignature_user_id(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_comfortsignature_user_id()
        """
        _response = self._raw_client.post_workflow_comfortsignature_user_id(request_options=request_options)
        return _response.data

    def get_workflow_idp_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.get_workflow_idp_token()
        """
        _response = self._raw_client.get_workflow_idp_token(request_options=request_options)
        return _response.data

    def post_workflow_sign(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_sign()
        """
        _response = self._raw_client.post_workflow_sign(request_options=request_options)
        return _response.data

    def get_workflow_signature_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSignatureModeResponseEvent:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSignatureModeResponseEvent
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.get_workflow_signature_mode()
        """
        _response = self._raw_client.get_workflow_signature_mode(request_options=request_options)
        return _response.data

    def post_workflow_task(
        self, *, flowtype: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        flowtype : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_task()
        """
        _response = self._raw_client.post_workflow_task(flowtype=flowtype, request_options=request_options)
        return _response.data

    def post_workflow_test_prescription(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_test_prescription()
        """
        _response = self._raw_client.post_workflow_test_prescription(request_options=request_options)
        return _response.data

    def post_workflow_update(
        self,
        *,
        task_id: typing.Optional[str] = OMIT,
        access_code: typing.Optional[str] = OMIT,
        signed_bytes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        task_id : typing.Optional[str]

        access_code : typing.Optional[str]

        signed_bytes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.e_rezept_workflow_resource.post_workflow_update()
        """
        _response = self._raw_client.post_workflow_update(
            task_id=task_id, access_code=access_code, signed_bytes=signed_bytes, request_options=request_options
        )
        return _response.data


class AsyncERezeptWorkflowResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawERezeptWorkflowResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawERezeptWorkflowResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawERezeptWorkflowResourceClient
        """
        return self._raw_client

    async def post_workflow_abort(
        self,
        *,
        task_id: typing.Optional[str] = OMIT,
        access_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        task_id : typing.Optional[str]

        access_code : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_abort()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_abort(
            task_id=task_id, access_code=access_code, request_options=request_options
        )
        return _response.data

    async def post_workflow_batch_sign(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_batch_sign()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_batch_sign(request_options=request_options)
        return _response.data

    async def get_workflow_cards(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetCardsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCardsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.get_workflow_cards()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflow_cards(request_options=request_options)
        return _response.data

    async def post_workflow_comfortsignature_activate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_comfortsignature_activate()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_comfortsignature_activate(request_options=request_options)
        return _response.data

    async def post_workflow_comfortsignature_deactivate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_comfortsignature_deactivate()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_comfortsignature_deactivate(request_options=request_options)
        return _response.data

    async def get_workflow_comfortsignature_user_id(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.get_workflow_comfortsignature_user_id()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflow_comfortsignature_user_id(request_options=request_options)
        return _response.data

    async def post_workflow_comfortsignature_user_id(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_comfortsignature_user_id()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_comfortsignature_user_id(request_options=request_options)
        return _response.data

    async def get_workflow_idp_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.get_workflow_idp_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflow_idp_token(request_options=request_options)
        return _response.data

    async def post_workflow_sign(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_sign()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_sign(request_options=request_options)
        return _response.data

    async def get_workflow_signature_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSignatureModeResponseEvent:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSignatureModeResponseEvent
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.get_workflow_signature_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflow_signature_mode(request_options=request_options)
        return _response.data

    async def post_workflow_task(
        self, *, flowtype: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        flowtype : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_task()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_task(flowtype=flowtype, request_options=request_options)
        return _response.data

    async def post_workflow_test_prescription(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_test_prescription()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_test_prescription(request_options=request_options)
        return _response.data

    async def post_workflow_update(
        self,
        *,
        task_id: typing.Optional[str] = OMIT,
        access_code: typing.Optional[str] = OMIT,
        signed_bytes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        task_id : typing.Optional[str]

        access_code : typing.Optional[str]

        signed_bytes : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.e_rezept_workflow_resource.post_workflow_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_workflow_update(
            task_id=task_id, access_code=access_code, signed_bytes=signed_bytes, request_options=request_options
        )
        return _response.data
