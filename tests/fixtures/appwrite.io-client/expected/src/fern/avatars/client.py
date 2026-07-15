

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAvatarsClient, RawAvatarsClient


class AvatarsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAvatarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAvatarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAvatarsClient
        """
        return self._raw_client

    def get_browser(
        self,
        code: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user /account/sessions endpoint. Use width, height and quality arguments to change the output settings.

        Parameters
        ----------
        code : str
            Browser Code.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        quality : typing.Optional[int]
            Image quality. Pass an integer between 0 to 100. Defaults to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.get_browser(
            code="code",
        )
        """
        _response = self._raw_client.get_browser(
            code, width=width, height=height, quality=quality, request_options=request_options
        )
        return _response.data

    def get_credit_card(
        self,
        code: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

        Parameters
        ----------
        code : str
            Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        quality : typing.Optional[int]
            Image quality. Pass an integer between 0 to 100. Defaults to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.get_credit_card(
            code="code",
        )
        """
        _response = self._raw_client.get_credit_card(
            code, width=width, height=height, quality=quality, request_options=request_options
        )
        return _response.data

    def get_favicon(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL.

        Parameters
        ----------
        url : str
            Website URL which you want to fetch the favicon from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.get_favicon(
            url="url",
        )
        """
        _response = self._raw_client.get_favicon(url=url, request_options=request_options)
        return _response.data

    def get_flag(
        self,
        code: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings.

        Parameters
        ----------
        code : str
            Country Code. ISO Alpha-2 country code format.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        quality : typing.Optional[int]
            Image quality. Pass an integer between 0 to 100. Defaults to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.get_flag(
            code="code",
        )
        """
        _response = self._raw_client.get_flag(
            code, width=width, height=height, quality=quality, request_options=request_options
        )
        return _response.data

    def get_image(
        self,
        *,
        url: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

        Parameters
        ----------
        url : str
            Image URL which you want to crop.

        width : typing.Optional[int]
            Resize preview image width, Pass an integer between 0 to 2000.

        height : typing.Optional[int]
            Resize preview image height, Pass an integer between 0 to 2000.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.get_image(
            url="url",
        )
        """
        _response = self._raw_client.get_image(url=url, width=width, height=height, request_options=request_options)
        return _response.data

    def get_initials(
        self,
        *,
        name: typing.Optional[str] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        color: typing.Optional[str] = None,
        background: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.

        You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.

        Parameters
        ----------
        name : typing.Optional[str]
            Full Name. When empty, current user name or email will be used. Max length: 128 chars.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        color : typing.Optional[str]
            Changes text color. By default a random color will be picked and stay will persistent to the given name.

        background : typing.Optional[str]
            Changes background color. By default a random color will be picked and stay will persistent to the given name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.get_initials()
        """
        _response = self._raw_client.get_initials(
            name=name, width=width, height=height, color=color, background=background, request_options=request_options
        )
        return _response.data

    def avatars_get_qr(
        self,
        *,
        text: str,
        size: typing.Optional[int] = None,
        margin: typing.Optional[int] = None,
        download: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.

        Parameters
        ----------
        text : str
            Plain text to be converted to QR code image.

        size : typing.Optional[int]
            QR code size. Pass an integer between 0 to 1000. Defaults to 400.

        margin : typing.Optional[int]
            Margin from edge. Pass an integer between 0 to 10. Defaults to 1.

        download : typing.Optional[bool]
            Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.avatars.avatars_get_qr(
            text="text",
        )
        """
        _response = self._raw_client.avatars_get_qr(
            text=text, size=size, margin=margin, download=download, request_options=request_options
        )
        return _response.data


class AsyncAvatarsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAvatarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAvatarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAvatarsClient
        """
        return self._raw_client

    async def get_browser(
        self,
        code: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user /account/sessions endpoint. Use width, height and quality arguments to change the output settings.

        Parameters
        ----------
        code : str
            Browser Code.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        quality : typing.Optional[int]
            Image quality. Pass an integer between 0 to 100. Defaults to 100.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.get_browser(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_browser(
            code, width=width, height=height, quality=quality, request_options=request_options
        )
        return _response.data

    async def get_credit_card(
        self,
        code: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

        Parameters
        ----------
        code : str
            Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        quality : typing.Optional[int]
            Image quality. Pass an integer between 0 to 100. Defaults to 100.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.get_credit_card(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_credit_card(
            code, width=width, height=height, quality=quality, request_options=request_options
        )
        return _response.data

    async def get_favicon(self, *, url: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL.

        Parameters
        ----------
        url : str
            Website URL which you want to fetch the favicon from.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.get_favicon(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_favicon(url=url, request_options=request_options)
        return _response.data

    async def get_flag(
        self,
        code: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        quality: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings.

        Parameters
        ----------
        code : str
            Country Code. ISO Alpha-2 country code format.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        quality : typing.Optional[int]
            Image quality. Pass an integer between 0 to 100. Defaults to 100.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.get_flag(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flag(
            code, width=width, height=height, quality=quality, request_options=request_options
        )
        return _response.data

    async def get_image(
        self,
        *,
        url: str,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

        Parameters
        ----------
        url : str
            Image URL which you want to crop.

        width : typing.Optional[int]
            Resize preview image width, Pass an integer between 0 to 2000.

        height : typing.Optional[int]
            Resize preview image height, Pass an integer between 0 to 2000.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.get_image(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image(
            url=url, width=width, height=height, request_options=request_options
        )
        return _response.data

    async def get_initials(
        self,
        *,
        name: typing.Optional[str] = None,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        color: typing.Optional[str] = None,
        background: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.

        You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.

        Parameters
        ----------
        name : typing.Optional[str]
            Full Name. When empty, current user name or email will be used. Max length: 128 chars.

        width : typing.Optional[int]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.

        height : typing.Optional[int]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.

        color : typing.Optional[str]
            Changes text color. By default a random color will be picked and stay will persistent to the given name.

        background : typing.Optional[str]
            Changes background color. By default a random color will be picked and stay will persistent to the given name.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.get_initials()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_initials(
            name=name, width=width, height=height, color=color, background=background, request_options=request_options
        )
        return _response.data

    async def avatars_get_qr(
        self,
        *,
        text: str,
        size: typing.Optional[int] = None,
        margin: typing.Optional[int] = None,
        download: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.

        Parameters
        ----------
        text : str
            Plain text to be converted to QR code image.

        size : typing.Optional[int]
            QR code size. Pass an integer between 0 to 1000. Defaults to 400.

        margin : typing.Optional[int]
            Margin from edge. Pass an integer between 0 to 10. Defaults to 1.

        download : typing.Optional[bool]
            Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.

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
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.avatars.avatars_get_qr(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.avatars_get_qr(
            text=text, size=size, margin=margin, download=download, request_options=request_options
        )
        return _response.data
