

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAmazonMusicClient, RawAmazonMusicClient


class AmazonMusicClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAmazonMusicClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAmazonMusicClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAmazonMusicClient
        """
        return self._raw_client

    def set_amazon_access_token(
        self, str: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setAmazonAccessToken:{str}:{str2}

        Parameters
        ----------
        str : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.amazon_music.set_amazon_access_token(
            str="str",
            str2="str2",
        )
        """
        _response = self._raw_client.set_amazon_access_token(str, str2, request_options=request_options)
        return _response.data

    def enable_amazon_atmos(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EnableAmazonAtmos:%d

        Parameters
        ----------
        n : int
            1 to enable, 0 to disable Amazon Atmos

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.amazon_music.enable_amazon_atmos(
            n=1,
        )
        """
        _response = self._raw_client.enable_amazon_atmos(n, request_options=request_options)
        return _response.data

    def enable_amazon_hd(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EnableAmazonHD:%d

        Parameters
        ----------
        n : int
            1 to enable, 0 to disable Amazon HD

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.amazon_music.enable_amazon_hd(
            n=1,
        )
        """
        _response = self._raw_client.enable_amazon_hd(n, request_options=request_options)
        return _response.data

    def get_amazon_hd(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=GetAmazonHD

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

        client = FernApi()
        client.amazon_music.get_amazon_hd()
        """
        _response = self._raw_client.get_amazon_hd(request_options=request_options)
        return _response.data

    def get_amazon_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getAmazonConfig

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

        client = FernApi()
        client.amazon_music.get_amazon_config()
        """
        _response = self._raw_client.get_amazon_config(request_options=request_options)
        return _response.data

    def set_amazon_music_params(
        self, str1: str, str2: str, str3: str, str4: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setAmazonMusicParams:code=%@:redirect_uri=%@:client_id=%@:code_verifier=%@
        Note: The parameters in the command should be replaced with actual values when making the request.

        Parameters
        ----------
        str1 : str
            The code parameter for Amazon Music

        str2 : str
            The redirect URI for Amazon Music

        str3 : str
            The client ID for Amazon Music

        str4 : str
            The code verifier for Amazon Music

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.amazon_music.set_amazon_music_params(
            str1="str1",
            str2="str2",
            str3="str3",
            str4="str4",
        )
        """
        _response = self._raw_client.set_amazon_music_params(str1, str2, str3, str4, request_options=request_options)
        return _response.data

    def set_prime_token(
        self, str1: str, str2: str, str3: str, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setPrimeToken:username=%@:token=%@:refreshToken=%@:expires_in=%ld

        Parameters
        ----------
        str1 : str
            The username for Amazon Prime

        str2 : str
            The access token for Amazon Prime

        str3 : str
            The refresh token for Amazon Prime

        n : int
            The expiration time in seconds for the access token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.amazon_music.set_prime_token(
            str1="str1",
            str2="str2",
            str3="str3",
            n=1,
        )
        """
        _response = self._raw_client.set_prime_token(str1, str2, str3, n, request_options=request_options)
        return _response.data


class AsyncAmazonMusicClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAmazonMusicClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAmazonMusicClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAmazonMusicClient
        """
        return self._raw_client

    async def set_amazon_access_token(
        self, str: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setAmazonAccessToken:{str}:{str2}

        Parameters
        ----------
        str : str
            Unknown

        str2 : str
            Unknown

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
            await client.amazon_music.set_amazon_access_token(
                str="str",
                str2="str2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_amazon_access_token(str, str2, request_options=request_options)
        return _response.data

    async def enable_amazon_atmos(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EnableAmazonAtmos:%d

        Parameters
        ----------
        n : int
            1 to enable, 0 to disable Amazon Atmos

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
            await client.amazon_music.enable_amazon_atmos(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_amazon_atmos(n, request_options=request_options)
        return _response.data

    async def enable_amazon_hd(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EnableAmazonHD:%d

        Parameters
        ----------
        n : int
            1 to enable, 0 to disable Amazon HD

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
            await client.amazon_music.enable_amazon_hd(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_amazon_hd(n, request_options=request_options)
        return _response.data

    async def get_amazon_hd(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=GetAmazonHD

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.amazon_music.get_amazon_hd()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_amazon_hd(request_options=request_options)
        return _response.data

    async def get_amazon_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getAmazonConfig

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.amazon_music.get_amazon_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_amazon_config(request_options=request_options)
        return _response.data

    async def set_amazon_music_params(
        self, str1: str, str2: str, str3: str, str4: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setAmazonMusicParams:code=%@:redirect_uri=%@:client_id=%@:code_verifier=%@
        Note: The parameters in the command should be replaced with actual values when making the request.

        Parameters
        ----------
        str1 : str
            The code parameter for Amazon Music

        str2 : str
            The redirect URI for Amazon Music

        str3 : str
            The client ID for Amazon Music

        str4 : str
            The code verifier for Amazon Music

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
            await client.amazon_music.set_amazon_music_params(
                str1="str1",
                str2="str2",
                str3="str3",
                str4="str4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_amazon_music_params(
            str1, str2, str3, str4, request_options=request_options
        )
        return _response.data

    async def set_prime_token(
        self, str1: str, str2: str, str3: str, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setPrimeToken:username=%@:token=%@:refreshToken=%@:expires_in=%ld

        Parameters
        ----------
        str1 : str
            The username for Amazon Prime

        str2 : str
            The access token for Amazon Prime

        str3 : str
            The refresh token for Amazon Prime

        n : int
            The expiration time in seconds for the access token

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
            await client.amazon_music.set_prime_token(
                str1="str1",
                str2="str2",
                str3="str3",
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_prime_token(str1, str2, str3, n, request_options=request_options)
        return _response.data
