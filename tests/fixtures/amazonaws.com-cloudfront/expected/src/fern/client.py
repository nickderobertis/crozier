

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.tag_resource20161125request_operation import TagResource20161125RequestOperation
from .types.untag_resource20161125request_operation import UntagResource20161125RequestOperation


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    amz_content_sha256 : typing.Optional[str]
    amz_date : typing.Optional[str]
    amz_algorithm : typing.Optional[str]
    amz_credential : typing.Optional[str]
    amz_security_token : typing.Optional[str]
    amz_signature : typing.Optional[str]
    amz_signed_headers : typing.Optional[str]
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
        amz_date="YOUR_AMZ_DATE",
        amz_algorithm="YOUR_AMZ_ALGORITHM",
        amz_credential="YOUR_AMZ_CREDENTIAL",
        amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
        amz_signature="YOUR_AMZ_SIGNATURE",
        amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        amz_content_sha256: typing.Optional[str] = None,
        amz_date: typing.Optional[str] = None,
        amz_algorithm: typing.Optional[str] = None,
        amz_credential: typing.Optional[str] = None,
        amz_security_token: typing.Optional[str] = None,
        amz_signature: typing.Optional[str] = None,
        amz_signed_headers: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            amz_content_sha256=amz_content_sha256,
            amz_date=amz_date,
            amz_algorithm=amz_algorithm,
            amz_credential=amz_credential,
            amz_security_token=amz_security_token,
            amz_signature=amz_signature,
            amz_signed_headers=amz_signed_headers,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def list_cloud_front_origin_access_identities20161125(
        self,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Lists origin access identities.

        Parameters
        ----------
        marker : typing.Optional[str]
            Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).

        max_items : typing.Optional[str]
            The maximum number of origin access identities you want in the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.list_cloud_front_origin_access_identities20161125()
        """
        _response = self._raw_client.list_cloud_front_origin_access_identities20161125(
            marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    def create_cloud_front_origin_access_identity20161125(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Creates a new origin access identity. If you're using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.create_cloud_front_origin_access_identity20161125()
        """
        _response = self._raw_client.create_cloud_front_origin_access_identity20161125(request_options=request_options)
        return _response.data

    def list_distributions20161125(
        self,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        List distributions.

        Parameters
        ----------
        marker : typing.Optional[str]
            Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last distribution on that page).

        max_items : typing.Optional[str]
            The maximum number of distributions you want in the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.list_distributions20161125()
        """
        _response = self._raw_client.list_distributions20161125(
            marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    def create_distribution20161125(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Creates a new web distribution. Send a <code>GET</code> request to the <code>/<i>CloudFront API version</i>/distribution</code>/<code>distribution ID</code> resource.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.create_distribution20161125()
        """
        _response = self._raw_client.create_distribution20161125(request_options=request_options)
        return _response.data

    def create_distribution_with_tags20161125(
        self, *, with_tags: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create a new distribution with tags.

        Parameters
        ----------
        with_tags : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.create_distribution_with_tags20161125(
            with_tags=True,
        )
        """
        _response = self._raw_client.create_distribution_with_tags20161125(
            with_tags=with_tags, request_options=request_options
        )
        return _response.data

    def list_invalidations20161125(
        self,
        distribution_id: str,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Lists invalidation batches.

        Parameters
        ----------
        distribution_id : str
            The distribution's ID.

        marker : typing.Optional[str]
            Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.

        max_items : typing.Optional[str]
            The maximum number of invalidation batches that you want in the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.list_invalidations20161125(
            distribution_id="DistributionId",
        )
        """
        _response = self._raw_client.list_invalidations20161125(
            distribution_id, marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    def create_invalidation20161125(
        self, distribution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create a new invalidation.

        Parameters
        ----------
        distribution_id : str
            The distribution's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.create_invalidation20161125(
            distribution_id="DistributionId",
        )
        """
        _response = self._raw_client.create_invalidation20161125(distribution_id, request_options=request_options)
        return _response.data

    def list_streaming_distributions20161125(
        self,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        List streaming distributions.

        Parameters
        ----------
        marker : typing.Optional[str]
            The value that you provided for the <code>Marker</code> request parameter.

        max_items : typing.Optional[str]
            The value that you provided for the <code>MaxItems</code> request parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.list_streaming_distributions20161125()
        """
        _response = self._raw_client.list_streaming_distributions20161125(
            marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    def create_streaming_distribution20161125(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        <p>Creates a new RMTP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP. </p> <p>To create a new web distribution, submit a <code>POST</code> request to the <i>CloudFront API version</i>/distribution resource. The request body must include a document with a <i>StreamingDistributionConfig</i> element. The response echoes the <code>StreamingDistributionConfig</code> element and returns other information about the RTMP distribution.</p> <p>To get the status of your request, use the <i>GET StreamingDistribution</i> API action. When the value of <code>Enabled</code> is <code>true</code> and the value of <code>Status</code> is <code>Deployed</code>, your distribution is ready. A distribution usually deploys in less than 15 minutes.</p> <p>For more information about web distributions, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-rtmp.html">Working with RTMP Distributions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <important> <p>Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a web distribution or an RTMP distribution, and when you invalidate objects. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there's a mismatch between the number of values you say you're specifying in the <code>Quantity</code> element and the number of values specified.</p> </important>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.create_streaming_distribution20161125()
        """
        _response = self._raw_client.create_streaming_distribution20161125(request_options=request_options)
        return _response.data

    def create_streaming_distribution_with_tags20161125(
        self, *, with_tags: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create a new streaming distribution with tags.

        Parameters
        ----------
        with_tags : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.create_streaming_distribution_with_tags20161125(
            with_tags=True,
        )
        """
        _response = self._raw_client.create_streaming_distribution_with_tags20161125(
            with_tags=with_tags, request_options=request_options
        )
        return _response.data

    def get_cloud_front_origin_access_identity20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the information about an origin access identity.

        Parameters
        ----------
        id : str
            The identity's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_cloud_front_origin_access_identity20161125(
            id="Id",
        )
        """
        _response = self._raw_client.get_cloud_front_origin_access_identity20161125(id, request_options=request_options)
        return _response.data

    def delete_cloud_front_origin_access_identity20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an origin access identity.

        Parameters
        ----------
        id : str
            The origin access identity's ID.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.delete_cloud_front_origin_access_identity20161125(
            id="Id",
        )
        """
        _response = self._raw_client.delete_cloud_front_origin_access_identity20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    def get_distribution20161125(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get the information about a distribution.

        Parameters
        ----------
        id : str
            The distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_distribution20161125(
            id="Id",
        )
        """
        _response = self._raw_client.get_distribution20161125(id, request_options=request_options)
        return _response.data

    def delete_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a distribution.

        Parameters
        ----------
        id : str
            The distribution ID.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.delete_distribution20161125(
            id="Id",
        )
        """
        _response = self._raw_client.delete_distribution20161125(id, if_match=if_match, request_options=request_options)
        return _response.data

    def get_streaming_distribution20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Gets information about a specified RTMP distribution, including the distribution configuration.

        Parameters
        ----------
        id : str
            The streaming distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_streaming_distribution20161125(
            id="Id",
        )
        """
        _response = self._raw_client.get_streaming_distribution20161125(id, request_options=request_options)
        return _response.data

    def delete_streaming_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <p>Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.</p> <p> <b>To delete an RTMP distribution using the CloudFront API</b>:</p> <ol> <li> <p>Disable the RTMP distribution.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to get the current configuration and the <code>Etag</code> header for the distribution. </p> </li> <li> <p>Update the XML document that was returned in the response to your <code>GET Streaming Distribution Config</code> request to change the value of <code>Enabled</code> to <code>false</code>.</p> </li> <li> <p>Submit a <code>PUT Streaming Distribution Config</code> request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to the <code>PUT Streaming Distribution Config</code> request to confirm that the distribution was successfully disabled.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to confirm that your changes have propagated. When propagation is complete, the value of <code>Status</code> is <code>Deployed</code>.</p> </li> <li> <p>Submit a <code>DELETE Streaming Distribution</code> request. Set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to your <code>DELETE Streaming Distribution</code> request to confirm that the distribution was successfully deleted.</p> </li> </ol> <p>For information about deleting a distribution using the CloudFront console, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html">Deleting a Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Parameters
        ----------
        id : str
            The distribution ID.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.delete_streaming_distribution20161125(
            id="Id",
        )
        """
        _response = self._raw_client.delete_streaming_distribution20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    def get_cloud_front_origin_access_identity_config20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the configuration information about an origin access identity.

        Parameters
        ----------
        id : str
            The identity's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_cloud_front_origin_access_identity_config20161125(
            id="Id",
        )
        """
        _response = self._raw_client.get_cloud_front_origin_access_identity_config20161125(
            id, request_options=request_options
        )
        return _response.data

    def update_cloud_front_origin_access_identity20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Update an origin access identity.

        Parameters
        ----------
        id : str
            The identity's id.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.update_cloud_front_origin_access_identity20161125(
            id="Id",
        )
        """
        _response = self._raw_client.update_cloud_front_origin_access_identity20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    def get_distribution_config20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the configuration information about a distribution.

        Parameters
        ----------
        id : str
            The distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_distribution_config20161125(
            id="Id",
        )
        """
        _response = self._raw_client.get_distribution_config20161125(id, request_options=request_options)
        return _response.data

    def update_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Update a distribution.

        Parameters
        ----------
        id : str
            The distribution's id.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.update_distribution20161125(
            id="Id",
        )
        """
        _response = self._raw_client.update_distribution20161125(id, if_match=if_match, request_options=request_options)
        return _response.data

    def get_invalidation20161125(
        self, distribution_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the information about an invalidation.

        Parameters
        ----------
        distribution_id : str
            The distribution's ID.

        id : str
            The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_invalidation20161125(
            distribution_id="DistributionId",
            id="Id",
        )
        """
        _response = self._raw_client.get_invalidation20161125(distribution_id, id, request_options=request_options)
        return _response.data

    def get_streaming_distribution_config20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the configuration information about a streaming distribution.

        Parameters
        ----------
        id : str
            The streaming distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.get_streaming_distribution_config20161125(
            id="Id",
        )
        """
        _response = self._raw_client.get_streaming_distribution_config20161125(id, request_options=request_options)
        return _response.data

    def update_streaming_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Update a streaming distribution.

        Parameters
        ----------
        id : str
            The streaming distribution's id.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.update_streaming_distribution20161125(
            id="Id",
        )
        """
        _response = self._raw_client.update_streaming_distribution20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    def list_distributions_by_web_acl_id20161125(
        self,
        web_acl_id: str,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        List the distributions that are associated with a specified AWS WAF web ACL.

        Parameters
        ----------
        web_acl_id : str
            The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify "null" for the ID, the request returns a list of the distributions that aren't associated with a web ACL.

        marker : typing.Optional[str]
            Use <code>Marker</code> and <code>MaxItems</code> to control pagination of results. If you have more than <code>MaxItems</code> distributions that satisfy the request, the response includes a <code>NextMarker</code> element. To get the next page of results, submit another request. For the value of <code>Marker</code>, specify the value of <code>NextMarker</code> from the last response. (For the first request, omit <code>Marker</code>.)

        max_items : typing.Optional[str]
            The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.list_distributions_by_web_acl_id20161125(
            web_acl_id="WebACLId",
        )
        """
        _response = self._raw_client.list_distributions_by_web_acl_id20161125(
            web_acl_id, marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    def list_tags_for_resource20161125(
        self, *, resource: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        List tags for a CloudFront resource.

        Parameters
        ----------
        resource : str
             An ARN of a CloudFront resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.list_tags_for_resource20161125(
            resource="Resource",
        )
        """
        _response = self._raw_client.list_tags_for_resource20161125(resource=resource, request_options=request_options)
        return _response.data

    def tag_resource20161125(
        self,
        *,
        resource: str,
        operation: TagResource20161125RequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add tags to a CloudFront resource.

        Parameters
        ----------
        resource : str
             An ARN of a CloudFront resource.

        operation : TagResource20161125RequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, TagResource20161125RequestOperation

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.tag_resource20161125(
            resource="Resource",
            operation=TagResource20161125RequestOperation.TAG,
        )
        """
        _response = self._raw_client.tag_resource20161125(
            resource=resource, operation=operation, request_options=request_options
        )
        return _response.data

    def untag_resource20161125(
        self,
        *,
        resource: str,
        operation: UntagResource20161125RequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove tags from a CloudFront resource.

        Parameters
        ----------
        resource : str
             An ARN of a CloudFront resource.

        operation : UntagResource20161125RequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, UntagResource20161125RequestOperation

        client = FernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )
        client.untag_resource20161125(
            resource="Resource",
            operation=UntagResource20161125RequestOperation.UNTAG,
        )
        """
        _response = self._raw_client.untag_resource20161125(
            resource=resource, operation=operation, request_options=request_options
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    amz_content_sha256 : typing.Optional[str]
    amz_date : typing.Optional[str]
    amz_algorithm : typing.Optional[str]
    amz_credential : typing.Optional[str]
    amz_security_token : typing.Optional[str]
    amz_signature : typing.Optional[str]
    amz_signed_headers : typing.Optional[str]
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
        amz_date="YOUR_AMZ_DATE",
        amz_algorithm="YOUR_AMZ_ALGORITHM",
        amz_credential="YOUR_AMZ_CREDENTIAL",
        amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
        amz_signature="YOUR_AMZ_SIGNATURE",
        amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        amz_content_sha256: typing.Optional[str] = None,
        amz_date: typing.Optional[str] = None,
        amz_algorithm: typing.Optional[str] = None,
        amz_credential: typing.Optional[str] = None,
        amz_security_token: typing.Optional[str] = None,
        amz_signature: typing.Optional[str] = None,
        amz_signed_headers: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            amz_content_sha256=amz_content_sha256,
            amz_date=amz_date,
            amz_algorithm=amz_algorithm,
            amz_credential=amz_credential,
            amz_security_token=amz_security_token,
            amz_signature=amz_signature,
            amz_signed_headers=amz_signed_headers,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def list_cloud_front_origin_access_identities20161125(
        self,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Lists origin access identities.

        Parameters
        ----------
        marker : typing.Optional[str]
            Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).

        max_items : typing.Optional[str]
            The maximum number of origin access identities you want in the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_cloud_front_origin_access_identities20161125()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_cloud_front_origin_access_identities20161125(
            marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    async def create_cloud_front_origin_access_identity20161125(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Creates a new origin access identity. If you're using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_cloud_front_origin_access_identity20161125()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cloud_front_origin_access_identity20161125(
            request_options=request_options
        )
        return _response.data

    async def list_distributions20161125(
        self,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        List distributions.

        Parameters
        ----------
        marker : typing.Optional[str]
            Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last distribution on that page).

        max_items : typing.Optional[str]
            The maximum number of distributions you want in the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_distributions20161125()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_distributions20161125(
            marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    async def create_distribution20161125(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Creates a new web distribution. Send a <code>GET</code> request to the <code>/<i>CloudFront API version</i>/distribution</code>/<code>distribution ID</code> resource.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_distribution20161125()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_distribution20161125(request_options=request_options)
        return _response.data

    async def create_distribution_with_tags20161125(
        self, *, with_tags: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create a new distribution with tags.

        Parameters
        ----------
        with_tags : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_distribution_with_tags20161125(
                with_tags=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_distribution_with_tags20161125(
            with_tags=with_tags, request_options=request_options
        )
        return _response.data

    async def list_invalidations20161125(
        self,
        distribution_id: str,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Lists invalidation batches.

        Parameters
        ----------
        distribution_id : str
            The distribution's ID.

        marker : typing.Optional[str]
            Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.

        max_items : typing.Optional[str]
            The maximum number of invalidation batches that you want in the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_invalidations20161125(
                distribution_id="DistributionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_invalidations20161125(
            distribution_id, marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    async def create_invalidation20161125(
        self, distribution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create a new invalidation.

        Parameters
        ----------
        distribution_id : str
            The distribution's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_invalidation20161125(
                distribution_id="DistributionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_invalidation20161125(distribution_id, request_options=request_options)
        return _response.data

    async def list_streaming_distributions20161125(
        self,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        List streaming distributions.

        Parameters
        ----------
        marker : typing.Optional[str]
            The value that you provided for the <code>Marker</code> request parameter.

        max_items : typing.Optional[str]
            The value that you provided for the <code>MaxItems</code> request parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_streaming_distributions20161125()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_streaming_distributions20161125(
            marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    async def create_streaming_distribution20161125(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        <p>Creates a new RMTP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP. </p> <p>To create a new web distribution, submit a <code>POST</code> request to the <i>CloudFront API version</i>/distribution resource. The request body must include a document with a <i>StreamingDistributionConfig</i> element. The response echoes the <code>StreamingDistributionConfig</code> element and returns other information about the RTMP distribution.</p> <p>To get the status of your request, use the <i>GET StreamingDistribution</i> API action. When the value of <code>Enabled</code> is <code>true</code> and the value of <code>Status</code> is <code>Deployed</code>, your distribution is ready. A distribution usually deploys in less than 15 minutes.</p> <p>For more information about web distributions, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-rtmp.html">Working with RTMP Distributions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <important> <p>Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a web distribution or an RTMP distribution, and when you invalidate objects. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there's a mismatch between the number of values you say you're specifying in the <code>Quantity</code> element and the number of values specified.</p> </important>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_streaming_distribution20161125()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_streaming_distribution20161125(request_options=request_options)
        return _response.data

    async def create_streaming_distribution_with_tags20161125(
        self, *, with_tags: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create a new streaming distribution with tags.

        Parameters
        ----------
        with_tags : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_streaming_distribution_with_tags20161125(
                with_tags=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_streaming_distribution_with_tags20161125(
            with_tags=with_tags, request_options=request_options
        )
        return _response.data

    async def get_cloud_front_origin_access_identity20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the information about an origin access identity.

        Parameters
        ----------
        id : str
            The identity's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_cloud_front_origin_access_identity20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cloud_front_origin_access_identity20161125(
            id, request_options=request_options
        )
        return _response.data

    async def delete_cloud_front_origin_access_identity20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an origin access identity.

        Parameters
        ----------
        id : str
            The origin access identity's ID.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.

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
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_cloud_front_origin_access_identity20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cloud_front_origin_access_identity20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    async def get_distribution20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the information about a distribution.

        Parameters
        ----------
        id : str
            The distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_distribution20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_distribution20161125(id, request_options=request_options)
        return _response.data

    async def delete_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a distribution.

        Parameters
        ----------
        id : str
            The distribution ID.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.

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
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_distribution20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_distribution20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    async def get_streaming_distribution20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Gets information about a specified RTMP distribution, including the distribution configuration.

        Parameters
        ----------
        id : str
            The streaming distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_streaming_distribution20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_streaming_distribution20161125(id, request_options=request_options)
        return _response.data

    async def delete_streaming_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <p>Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.</p> <p> <b>To delete an RTMP distribution using the CloudFront API</b>:</p> <ol> <li> <p>Disable the RTMP distribution.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to get the current configuration and the <code>Etag</code> header for the distribution. </p> </li> <li> <p>Update the XML document that was returned in the response to your <code>GET Streaming Distribution Config</code> request to change the value of <code>Enabled</code> to <code>false</code>.</p> </li> <li> <p>Submit a <code>PUT Streaming Distribution Config</code> request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to the <code>PUT Streaming Distribution Config</code> request to confirm that the distribution was successfully disabled.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to confirm that your changes have propagated. When propagation is complete, the value of <code>Status</code> is <code>Deployed</code>.</p> </li> <li> <p>Submit a <code>DELETE Streaming Distribution</code> request. Set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to your <code>DELETE Streaming Distribution</code> request to confirm that the distribution was successfully deleted.</p> </li> </ol> <p>For information about deleting a distribution using the CloudFront console, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html">Deleting a Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Parameters
        ----------
        id : str
            The distribution ID.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.

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
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_streaming_distribution20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_streaming_distribution20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    async def get_cloud_front_origin_access_identity_config20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the configuration information about an origin access identity.

        Parameters
        ----------
        id : str
            The identity's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_cloud_front_origin_access_identity_config20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cloud_front_origin_access_identity_config20161125(
            id, request_options=request_options
        )
        return _response.data

    async def update_cloud_front_origin_access_identity20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Update an origin access identity.

        Parameters
        ----------
        id : str
            The identity's id.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_cloud_front_origin_access_identity20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cloud_front_origin_access_identity20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    async def get_distribution_config20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the configuration information about a distribution.

        Parameters
        ----------
        id : str
            The distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_distribution_config20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_distribution_config20161125(id, request_options=request_options)
        return _response.data

    async def update_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Update a distribution.

        Parameters
        ----------
        id : str
            The distribution's id.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_distribution20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_distribution20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    async def get_invalidation20161125(
        self, distribution_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the information about an invalidation.

        Parameters
        ----------
        distribution_id : str
            The distribution's ID.

        id : str
            The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_invalidation20161125(
                distribution_id="DistributionId",
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_invalidation20161125(
            distribution_id, id, request_options=request_options
        )
        return _response.data

    async def get_streaming_distribution_config20161125(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get the configuration information about a streaming distribution.

        Parameters
        ----------
        id : str
            The streaming distribution's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_streaming_distribution_config20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_streaming_distribution_config20161125(
            id, request_options=request_options
        )
        return _response.data

    async def update_streaming_distribution20161125(
        self, id: str, *, if_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Update a streaming distribution.

        Parameters
        ----------
        id : str
            The streaming distribution's id.

        if_match : typing.Optional[str]
            The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_streaming_distribution20161125(
                id="Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_streaming_distribution20161125(
            id, if_match=if_match, request_options=request_options
        )
        return _response.data

    async def list_distributions_by_web_acl_id20161125(
        self,
        web_acl_id: str,
        *,
        marker: typing.Optional[str] = None,
        max_items: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        List the distributions that are associated with a specified AWS WAF web ACL.

        Parameters
        ----------
        web_acl_id : str
            The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify "null" for the ID, the request returns a list of the distributions that aren't associated with a web ACL.

        marker : typing.Optional[str]
            Use <code>Marker</code> and <code>MaxItems</code> to control pagination of results. If you have more than <code>MaxItems</code> distributions that satisfy the request, the response includes a <code>NextMarker</code> element. To get the next page of results, submit another request. For the value of <code>Marker</code>, specify the value of <code>NextMarker</code> from the last response. (For the first request, omit <code>Marker</code>.)

        max_items : typing.Optional[str]
            The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_distributions_by_web_acl_id20161125(
                web_acl_id="WebACLId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_distributions_by_web_acl_id20161125(
            web_acl_id, marker=marker, max_items=max_items, request_options=request_options
        )
        return _response.data

    async def list_tags_for_resource20161125(
        self, *, resource: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        List tags for a CloudFront resource.

        Parameters
        ----------
        resource : str
             An ARN of a CloudFront resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_tags_for_resource20161125(
                resource="Resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags_for_resource20161125(
            resource=resource, request_options=request_options
        )
        return _response.data

    async def tag_resource20161125(
        self,
        *,
        resource: str,
        operation: TagResource20161125RequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add tags to a CloudFront resource.

        Parameters
        ----------
        resource : str
             An ARN of a CloudFront resource.

        operation : TagResource20161125RequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TagResource20161125RequestOperation

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tag_resource20161125(
                resource="Resource",
                operation=TagResource20161125RequestOperation.TAG,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tag_resource20161125(
            resource=resource, operation=operation, request_options=request_options
        )
        return _response.data

    async def untag_resource20161125(
        self,
        *,
        resource: str,
        operation: UntagResource20161125RequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove tags from a CloudFront resource.

        Parameters
        ----------
        resource : str
             An ARN of a CloudFront resource.

        operation : UntagResource20161125RequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UntagResource20161125RequestOperation

        client = AsyncFernApi(
            amz_content_sha256="YOUR_AMZ_CONTENT_SHA256",
            amz_date="YOUR_AMZ_DATE",
            amz_algorithm="YOUR_AMZ_ALGORITHM",
            amz_credential="YOUR_AMZ_CREDENTIAL",
            amz_security_token="YOUR_AMZ_SECURITY_TOKEN",
            amz_signature="YOUR_AMZ_SIGNATURE",
            amz_signed_headers="YOUR_AMZ_SIGNED_HEADERS",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.untag_resource20161125(
                resource="Resource",
                operation=UntagResource20161125RequestOperation.UNTAG,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.untag_resource20161125(
            resource=resource, operation=operation, request_options=request_options
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
