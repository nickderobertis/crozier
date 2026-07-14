

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.continent_list import ContinentList
from ..types.country_list import CountryList
from ..types.currency_list import CurrencyList
from ..types.language_list import LanguageList
from ..types.locale import Locale
from ..types.phone_list import PhoneList
from .raw_client import AsyncRawLocaleClient, RawLocaleClient


class LocaleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocaleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocaleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocaleClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> Locale:
        """
        Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.

        ([IP Geolocation by DB-IP](https://db-ip.com))

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Locale
            Locale

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def get_continents(self, *, request_options: typing.Optional[RequestOptions] = None) -> ContinentList:
        """
        List of all continents. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContinentList
            Continents List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.get_continents()
        """
        _response = self._raw_client.get_continents(request_options=request_options)
        return _response.data

    def get_countries(self, *, request_options: typing.Optional[RequestOptions] = None) -> CountryList:
        """
        List of all countries. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CountryList
            Countries List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.get_countries()
        """
        _response = self._raw_client.get_countries(request_options=request_options)
        return _response.data

    def locale_get_countries_eu(self, *, request_options: typing.Optional[RequestOptions] = None) -> CountryList:
        """
        List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CountryList
            Countries List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.locale_get_countries_eu()
        """
        _response = self._raw_client.locale_get_countries_eu(request_options=request_options)
        return _response.data

    def get_countries_phones(self, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneList:
        """
        List of all countries phone codes. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneList
            Phones List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.get_countries_phones()
        """
        _response = self._raw_client.get_countries_phones(request_options=request_options)
        return _response.data

    def get_currencies(self, *, request_options: typing.Optional[RequestOptions] = None) -> CurrencyList:
        """
        List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyList
            Currencies List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.get_currencies()
        """
        _response = self._raw_client.get_currencies(request_options=request_options)
        return _response.data

    def get_languages(self, *, request_options: typing.Optional[RequestOptions] = None) -> LanguageList:
        """
        List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguageList
            Languages List

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )
        client.locale.get_languages()
        """
        _response = self._raw_client.get_languages(request_options=request_options)
        return _response.data


class AsyncLocaleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocaleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocaleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocaleClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> Locale:
        """
        Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.

        ([IP Geolocation by DB-IP](https://db-ip.com))

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Locale
            Locale

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def get_continents(self, *, request_options: typing.Optional[RequestOptions] = None) -> ContinentList:
        """
        List of all continents. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContinentList
            Continents List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.get_continents()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_continents(request_options=request_options)
        return _response.data

    async def get_countries(self, *, request_options: typing.Optional[RequestOptions] = None) -> CountryList:
        """
        List of all countries. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CountryList
            Countries List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.get_countries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_countries(request_options=request_options)
        return _response.data

    async def locale_get_countries_eu(self, *, request_options: typing.Optional[RequestOptions] = None) -> CountryList:
        """
        List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CountryList
            Countries List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.locale_get_countries_eu()


        asyncio.run(main())
        """
        _response = await self._raw_client.locale_get_countries_eu(request_options=request_options)
        return _response.data

    async def get_countries_phones(self, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneList:
        """
        List of all countries phone codes. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneList
            Phones List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.get_countries_phones()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_countries_phones(request_options=request_options)
        return _response.data

    async def get_currencies(self, *, request_options: typing.Optional[RequestOptions] = None) -> CurrencyList:
        """
        List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyList
            Currencies List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.get_currencies()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_currencies(request_options=request_options)
        return _response.data

    async def get_languages(self, *, request_options: typing.Optional[RequestOptions] = None) -> LanguageList:
        """
        List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguageList
            Languages List

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            appwrite_key="YOUR_APPWRITE_KEY",
            appwrite_locale="YOUR_APPWRITE_LOCALE",
            appwrite_project="YOUR_APPWRITE_PROJECT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.locale.get_languages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_languages(request_options=request_options)
        return _response.data
