

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_pkg_filter import AppPkgFilter
from ..types.app_pkg_info import AppPkgInfo
from ..types.app_pkg_info_modifications import AppPkgInfoModifications
from ..types.app_pkg_info_modifications_operation_state import AppPkgInfoModificationsOperationState
from ..types.app_pkg_subscription_info import AppPkgSubscriptionInfo
from ..types.app_pkg_subscription_link_list import AppPkgSubscriptionLinkList
from ..types.callback_uri import CallbackUri
from ..types.checksum import Checksum
from ..types.key_value_pairs import KeyValuePairs
from ..types.subsctiption_type_app_pkg import SubsctiptionTypeAppPkg
from ..types.uri import Uri
from .raw_client import AsyncRawAppPkgmClient, RawAppPkgmClient


OMIT = typing.cast(typing.Any, ...)


class AppPkgmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppPkgmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppPkgmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppPkgmClient
        """
        return self._raw_client

    def app_packages_get(
        self,
        *,
        filter: typing.Optional[str] = None,
        all_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        exclude_fields: typing.Optional[str] = None,
        exclude_default: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AppPkgInfo]:
        """
        queries information relating to on-boarded application packages in the MEO

        Parameters
        ----------
        filter : typing.Optional[str]
            Attribute-based filtering parameters according to ETSI GS MEC 009

        all_fields : typing.Optional[str]
            Include all complex attributes in the response.

        fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be included into the response

        exclude_fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be excluded from the response.

        exclude_default : typing.Optional[str]
            Indicates to exclude the following complex attributes of AppPkgInfo from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AppPkgInfo]
            Contains a representation of the application package resource

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_packages_get()
        """
        _response = self._raw_client.app_packages_get(
            filter=filter,
            all_fields=all_fields,
            fields=fields,
            exclude_fields=exclude_fields,
            exclude_default=exclude_default,
            request_options=request_options,
        )
        return _response.data

    def app_packages_post(
        self,
        *,
        app_pkg_name: str,
        app_pkg_path: Uri,
        app_pkg_version: str,
        checksum: Checksum,
        app_provider: typing.Optional[str] = OMIT,
        user_defined_data: typing.Optional[KeyValuePairs] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AppPkgInfo]:
        """
        Create a resource for on-boarding an application package to a MEO

        Parameters
        ----------
        app_pkg_name : str
            Name of the application package to be onboarded.

        app_pkg_path : Uri

        app_pkg_version : str
            Version of the application package to be onboarded.
            The appPkgName with appPkgVersion can be used to uniquely identify the application package.

        checksum : Checksum

        app_provider : typing.Optional[str]
            The provider's name of the application package to be onboarded.

        user_defined_data : typing.Optional[KeyValuePairs]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AppPkgInfo]
            Successful response for resource creation

        Examples
        --------
        from fern import Checksum, FernApi

        client = FernApi()
        client.app_pkgm.app_packages_post(
            app_pkg_name="appPkgName",
            app_pkg_path="appPkgPath",
            app_pkg_version="appPkgVersion",
            checksum=Checksum(
                algorithm="algorithm",
                hash="hash",
            ),
        )
        """
        _response = self._raw_client.app_packages_post(
            app_pkg_name=app_pkg_name,
            app_pkg_path=app_pkg_path,
            app_pkg_version=app_pkg_version,
            checksum=checksum,
            app_provider=app_provider,
            user_defined_data=user_defined_data,
            request_options=request_options,
        )
        return _response.data

    def app_package_get(
        self, app_pkg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppPkgInfo:
        """
        Queries the information related to individual application package resources

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an individual application package resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgInfo
            Contains a representation of the application package resource

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_package_get(
            app_pkg_id="appPkgId",
        )
        """
        _response = self._raw_client.app_package_get(app_pkg_id, request_options=request_options)
        return _response.data

    def app_package_delete(self, app_pkg_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an individual application package resources

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an individual application package resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_package_delete(
            app_pkg_id="appPkgId",
        )
        """
        _response = self._raw_client.app_package_delete(app_pkg_id, request_options=request_options)
        return _response.data

    def app_package_patch(
        self,
        app_pkg_id: str,
        *,
        operation_state: AppPkgInfoModificationsOperationState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppPkgInfoModifications:
        """
        Updates the operational state of an individual application package resources

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an individual application package resource

        operation_state : AppPkgInfoModificationsOperationState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgInfoModifications
            Shows that the operation has been completed successfully

        Examples
        --------
        from fern import AppPkgInfoModificationsOperationState, FernApi

        client = FernApi()
        client.app_pkgm.app_package_patch(
            app_pkg_id="appPkgId",
            operation_state=AppPkgInfoModificationsOperationState.DISABLED,
        )
        """
        _response = self._raw_client.app_package_patch(
            app_pkg_id, operation_state=operation_state, request_options=request_options
        )
        return _response.data

    def app_pkg_id_get(
        self,
        app_pkg_id: str,
        *,
        filter: typing.Optional[str] = None,
        all_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        exclude_fields: typing.Optional[str] = None,
        exclude_default: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Reads the content of the AppD of on-boarded individual application package resources.

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an on-boarded individual application package

        filter : typing.Optional[str]
            Attribute-based filtering parameters according to ETSI GS MEC 009

        all_fields : typing.Optional[str]
            Include all complex attributes in the response.

        fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be included into the response

        exclude_fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be excluded from the response.

        exclude_default : typing.Optional[str]
            Indicates to exclude the following complex attributes of AppPkgInfo from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Content of the AppD is returned.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_pkg_id_get(
            app_pkg_id="appPkgId",
        )
        """
        _response = self._raw_client.app_pkg_id_get(
            app_pkg_id,
            filter=filter,
            all_fields=all_fields,
            fields=fields,
            exclude_fields=exclude_fields,
            exclude_default=exclude_default,
            request_options=request_options,
        )
        return _response.data

    def app_pkg_get(self, app_pkg_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Fetch the onboarded application package content identified by appPkgId or appDId.

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an on-boarded individual application package

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_pkg_get(
            app_pkg_id="appPkgId",
        )
        """
        _response = self._raw_client.app_pkg_get(app_pkg_id, request_options=request_options)
        return _response.data

    def app_pkg_put(
        self,
        app_pkg_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Uploads the content of application package.

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an on-boarded individual application package

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.app_pkg_put(app_pkg_id, request=request, request_options=request_options)
        return _response.data

    def app_dget(
        self,
        app_d_id: str,
        *,
        filter: typing.Optional[str] = None,
        all_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        exclude_fields: typing.Optional[str] = None,
        exclude_default: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Reads the content of the AppD of on-boarded individual application package resources.

        Parameters
        ----------
        app_d_id : str
            Identifier of an application descriptor

        filter : typing.Optional[str]
            Attribute-based filtering parameters according to ETSI GS MEC 009

        all_fields : typing.Optional[str]
            Include all complex attributes in the response.

        fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be included into the response

        exclude_fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be excluded from the response.

        exclude_default : typing.Optional[str]
            Indicates to exclude the following complex attributes of AppPkgInfo from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Content of the AppD is returned.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_dget(
            app_d_id="appDId",
        )
        """
        _response = self._raw_client.app_dget(
            app_d_id,
            filter=filter,
            all_fields=all_fields,
            fields=fields,
            exclude_fields=exclude_fields,
            exclude_default=exclude_default,
            request_options=request_options,
        )
        return _response.data

    def app_d_id_get(self, app_d_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Fetch the onboarded application package content identified by appPkgId or appDId.

        Parameters
        ----------
        app_d_id : str
            Identifier of an application descriptor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.app_d_id_get(
            app_d_id="appDId",
        )
        """
        _response = self._raw_client.app_d_id_get(app_d_id, request_options=request_options)
        return _response.data

    def app_d_id_put(
        self,
        app_d_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Uploads the content of application package.

        Parameters
        ----------
        app_d_id : str
            Identifier of an application descriptor

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.app_d_id_put(app_d_id, request=request, request_options=request_options)
        return _response.data

    def subscriptions_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppPkgSubscriptionLinkList:
        """
        used to retrieve the information of subscriptions to individual application package resource in MEO package

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgSubscriptionLinkList
            List of zero or more subscriptions

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.subscriptions_get()
        """
        _response = self._raw_client.subscriptions_get(request_options=request_options)
        return _response.data

    def subscriptions_post(
        self,
        *,
        callback_uri: CallbackUri,
        subsctiption_type: SubsctiptionTypeAppPkg,
        app_pkg_filter: typing.Optional[typing.Sequence[AppPkgFilter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppPkgSubscriptionInfo:
        """
        Subscribe to notifications about on-boarding an application package

        Parameters
        ----------
        callback_uri : CallbackUri

        subsctiption_type : SubsctiptionTypeAppPkg

        app_pkg_filter : typing.Optional[typing.Sequence[AppPkgFilter]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgSubscriptionInfo
            Successful response for created subscription

        Examples
        --------
        from fern import FernApi, SubsctiptionTypeAppPkg

        client = FernApi()
        client.app_pkgm.subscriptions_post(
            callback_uri="callbackUri",
            subsctiption_type=SubsctiptionTypeAppPkg.APP_PACKAGE_ON_BOARDING,
        )
        """
        _response = self._raw_client.subscriptions_post(
            callback_uri=callback_uri,
            subsctiption_type=subsctiption_type,
            app_pkg_filter=app_pkg_filter,
            request_options=request_options,
        )
        return _response.data

    def individual_subscription_get(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppPkgSubscriptionInfo:
        """
        Used to represent an individual subscription to notifications about application package changes.

        Parameters
        ----------
        subscription_id : str
            Identifier of an individual subscription to notifications about application package changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgSubscriptionInfo
            Representation of the resource.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.individual_subscription_get(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.individual_subscription_get(subscription_id, request_options=request_options)
        return _response.data

    def individual_subscription_delete(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the individual subscription to notifications about application package changes in MEO.

        Parameters
        ----------
        subscription_id : str
            Identifier of an individual subscription to notifications about application package changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app_pkgm.individual_subscription_delete(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.individual_subscription_delete(subscription_id, request_options=request_options)
        return _response.data


class AsyncAppPkgmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppPkgmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppPkgmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppPkgmClient
        """
        return self._raw_client

    async def app_packages_get(
        self,
        *,
        filter: typing.Optional[str] = None,
        all_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        exclude_fields: typing.Optional[str] = None,
        exclude_default: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AppPkgInfo]:
        """
        queries information relating to on-boarded application packages in the MEO

        Parameters
        ----------
        filter : typing.Optional[str]
            Attribute-based filtering parameters according to ETSI GS MEC 009

        all_fields : typing.Optional[str]
            Include all complex attributes in the response.

        fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be included into the response

        exclude_fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be excluded from the response.

        exclude_default : typing.Optional[str]
            Indicates to exclude the following complex attributes of AppPkgInfo from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AppPkgInfo]
            Contains a representation of the application package resource

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.app_packages_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.app_packages_get(
            filter=filter,
            all_fields=all_fields,
            fields=fields,
            exclude_fields=exclude_fields,
            exclude_default=exclude_default,
            request_options=request_options,
        )
        return _response.data

    async def app_packages_post(
        self,
        *,
        app_pkg_name: str,
        app_pkg_path: Uri,
        app_pkg_version: str,
        checksum: Checksum,
        app_provider: typing.Optional[str] = OMIT,
        user_defined_data: typing.Optional[KeyValuePairs] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AppPkgInfo]:
        """
        Create a resource for on-boarding an application package to a MEO

        Parameters
        ----------
        app_pkg_name : str
            Name of the application package to be onboarded.

        app_pkg_path : Uri

        app_pkg_version : str
            Version of the application package to be onboarded.
            The appPkgName with appPkgVersion can be used to uniquely identify the application package.

        checksum : Checksum

        app_provider : typing.Optional[str]
            The provider's name of the application package to be onboarded.

        user_defined_data : typing.Optional[KeyValuePairs]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AppPkgInfo]
            Successful response for resource creation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Checksum

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.app_packages_post(
                app_pkg_name="appPkgName",
                app_pkg_path="appPkgPath",
                app_pkg_version="appPkgVersion",
                checksum=Checksum(
                    algorithm="algorithm",
                    hash="hash",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_packages_post(
            app_pkg_name=app_pkg_name,
            app_pkg_path=app_pkg_path,
            app_pkg_version=app_pkg_version,
            checksum=checksum,
            app_provider=app_provider,
            user_defined_data=user_defined_data,
            request_options=request_options,
        )
        return _response.data

    async def app_package_get(
        self, app_pkg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppPkgInfo:
        """
        Queries the information related to individual application package resources

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an individual application package resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgInfo
            Contains a representation of the application package resource

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.app_package_get(
                app_pkg_id="appPkgId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_package_get(app_pkg_id, request_options=request_options)
        return _response.data

    async def app_package_delete(
        self, app_pkg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an individual application package resources

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an individual application package resource

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
            await client.app_pkgm.app_package_delete(
                app_pkg_id="appPkgId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_package_delete(app_pkg_id, request_options=request_options)
        return _response.data

    async def app_package_patch(
        self,
        app_pkg_id: str,
        *,
        operation_state: AppPkgInfoModificationsOperationState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppPkgInfoModifications:
        """
        Updates the operational state of an individual application package resources

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an individual application package resource

        operation_state : AppPkgInfoModificationsOperationState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgInfoModifications
            Shows that the operation has been completed successfully

        Examples
        --------
        import asyncio

        from fern import AppPkgInfoModificationsOperationState, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.app_package_patch(
                app_pkg_id="appPkgId",
                operation_state=AppPkgInfoModificationsOperationState.DISABLED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_package_patch(
            app_pkg_id, operation_state=operation_state, request_options=request_options
        )
        return _response.data

    async def app_pkg_id_get(
        self,
        app_pkg_id: str,
        *,
        filter: typing.Optional[str] = None,
        all_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        exclude_fields: typing.Optional[str] = None,
        exclude_default: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Reads the content of the AppD of on-boarded individual application package resources.

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an on-boarded individual application package

        filter : typing.Optional[str]
            Attribute-based filtering parameters according to ETSI GS MEC 009

        all_fields : typing.Optional[str]
            Include all complex attributes in the response.

        fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be included into the response

        exclude_fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be excluded from the response.

        exclude_default : typing.Optional[str]
            Indicates to exclude the following complex attributes of AppPkgInfo from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Content of the AppD is returned.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.app_pkg_id_get(
                app_pkg_id="appPkgId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_pkg_id_get(
            app_pkg_id,
            filter=filter,
            all_fields=all_fields,
            fields=fields,
            exclude_fields=exclude_fields,
            exclude_default=exclude_default,
            request_options=request_options,
        )
        return _response.data

    async def app_pkg_get(self, app_pkg_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Fetch the onboarded application package content identified by appPkgId or appDId.

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an on-boarded individual application package

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
            await client.app_pkgm.app_pkg_get(
                app_pkg_id="appPkgId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_pkg_get(app_pkg_id, request_options=request_options)
        return _response.data

    async def app_pkg_put(
        self,
        app_pkg_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Uploads the content of application package.

        Parameters
        ----------
        app_pkg_id : str
            Identifier of an on-boarded individual application package

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.app_pkg_put(app_pkg_id, request=request, request_options=request_options)
        return _response.data

    async def app_dget(
        self,
        app_d_id: str,
        *,
        filter: typing.Optional[str] = None,
        all_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        exclude_fields: typing.Optional[str] = None,
        exclude_default: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Reads the content of the AppD of on-boarded individual application package resources.

        Parameters
        ----------
        app_d_id : str
            Identifier of an application descriptor

        filter : typing.Optional[str]
            Attribute-based filtering parameters according to ETSI GS MEC 009

        all_fields : typing.Optional[str]
            Include all complex attributes in the response.

        fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be included into the response

        exclude_fields : typing.Optional[str]
            Complex attributes of AppPkgInfo to be excluded from the response.

        exclude_default : typing.Optional[str]
            Indicates to exclude the following complex attributes of AppPkgInfo from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Content of the AppD is returned.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.app_dget(
                app_d_id="appDId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_dget(
            app_d_id,
            filter=filter,
            all_fields=all_fields,
            fields=fields,
            exclude_fields=exclude_fields,
            exclude_default=exclude_default,
            request_options=request_options,
        )
        return _response.data

    async def app_d_id_get(self, app_d_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Fetch the onboarded application package content identified by appPkgId or appDId.

        Parameters
        ----------
        app_d_id : str
            Identifier of an application descriptor

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
            await client.app_pkgm.app_d_id_get(
                app_d_id="appDId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_d_id_get(app_d_id, request_options=request_options)
        return _response.data

    async def app_d_id_put(
        self,
        app_d_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Uploads the content of application package.

        Parameters
        ----------
        app_d_id : str
            Identifier of an application descriptor

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.app_d_id_put(app_d_id, request=request, request_options=request_options)
        return _response.data

    async def subscriptions_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppPkgSubscriptionLinkList:
        """
        used to retrieve the information of subscriptions to individual application package resource in MEO package

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgSubscriptionLinkList
            List of zero or more subscriptions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.subscriptions_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.subscriptions_get(request_options=request_options)
        return _response.data

    async def subscriptions_post(
        self,
        *,
        callback_uri: CallbackUri,
        subsctiption_type: SubsctiptionTypeAppPkg,
        app_pkg_filter: typing.Optional[typing.Sequence[AppPkgFilter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppPkgSubscriptionInfo:
        """
        Subscribe to notifications about on-boarding an application package

        Parameters
        ----------
        callback_uri : CallbackUri

        subsctiption_type : SubsctiptionTypeAppPkg

        app_pkg_filter : typing.Optional[typing.Sequence[AppPkgFilter]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgSubscriptionInfo
            Successful response for created subscription

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SubsctiptionTypeAppPkg

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.subscriptions_post(
                callback_uri="callbackUri",
                subsctiption_type=SubsctiptionTypeAppPkg.APP_PACKAGE_ON_BOARDING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscriptions_post(
            callback_uri=callback_uri,
            subsctiption_type=subsctiption_type,
            app_pkg_filter=app_pkg_filter,
            request_options=request_options,
        )
        return _response.data

    async def individual_subscription_get(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppPkgSubscriptionInfo:
        """
        Used to represent an individual subscription to notifications about application package changes.

        Parameters
        ----------
        subscription_id : str
            Identifier of an individual subscription to notifications about application package changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppPkgSubscriptionInfo
            Representation of the resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app_pkgm.individual_subscription_get(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.individual_subscription_get(subscription_id, request_options=request_options)
        return _response.data

    async def individual_subscription_delete(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the individual subscription to notifications about application package changes in MEO.

        Parameters
        ----------
        subscription_id : str
            Identifier of an individual subscription to notifications about application package changes

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
            await client.app_pkgm.individual_subscription_delete(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.individual_subscription_delete(
            subscription_id, request_options=request_options
        )
        return _response.data
