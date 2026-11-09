

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.task import Task
from ..types.token_info import TokenInfo
from .raw_client import AsyncRawTokensClient, RawTokensClient
from .types.get_tokens_response_item import GetTokensResponseItem


OMIT = typing.cast(typing.Any, ...)


class TokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokensClient
        """
        return self._raw_client

    def return_a_list_of_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetTokensResponseItem]:
        """
        Returns all tokens. For the Standard Registry role it returns only the list of tokens, for other users it also returns token balances as well as the KYC, Freeze, and Association statuses. Not allowed for the Auditor role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetTokensResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.return_a_list_of_tokens()
        """
        _response = self._raw_client.return_a_list_of_tokens(request_options=request_options)
        return _response.data

    def creates_a_new_token(
        self,
        *,
        change_supply: bool,
        decimals: str,
        enable_admin: bool,
        enable_freeze: bool,
        enable_kyc: bool,
        enable_wipe: bool,
        initial_supply: str,
        token_name: str,
        token_symbol: str,
        token_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Creates a new token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        change_supply : bool

        decimals : str

        enable_admin : bool

        enable_freeze : bool

        enable_kyc : bool

        enable_wipe : bool

        initial_supply : str

        token_name : str

        token_symbol : str

        token_type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.creates_a_new_token(
            change_supply=True,
            decimals="decimals",
            enable_admin=True,
            enable_freeze=True,
            enable_kyc=True,
            enable_wipe=True,
            initial_supply="initialSupply",
            token_name="tokenName",
            token_symbol="tokenSymbol",
            token_type="tokenType",
        )
        """
        _response = self._raw_client.creates_a_new_token(
            change_supply=change_supply,
            decimals=decimals,
            enable_admin=enable_admin,
            enable_freeze=enable_freeze,
            enable_kyc=enable_kyc,
            enable_wipe=enable_wipe,
            initial_supply=initial_supply,
            token_name=token_name,
            token_symbol=token_symbol,
            token_type=token_type,
            request_options=request_options,
        )
        return _response.data

    def tokens_api_delete_token_async(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        token_id : str
            Token identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.tokens_api_delete_token_async(
            token_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.tokens_api_delete_token_async(token_id, request_options=request_options)
        return _response.data

    def associates_the_user_with_the_provided_hedera_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Associates the user with the provided Hedera token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.associates_the_user_with_the_provided_hedera_token(
            token_id="tokenId",
        )
        """
        _response = self._raw_client.associates_the_user_with_the_provided_hedera_token(
            token_id, request_options=request_options
        )
        return _response.data

    def associate_the_user_with_the_provided_hedera_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disassociates the user with the provided Hedera token. Only users with the Installer role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.associate_the_user_with_the_provided_hedera_token(
            token_id="tokenId",
        )
        """
        _response = self._raw_client.associate_the_user_with_the_provided_hedera_token(
            token_id, request_options=request_options
        )
        return _response.data

    def disassociates_the_user_with_the_provided_hedera_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Disassociates the user with the provided Hedera token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.disassociates_the_user_with_the_provided_hedera_token(
            token_id="tokenId",
        )
        """
        _response = self._raw_client.disassociates_the_user_with_the_provided_hedera_token(
            token_id, request_options=request_options
        )
        return _response.data

    def sets_the_kyc_flag_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Sets the KYC flag for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.sets_the_kyc_flag_for_the_user(
            token_id="tokenId",
            username="username",
        )
        """
        _response = self._raw_client.sets_the_kyc_flag_for_the_user(token_id, username, request_options=request_options)
        return _response.data

    def unsets_the_kyc_flag_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Unsets the KYC flag for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.unsets_the_kyc_flag_for_the_user(
            token_id="tokenId",
            username="username",
        )
        """
        _response = self._raw_client.unsets_the_kyc_flag_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    def freeze_transfers_of_the_specified_token_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Freezes transfers of the specified token for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.freeze_transfers_of_the_specified_token_for_the_user(
            token_id="tokenId",
            username="username",
        )
        """
        _response = self._raw_client.freeze_transfers_of_the_specified_token_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    def unfreezes_transfers_of_the_specified_token_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Unfreezes transfers of the specified token for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.unfreezes_transfers_of_the_specified_token_for_the_user(
            token_id="tokenId",
            username="username",
        )
        """
        _response = self._raw_client.unfreezes_transfers_of_the_specified_token_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    def get_tokens_token_id_username_info(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenInfo:
        """
        Returns user information for the selected token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenInfo
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.get_tokens_token_id_username_info(
            token_id="tokenId",
            username="username",
        )
        """
        _response = self._raw_client.get_tokens_token_id_username_info(
            token_id, username, request_options=request_options
        )
        return _response.data

    def tokens_api_get_token_serials(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[float]:
        """
        Returns token serials of current user.

        Parameters
        ----------
        token_id : str
            Token identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Token serials.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.tokens_api_get_token_serials(
            token_id="0.0.1",
        )
        """
        _response = self._raw_client.tokens_api_get_token_serials(token_id, request_options=request_options)
        return _response.data


class AsyncTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokensClient
        """
        return self._raw_client

    async def return_a_list_of_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetTokensResponseItem]:
        """
        Returns all tokens. For the Standard Registry role it returns only the list of tokens, for other users it also returns token balances as well as the KYC, Freeze, and Association statuses. Not allowed for the Auditor role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetTokensResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.return_a_list_of_tokens()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_tokens(request_options=request_options)
        return _response.data

    async def creates_a_new_token(
        self,
        *,
        change_supply: bool,
        decimals: str,
        enable_admin: bool,
        enable_freeze: bool,
        enable_kyc: bool,
        enable_wipe: bool,
        initial_supply: str,
        token_name: str,
        token_symbol: str,
        token_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Creates a new token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        change_supply : bool

        decimals : str

        enable_admin : bool

        enable_freeze : bool

        enable_kyc : bool

        enable_wipe : bool

        initial_supply : str

        token_name : str

        token_symbol : str

        token_type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.creates_a_new_token(
                change_supply=True,
                decimals="decimals",
                enable_admin=True,
                enable_freeze=True,
                enable_kyc=True,
                enable_wipe=True,
                initial_supply="initialSupply",
                token_name="tokenName",
                token_symbol="tokenSymbol",
                token_type="tokenType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_token(
            change_supply=change_supply,
            decimals=decimals,
            enable_admin=enable_admin,
            enable_freeze=enable_freeze,
            enable_kyc=enable_kyc,
            enable_wipe=enable_wipe,
            initial_supply=initial_supply,
            token_name=token_name,
            token_symbol=token_symbol,
            token_type=token_type,
            request_options=request_options,
        )
        return _response.data

    async def tokens_api_delete_token_async(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        token_id : str
            Token identifier

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.tokens_api_delete_token_async(
                token_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_api_delete_token_async(token_id, request_options=request_options)
        return _response.data

    async def associates_the_user_with_the_provided_hedera_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Associates the user with the provided Hedera token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.associates_the_user_with_the_provided_hedera_token(
                token_id="tokenId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.associates_the_user_with_the_provided_hedera_token(
            token_id, request_options=request_options
        )
        return _response.data

    async def associate_the_user_with_the_provided_hedera_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disassociates the user with the provided Hedera token. Only users with the Installer role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.associate_the_user_with_the_provided_hedera_token(
                token_id="tokenId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.associate_the_user_with_the_provided_hedera_token(
            token_id, request_options=request_options
        )
        return _response.data

    async def disassociates_the_user_with_the_provided_hedera_token(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Disassociates the user with the provided Hedera token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.disassociates_the_user_with_the_provided_hedera_token(
                token_id="tokenId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disassociates_the_user_with_the_provided_hedera_token(
            token_id, request_options=request_options
        )
        return _response.data

    async def sets_the_kyc_flag_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Sets the KYC flag for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.sets_the_kyc_flag_for_the_user(
                token_id="tokenId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sets_the_kyc_flag_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    async def unsets_the_kyc_flag_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Unsets the KYC flag for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.unsets_the_kyc_flag_for_the_user(
                token_id="tokenId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsets_the_kyc_flag_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    async def freeze_transfers_of_the_specified_token_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Freezes transfers of the specified token for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.freeze_transfers_of_the_specified_token_for_the_user(
                token_id="tokenId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.freeze_transfers_of_the_specified_token_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    async def unfreezes_transfers_of_the_specified_token_for_the_user(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Unfreezes transfers of the specified token for the user. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.unfreezes_transfers_of_the_specified_token_for_the_user(
                token_id="tokenId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfreezes_transfers_of_the_specified_token_for_the_user(
            token_id, username, request_options=request_options
        )
        return _response.data

    async def get_tokens_token_id_username_info(
        self, token_id: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenInfo:
        """
        Returns user information for the selected token. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        token_id : str
            Token ID.

        username : str
            Username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenInfo
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.get_tokens_token_id_username_info(
                token_id="tokenId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tokens_token_id_username_info(
            token_id, username, request_options=request_options
        )
        return _response.data

    async def tokens_api_get_token_serials(
        self, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[float]:
        """
        Returns token serials of current user.

        Parameters
        ----------
        token_id : str
            Token identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Token serials.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.tokens_api_get_token_serials(
                token_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tokens_api_get_token_serials(token_id, request_options=request_options)
        return _response.data
