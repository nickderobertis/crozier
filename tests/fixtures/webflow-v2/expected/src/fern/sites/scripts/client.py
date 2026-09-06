

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawScriptsClient, RawScriptsClient
from .types.get_custom_code_scripts_response import GetCustomCodeScriptsResponse
from .types.list_custom_code_blocks_scripts_response import ListCustomCodeBlocksScriptsResponse
from .types.upsert_custom_code_scripts_request_scripts_item import UpsertCustomCodeScriptsRequestScriptsItem
from .types.upsert_custom_code_scripts_response import UpsertCustomCodeScriptsResponse


OMIT = typing.cast(typing.Any, ...)


class ScriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScriptsClient
        """
        return self._raw_client

    def get_custom_code(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomCodeScriptsResponse:
        """
        Get all scripts applied to a site by the App.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.scripts.get_custom_code(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get_custom_code(site_id, request_options=request_options)
        return _response.data

    def upsert_custom_code(
        self,
        site_id: str,
        *,
        scripts: typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertCustomCodeScriptsResponse:
        """
        Apply registered scripts to a site. If you have multiple scripts your App needs to apply or maintain on a site, ensure they are always included in the request body for this endpoint. To remove individual scripts, simply call this endpoint without the script in the request body.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        scripts : typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]]
            A list of scripts applied to a Site or a Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        from fern.sites.scripts import (
            UpsertCustomCodeScriptsRequestScriptsItem,
            UpsertCustomCodeScriptsRequestScriptsItemLocation,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.scripts.upsert_custom_code(
            site_id="580e63e98c9a982ac9b8b741",
            scripts=[
                UpsertCustomCodeScriptsRequestScriptsItem(
                    id="cms_slider",
                    location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                    version="1.0.0",
                    attributes={"my-attribute": "some-value"},
                ),
                UpsertCustomCodeScriptsRequestScriptsItem(
                    id="alert",
                    location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                    version="0.0.1",
                ),
            ],
        )
        """
        _response = self._raw_client.upsert_custom_code(site_id, scripts=scripts, request_options=request_options)
        return _response.data

    def delete_custom_code(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove all scripts from a site applied by the App. This endpoint will not remove scripts from the site's registered scripts.

        To remove individual scripts applied by the App, use the [Add/Update Custom Code](/data/reference/custom-code/custom-code-sites/upsert-custom-code) endpoint.

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

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
        client.sites.scripts.delete_custom_code(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.delete_custom_code(site_id, request_options=request_options)
        return _response.data

    def list_custom_code_blocks(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomCodeBlocksScriptsResponse:
        """
        Get a list of scripts that have been applied to a site and/or individual pages.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints.

          See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomCodeBlocksScriptsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.scripts.list_custom_code_blocks(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list_custom_code_blocks(
            site_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncScriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScriptsClient
        """
        return self._raw_client

    async def get_custom_code(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomCodeScriptsResponse:
        """
        Get all scripts applied to a site by the App.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.scripts.get_custom_code(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_custom_code(site_id, request_options=request_options)
        return _response.data

    async def upsert_custom_code(
        self,
        site_id: str,
        *,
        scripts: typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertCustomCodeScriptsResponse:
        """
        Apply registered scripts to a site. If you have multiple scripts your App needs to apply or maintain on a site, ensure they are always included in the request body for this endpoint. To remove individual scripts, simply call this endpoint without the script in the request body.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        scripts : typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]]
            A list of scripts applied to a Site or a Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.sites.scripts import (
            UpsertCustomCodeScriptsRequestScriptsItem,
            UpsertCustomCodeScriptsRequestScriptsItemLocation,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.scripts.upsert_custom_code(
                site_id="580e63e98c9a982ac9b8b741",
                scripts=[
                    UpsertCustomCodeScriptsRequestScriptsItem(
                        id="cms_slider",
                        location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                        version="1.0.0",
                        attributes={"my-attribute": "some-value"},
                    ),
                    UpsertCustomCodeScriptsRequestScriptsItem(
                        id="alert",
                        location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                        version="0.0.1",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_custom_code(site_id, scripts=scripts, request_options=request_options)
        return _response.data

    async def delete_custom_code(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove all scripts from a site applied by the App. This endpoint will not remove scripts from the site's registered scripts.

        To remove individual scripts applied by the App, use the [Add/Update Custom Code](/data/reference/custom-code/custom-code-sites/upsert-custom-code) endpoint.

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

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
            await client.sites.scripts.delete_custom_code(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_custom_code(site_id, request_options=request_options)
        return _response.data

    async def list_custom_code_blocks(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomCodeBlocksScriptsResponse:
        """
        Get a list of scripts that have been applied to a site and/or individual pages.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints.

          See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomCodeBlocksScriptsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.scripts.list_custom_code_blocks(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_custom_code_blocks(
            site_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data
