

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.check_indexer_url_response import CheckIndexerUrlResponse
from ..types.empty_response import EmptyResponse
from ..types.init_response import InitResponse
from ..types.ldk_chain_sync import LdkChainSync
from ..types.network_info_response import NetworkInfoResponse
from ..types.node_info_response import NodeInfoResponse
from ..types.sign_message_response import SignMessageResponse
from .raw_client import AsyncRawOtherClient, RawOtherClient


OMIT = typing.cast(typing.Any, ...)


class OtherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOtherClient
        """
        return self._raw_client

    def backup_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Create a backup of the node's data

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.backup_the_node(
            backup_path="/path/where/to/save/the/backup/file",
            password="nodepassword",
        )
        """
        _response = self._raw_client.backup_the_node(
            backup_path=backup_path, password=password, request_options=request_options
        )
        return _response.data

    def change_the_password(
        self, *, old_password: str, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Change the node's password

        Parameters
        ----------
        old_password : str

        new_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.change_the_password(
            old_password="nodepassword",
            new_password="nodenewpassword",
        )
        """
        _response = self._raw_client.change_the_password(
            old_password=old_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    def check_an_indexer_url(
        self, *, indexer_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckIndexerUrlResponse:
        """
        Check the given indexer URL is valid

        Parameters
        ----------
        indexer_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckIndexerUrlResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.check_an_indexer_url(
            indexer_url="127.0.0.1:50001",
        )
        """
        _response = self._raw_client.check_an_indexer_url(indexer_url=indexer_url, request_options=request_options)
        return _response.data

    def check_a_proxy_endpoint(
        self, *, proxy_endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Check the given proxy endpoint is valid

        Parameters
        ----------
        proxy_endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.check_a_proxy_endpoint(
            proxy_endpoint="rpc://127.0.0.1:3000/json-rpc",
        )
        """
        _response = self._raw_client.check_a_proxy_endpoint(
            proxy_endpoint=proxy_endpoint, request_options=request_options
        )
        return _response.data

    def init_the_node(
        self,
        *,
        password: str,
        mnemonic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InitResponse:
        """
        Initialize a new node, optionally providing a mnemonic. If no mnemonic is provided a new one is generated. Note that a mnemonic alone is not sufficient to recover RGB state, which also requires client-side data.

        Parameters
        ----------
        password : str

        mnemonic : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InitResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.init_the_node(
            password="nodepassword",
        )
        """
        _response = self._raw_client.init_the_node(
            password=password, mnemonic=mnemonic, request_options=request_options
        )
        return _response.data

    def lock_the_node(self, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Lock an unlocked node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.lock_the_node()
        """
        _response = self._raw_client.lock_the_node(request_options=request_options)
        return _response.data

    def get_network_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> NetworkInfoResponse:
        """
        Get info on the Bitcoin network where the LN is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkInfoResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.get_network_info()
        """
        _response = self._raw_client.get_network_info(request_options=request_options)
        return _response.data

    def get_node_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> NodeInfoResponse:
        """
        Get the LN node's info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodeInfoResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.get_node_info()
        """
        _response = self._raw_client.get_node_info(request_options=request_options)
        return _response.data

    def restore_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Restore a node from a backup file

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.restore_the_node(
            backup_path="/path/to/the/backup/file",
            password="nodepassword",
        )
        """
        _response = self._raw_client.restore_the_node(
            backup_path=backup_path, password=password, request_options=request_options
        )
        return _response.data

    def revoke_a_token(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Revoke an authentication token

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.revoke_a_token(
            token="EnYKDBgDIggKBggGEgIYDRIkCAASICqCgqtFMIJ1eLCM3raDzqg9UqV-6nJWzGjjJG0S5IIUGkBpF-itmppHcdcSrSCiKklz9VZT4UmIND_0RFc32Imq3bLR_Y7GYaSpJo5lJfU1cA2BG_hy7P1UN4g5jKTKS88GIiIKIAUKXrrx0Ca-rMZa537VOFw2X8q_KVQ6OC4Z0ztro0sQ",
        )
        """
        _response = self._raw_client.revoke_a_token(token=token, request_options=request_options)
        return _response.data

    def send_an_onion_message(
        self,
        *,
        node_ids: typing.Sequence[str],
        tlv_type: int,
        data: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Send an onion message via the LN

        Parameters
        ----------
        node_ids : typing.Sequence[str]

        tlv_type : int

        data : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.send_an_onion_message(
            node_ids=[
                "03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d"
            ],
            tlv_type=77,
            data="message to send",
        )
        """
        _response = self._raw_client.send_an_onion_message(
            node_ids=node_ids, tlv_type=tlv_type, data=data, request_options=request_options
        )
        return _response.data

    def shutdown_the_node(self, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Gracefully shutdown the node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.shutdown_the_node()
        """
        _response = self._raw_client.shutdown_the_node(request_options=request_options)
        return _response.data

    def sign_a_message(
        self, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SignMessageResponse:
        """
        Sign the provided message

        Parameters
        ----------
        message : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignMessageResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.sign_a_message(
            message="message to sign",
        )
        """
        _response = self._raw_client.sign_a_message(message=message, request_options=request_options)
        return _response.data

    def unlock_the_node(
        self,
        *,
        password: str,
        ldk_chain_sync: LdkChainSync,
        indexer_url: str,
        announce_addresses: typing.Sequence[str],
        announce_alias: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Unlock a locked node

        Parameters
        ----------
        password : str

        ldk_chain_sync : LdkChainSync

        indexer_url : str

        announce_addresses : typing.Sequence[str]

        announce_alias : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, LdkChainSync_BlockSync, LdkChainSyncBlockSyncConfig

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.unlock_the_node(
            password="nodepassword",
            ldk_chain_sync=LdkChainSync_BlockSync(
                config=LdkChainSyncBlockSyncConfig(
                    bitcoind_rpc_username="user",
                    bitcoind_rpc_password="password",
                    bitcoind_rpc_host="localhost",
                    bitcoind_rpc_port=18443,
                ),
            ),
            indexer_url="127.0.0.1:50001",
            announce_addresses=["pub.addr.example.com:9735"],
        )
        """
        _response = self._raw_client.unlock_the_node(
            password=password,
            ldk_chain_sync=ldk_chain_sync,
            indexer_url=indexer_url,
            announce_addresses=announce_addresses,
            announce_alias=announce_alias,
            request_options=request_options,
        )
        return _response.data


class AsyncOtherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOtherClient
        """
        return self._raw_client

    async def backup_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Create a backup of the node's data

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.backup_the_node(
                backup_path="/path/where/to/save/the/backup/file",
                password="nodepassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.backup_the_node(
            backup_path=backup_path, password=password, request_options=request_options
        )
        return _response.data

    async def change_the_password(
        self, *, old_password: str, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Change the node's password

        Parameters
        ----------
        old_password : str

        new_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.change_the_password(
                old_password="nodepassword",
                new_password="nodenewpassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_the_password(
            old_password=old_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    async def check_an_indexer_url(
        self, *, indexer_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckIndexerUrlResponse:
        """
        Check the given indexer URL is valid

        Parameters
        ----------
        indexer_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckIndexerUrlResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.check_an_indexer_url(
                indexer_url="127.0.0.1:50001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_an_indexer_url(
            indexer_url=indexer_url, request_options=request_options
        )
        return _response.data

    async def check_a_proxy_endpoint(
        self, *, proxy_endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Check the given proxy endpoint is valid

        Parameters
        ----------
        proxy_endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.check_a_proxy_endpoint(
                proxy_endpoint="rpc://127.0.0.1:3000/json-rpc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_a_proxy_endpoint(
            proxy_endpoint=proxy_endpoint, request_options=request_options
        )
        return _response.data

    async def init_the_node(
        self,
        *,
        password: str,
        mnemonic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InitResponse:
        """
        Initialize a new node, optionally providing a mnemonic. If no mnemonic is provided a new one is generated. Note that a mnemonic alone is not sufficient to recover RGB state, which also requires client-side data.

        Parameters
        ----------
        password : str

        mnemonic : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InitResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.init_the_node(
                password="nodepassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.init_the_node(
            password=password, mnemonic=mnemonic, request_options=request_options
        )
        return _response.data

    async def lock_the_node(self, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Lock an unlocked node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.lock_the_node()


        asyncio.run(main())
        """
        _response = await self._raw_client.lock_the_node(request_options=request_options)
        return _response.data

    async def get_network_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> NetworkInfoResponse:
        """
        Get info on the Bitcoin network where the LN is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkInfoResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.get_network_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_network_info(request_options=request_options)
        return _response.data

    async def get_node_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> NodeInfoResponse:
        """
        Get the LN node's info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodeInfoResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.get_node_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_node_info(request_options=request_options)
        return _response.data

    async def restore_the_node(
        self, *, backup_path: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Restore a node from a backup file

        Parameters
        ----------
        backup_path : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.restore_the_node(
                backup_path="/path/to/the/backup/file",
                password="nodepassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_the_node(
            backup_path=backup_path, password=password, request_options=request_options
        )
        return _response.data

    async def revoke_a_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Revoke an authentication token

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.revoke_a_token(
                token="EnYKDBgDIggKBggGEgIYDRIkCAASICqCgqtFMIJ1eLCM3raDzqg9UqV-6nJWzGjjJG0S5IIUGkBpF-itmppHcdcSrSCiKklz9VZT4UmIND_0RFc32Imq3bLR_Y7GYaSpJo5lJfU1cA2BG_hy7P1UN4g5jKTKS88GIiIKIAUKXrrx0Ca-rMZa537VOFw2X8q_KVQ6OC4Z0ztro0sQ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_a_token(token=token, request_options=request_options)
        return _response.data

    async def send_an_onion_message(
        self,
        *,
        node_ids: typing.Sequence[str],
        tlv_type: int,
        data: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Send an onion message via the LN

        Parameters
        ----------
        node_ids : typing.Sequence[str]

        tlv_type : int

        data : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.send_an_onion_message(
                node_ids=[
                    "03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d"
                ],
                tlv_type=77,
                data="message to send",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_an_onion_message(
            node_ids=node_ids, tlv_type=tlv_type, data=data, request_options=request_options
        )
        return _response.data

    async def shutdown_the_node(self, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Gracefully shutdown the node

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.shutdown_the_node()


        asyncio.run(main())
        """
        _response = await self._raw_client.shutdown_the_node(request_options=request_options)
        return _response.data

    async def sign_a_message(
        self, *, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SignMessageResponse:
        """
        Sign the provided message

        Parameters
        ----------
        message : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignMessageResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.sign_a_message(
                message="message to sign",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_a_message(message=message, request_options=request_options)
        return _response.data

    async def unlock_the_node(
        self,
        *,
        password: str,
        ldk_chain_sync: LdkChainSync,
        indexer_url: str,
        announce_addresses: typing.Sequence[str],
        announce_alias: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Unlock a locked node

        Parameters
        ----------
        password : str

        ldk_chain_sync : LdkChainSync

        indexer_url : str

        announce_addresses : typing.Sequence[str]

        announce_alias : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            LdkChainSync_BlockSync,
            LdkChainSyncBlockSyncConfig,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.unlock_the_node(
                password="nodepassword",
                ldk_chain_sync=LdkChainSync_BlockSync(
                    config=LdkChainSyncBlockSyncConfig(
                        bitcoind_rpc_username="user",
                        bitcoind_rpc_password="password",
                        bitcoind_rpc_host="localhost",
                        bitcoind_rpc_port=18443,
                    ),
                ),
                indexer_url="127.0.0.1:50001",
                announce_addresses=["pub.addr.example.com:9735"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unlock_the_node(
            password=password,
            ldk_chain_sync=ldk_chain_sync,
            indexer_url=indexer_url,
            announce_addresses=announce_addresses,
            announce_alias=announce_alias,
            request_options=request_options,
        )
        return _response.data
