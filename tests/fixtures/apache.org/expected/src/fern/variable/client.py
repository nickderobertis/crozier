

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.variable import Variable
from ..types.variable_collection import VariableCollection
from .raw_client import AsyncRawVariableClient, RawVariableClient


OMIT = typing.cast(typing.Any, ...)


class VariableClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVariableClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVariableClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVariableClient
        """
        return self._raw_client

    def get_variables(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VariableCollection:
        """
        The collection does not contain data. To get data, you must get a single entity.

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VariableCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.variable.get_variables()
        """
        _response = self._raw_client.get_variables(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def post_variables(
        self,
        *,
        value: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Variable:
        """
        Parameters
        ----------
        value : typing.Optional[str]

        description : typing.Optional[str]
            The description of the variable.

            *New in version 2.4.0*

        key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variable
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.variable.post_variables()
        """
        _response = self._raw_client.post_variables(
            value=value, description=description, key=key, request_options=request_options
        )
        return _response.data

    def get_variable(self, variable_key: str, *, request_options: typing.Optional[RequestOptions] = None) -> Variable:
        """
        Get a variable by key.

        Parameters
        ----------
        variable_key : str
            The variable Key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variable
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.variable.get_variable(
            variable_key="variable_key",
        )
        """
        _response = self._raw_client.get_variable(variable_key, request_options=request_options)
        return _response.data

    def delete_variable(self, variable_key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        variable_key : str
            The variable Key.

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
        client.variable.delete_variable(
            variable_key="variable_key",
        )
        """
        _response = self._raw_client.delete_variable(variable_key, request_options=request_options)
        return _response.data

    def patch_variable(
        self,
        variable_key: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        value: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Variable:
        """
        Update a variable by key.

        Parameters
        ----------
        variable_key : str
            The variable Key.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        value : typing.Optional[str]

        description : typing.Optional[str]
            The description of the variable.

            *New in version 2.4.0*

        key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variable
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.variable.patch_variable(
            variable_key="variable_key",
        )
        """
        _response = self._raw_client.patch_variable(
            variable_key,
            update_mask=update_mask,
            value=value,
            description=description,
            key=key,
            request_options=request_options,
        )
        return _response.data


class AsyncVariableClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVariableClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVariableClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVariableClient
        """
        return self._raw_client

    async def get_variables(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VariableCollection:
        """
        The collection does not contain data. To get data, you must get a single entity.

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VariableCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.variable.get_variables()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_variables(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def post_variables(
        self,
        *,
        value: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Variable:
        """
        Parameters
        ----------
        value : typing.Optional[str]

        description : typing.Optional[str]
            The description of the variable.

            *New in version 2.4.0*

        key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variable
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.variable.post_variables()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_variables(
            value=value, description=description, key=key, request_options=request_options
        )
        return _response.data

    async def get_variable(
        self, variable_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Variable:
        """
        Get a variable by key.

        Parameters
        ----------
        variable_key : str
            The variable Key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variable
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.variable.get_variable(
                variable_key="variable_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_variable(variable_key, request_options=request_options)
        return _response.data

    async def delete_variable(
        self, variable_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        variable_key : str
            The variable Key.

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
            await client.variable.delete_variable(
                variable_key="variable_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_variable(variable_key, request_options=request_options)
        return _response.data

    async def patch_variable(
        self,
        variable_key: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        value: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Variable:
        """
        Update a variable by key.

        Parameters
        ----------
        variable_key : str
            The variable Key.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        value : typing.Optional[str]

        description : typing.Optional[str]
            The description of the variable.

            *New in version 2.4.0*

        key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Variable
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.variable.patch_variable(
                variable_key="variable_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_variable(
            variable_key,
            update_mask=update_mask,
            value=value,
            description=description,
            key=key,
            request_options=request_options,
        )
        return _response.data
