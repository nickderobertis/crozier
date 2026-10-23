

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_token import AccessToken
from ..types.ls_datasets import LsDatasets
from .raw_client import AsyncRawUtilityClient, RawUtilityClient


class UtilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUtilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUtilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUtilityClient
        """
        return self._raw_client

    def ls(
        self,
        *,
        sdpath: str,
        wmode: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LsDatasets:
        """
        <ul>
        <li>Return the list of datasets and sub-directories of a seismic store path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path, sd://tenant/sub-project/path.

        wmode : typing.Optional[str]
            Working mode, directories or datasets or undefined for both.

        limit : typing.Optional[float]
            Limits the total number of datasets to return.

        cursor : typing.Optional[str]
            Pagination token - this query parameter can be omitted on first call.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LsDatasets
            Seismic store path content.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.utility.ls(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.ls(
            sdpath=sdpath,
            wmode=wmode,
            limit=limit,
            cursor=cursor,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def storage_tiers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        <ul><li>Return the list of storage tiers</ul>

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

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.utility.storage_tiers()
        """
        _response = self._raw_client.storage_tiers(request_options=request_options)
        return _response.data

    def cp(
        self,
        *,
        sdpath_from: str,
        sdpath_to: str,
        lock: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        <ul>
        <li>Copy a seismic store dataset. The source and destination dataset must be in the same sub-project.</li>
        <li>Required roles:
          <ul>
            <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
            <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
          </ul>
        </li>
        </ul>

        Parameters
        ----------
        sdpath_from : str
            Seismic store source dataset path.

        sdpath_to : str
            Seismic store destination dataset path.

        lock : typing.Optional[bool]
            Lock source and destination while copying.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Copy operation succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.utility.cp(
            sdpath_from="sdpath_from",
            sdpath_to="sdpath_to",
        )
        """
        _response = self._raw_client.cp(
            sdpath_from=sdpath_from,
            sdpath_to=sdpath_to,
            lock=lock,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def gcs_access_token(
        self,
        *,
        sdpath: str,
        readonly: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessToken:
        """
        <ul>
          <li>Generate a GCS access token for a specified seismic store resource. The source and destination dataset must be in the same sub-project.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/sub-project.

        readonly : typing.Optional[bool]
            Readonly access, true(default) or false.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            The GCS access token.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.utility.gcs_access_token(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.gcs_access_token(
            sdpath=sdpath,
            readonly=readonly,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def upload_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessToken:
        """
        <ul> <li>Generate the upload connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk upload.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            The upload connection credential string.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.utility.upload_connection_string(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.upload_connection_string(
            sdpath=sdpath, impersonation_token_context=impersonation_token_context, request_options=request_options
        )
        return _response.data

    def download_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessToken:
        """
        <ul> <li>Generate the download connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk download.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            The download connection credential string.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.utility.download_connection_string(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.download_connection_string(
            sdpath=sdpath, impersonation_token_context=impersonation_token_context, request_options=request_options
        )
        return _response.data


class AsyncUtilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUtilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUtilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUtilityClient
        """
        return self._raw_client

    async def ls(
        self,
        *,
        sdpath: str,
        wmode: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LsDatasets:
        """
        <ul>
        <li>Return the list of datasets and sub-directories of a seismic store path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path, sd://tenant/sub-project/path.

        wmode : typing.Optional[str]
            Working mode, directories or datasets or undefined for both.

        limit : typing.Optional[float]
            Limits the total number of datasets to return.

        cursor : typing.Optional[str]
            Pagination token - this query parameter can be omitted on first call.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LsDatasets
            Seismic store path content.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.utility.ls(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ls(
            sdpath=sdpath,
            wmode=wmode,
            limit=limit,
            cursor=cursor,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def storage_tiers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        <ul><li>Return the list of storage tiers</ul>

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

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.utility.storage_tiers()


        asyncio.run(main())
        """
        _response = await self._raw_client.storage_tiers(request_options=request_options)
        return _response.data

    async def cp(
        self,
        *,
        sdpath_from: str,
        sdpath_to: str,
        lock: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        <ul>
        <li>Copy a seismic store dataset. The source and destination dataset must be in the same sub-project.</li>
        <li>Required roles:
          <ul>
            <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
            <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
          </ul>
        </li>
        </ul>

        Parameters
        ----------
        sdpath_from : str
            Seismic store source dataset path.

        sdpath_to : str
            Seismic store destination dataset path.

        lock : typing.Optional[bool]
            Lock source and destination while copying.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Copy operation succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.utility.cp(
                sdpath_from="sdpath_from",
                sdpath_to="sdpath_to",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cp(
            sdpath_from=sdpath_from,
            sdpath_to=sdpath_to,
            lock=lock,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def gcs_access_token(
        self,
        *,
        sdpath: str,
        readonly: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessToken:
        """
        <ul>
          <li>Generate a GCS access token for a specified seismic store resource. The source and destination dataset must be in the same sub-project.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/sub-project.

        readonly : typing.Optional[bool]
            Readonly access, true(default) or false.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            The GCS access token.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.utility.gcs_access_token(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gcs_access_token(
            sdpath=sdpath,
            readonly=readonly,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def upload_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessToken:
        """
        <ul> <li>Generate the upload connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk upload.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            The upload connection credential string.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.utility.upload_connection_string(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_connection_string(
            sdpath=sdpath, impersonation_token_context=impersonation_token_context, request_options=request_options
        )
        return _response.data

    async def download_connection_string(
        self,
        *,
        sdpath: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessToken:
        """
        <ul> <li>Generate the download connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk download.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>

        Parameters
        ----------
        sdpath : str
            Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            The download connection credential string.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.utility.download_connection_string(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_connection_string(
            sdpath=sdpath, impersonation_token_context=impersonation_token_context, request_options=request_options
        )
        return _response.data
