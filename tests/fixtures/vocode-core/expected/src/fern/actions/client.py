

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action_page import ActionPage
from ..types.action_params_request import ActionParamsRequest
from ..types.action_response_model import ActionResponseModel
from ..types.action_update_params_request import ActionUpdateParamsRequest
from .raw_client import AsyncRawActionsClient, RawActionsClient


OMIT = typing.cast(typing.Any, ...)


class ActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActionsClient
        """
        return self._raw_client

    def get_action(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> ActionResponseModel:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResponseModel
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.actions.get_action(
            id="id",
        )
        """
        _response = self._raw_client.get_action(id=id, request_options=request_options)
        return _response.data

    def list_actions(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.actions.list_actions()
        """
        _response = self._raw_client.list_actions(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def create_action(
        self, *, request: ActionParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionResponseModel:
        """
        Parameters
        ----------
        request : ActionParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResponseModel
            Successful Response

        Examples
        --------
        from fern import (
            ActionParamsRequest_ActionAddToConference,
            AddToConferenceConfig,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.actions.create_action(
            request=ActionParamsRequest_ActionAddToConference(
                config=AddToConferenceConfig(
                    phone_number="phone_number",
                ),
            ),
        )
        """
        _response = self._raw_client.create_action(request=request, request_options=request_options)
        return _response.data

    def update_action(
        self, *, id: str, request: ActionUpdateParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionResponseModel:
        """
        Parameters
        ----------
        id : str

        request : ActionUpdateParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResponseModel
            Successful Response

        Examples
        --------
        from fern import ActionUpdateParamsRequest_ActionAddToConference, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.actions.update_action(
            id="id",
            request=ActionUpdateParamsRequest_ActionAddToConference(),
        )
        """
        _response = self._raw_client.update_action(id=id, request=request, request_options=request_options)
        return _response.data


class AsyncActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActionsClient
        """
        return self._raw_client

    async def get_action(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionResponseModel:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.get_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_action(id=id, request_options=request_options)
        return _response.data

    async def list_actions(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ActionPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.list_actions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_actions(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def create_action(
        self, *, request: ActionParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionResponseModel:
        """
        Parameters
        ----------
        request : ActionParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            ActionParamsRequest_ActionAddToConference,
            AddToConferenceConfig,
            AsyncFernApi,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.create_action(
                request=ActionParamsRequest_ActionAddToConference(
                    config=AddToConferenceConfig(
                        phone_number="phone_number",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_action(request=request, request_options=request_options)
        return _response.data

    async def update_action(
        self, *, id: str, request: ActionUpdateParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionResponseModel:
        """
        Parameters
        ----------
        id : str

        request : ActionUpdateParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import ActionUpdateParamsRequest_ActionAddToConference, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.actions.update_action(
                id="id",
                request=ActionUpdateParamsRequest_ActionAddToConference(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_action(id=id, request=request, request_options=request_options)
        return _response.data
