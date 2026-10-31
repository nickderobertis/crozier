

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAlexaClient, RawAlexaClient


class AlexaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlexaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlexaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlexaClient
        """
        return self._raw_client

    def enable_beta_id(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaEnableBetaId:{n}

        Parameters
        ----------
        n : int
            The beta ID to enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alexa.enable_beta_id(
            n=1,
        )
        """
        _response = self._raw_client.enable_beta_id(n, request_options=request_options)
        return _response.data

    def get_alexa_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getAlexaProfile

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
        client.alexa.get_alexa_profile()
        """
        _response = self._raw_client.get_alexa_profile(request_options=request_options)
        return _response.data

    def log_out(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaLogOut

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
        client.alexa.log_out()
        """
        _response = self._raw_client.log_out(request_options=request_options)
        return _response.data

    def get_alexa_country(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getAlexaCountry

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
        client.alexa.get_alexa_country()
        """
        _response = self._raw_client.get_alexa_country(request_options=request_options)
        return _response.data

    def language_list_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaLanguageListGet

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
        client.alexa.language_list_get()
        """
        _response = self._raw_client.language_list_get(request_options=request_options)
        return _response.data

    def get_language(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaGetLanguage

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
        client.alexa.get_language()
        """
        _response = self._raw_client.get_language(request_options=request_options)
        return _response.data

    def set_alexa_country(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setAlexaCountry:{str}

        Parameters
        ----------
        str : str
            Country code to set for Alexa

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alexa.set_alexa_country(
            str="str",
        )
        """
        _response = self._raw_client.set_alexa_country(str, request_options=request_options)
        return _response.data

    def set_language(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaSetLanguage:{str}

        Parameters
        ----------
        str : str
            Language code to set for Alexa

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alexa.set_language(
            str="str",
        )
        """
        _response = self._raw_client.set_language(str, request_options=request_options)
        return _response.data

    def get_avs_dev_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

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
        client.alexa.get_avs_dev_info()
        """
        _response = self._raw_client.get_avs_dev_info(request_options=request_options)
        return _response.data

    def get_avs_music_hd_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

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
        client.alexa.get_avs_music_hd_enable()
        """
        _response = self._raw_client.get_avs_music_hd_enable(request_options=request_options)
        return _response.data

    def set_avs_music_hd_enable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
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
        client.alexa.set_avs_music_hd_enable(
            str="str",
        )
        """
        _response = self._raw_client.set_avs_music_hd_enable(str, request_options=request_options)
        return _response.data


class AsyncAlexaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlexaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlexaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlexaClient
        """
        return self._raw_client

    async def enable_beta_id(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaEnableBetaId:{n}

        Parameters
        ----------
        n : int
            The beta ID to enable

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
            await client.alexa.enable_beta_id(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_beta_id(n, request_options=request_options)
        return _response.data

    async def get_alexa_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getAlexaProfile

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
            await client.alexa.get_alexa_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alexa_profile(request_options=request_options)
        return _response.data

    async def log_out(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaLogOut

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
            await client.alexa.log_out()


        asyncio.run(main())
        """
        _response = await self._raw_client.log_out(request_options=request_options)
        return _response.data

    async def get_alexa_country(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getAlexaCountry

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
            await client.alexa.get_alexa_country()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alexa_country(request_options=request_options)
        return _response.data

    async def language_list_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaLanguageListGet

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
            await client.alexa.language_list_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.language_list_get(request_options=request_options)
        return _response.data

    async def get_language(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaGetLanguage

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
            await client.alexa.get_language()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_language(request_options=request_options)
        return _response.data

    async def set_alexa_country(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=setAlexaCountry:{str}

        Parameters
        ----------
        str : str
            Country code to set for Alexa

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
            await client.alexa.set_alexa_country(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_alexa_country(str, request_options=request_options)
        return _response.data

    async def set_language(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=alexaSetLanguage:{str}

        Parameters
        ----------
        str : str
            Language code to set for Alexa

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
            await client.alexa.set_language(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_language(str, request_options=request_options)
        return _response.data

    async def get_avs_dev_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

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
            await client.alexa.get_avs_dev_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_avs_dev_info(request_options=request_options)
        return _response.data

    async def get_avs_music_hd_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

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
            await client.alexa.get_avs_music_hd_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_avs_music_hd_enable(request_options=request_options)
        return _response.data

    async def set_avs_music_hd_enable(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
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
            await client.alexa.set_avs_music_hd_enable(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_avs_music_hd_enable(str, request_options=request_options)
        return _response.data
