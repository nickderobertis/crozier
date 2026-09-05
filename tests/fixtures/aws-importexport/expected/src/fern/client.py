

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.generic_string import GenericString
from .types.get_cancel_job_request_action import GetCancelJobRequestAction
from .types.get_cancel_job_request_operation import GetCancelJobRequestOperation
from .types.get_cancel_job_request_version import GetCancelJobRequestVersion
from .types.get_create_job_request_action import GetCreateJobRequestAction
from .types.get_create_job_request_job_type import GetCreateJobRequestJobType
from .types.get_create_job_request_operation import GetCreateJobRequestOperation
from .types.get_create_job_request_version import GetCreateJobRequestVersion
from .types.get_get_shipping_label_request_action import GetGetShippingLabelRequestAction
from .types.get_get_shipping_label_request_operation import GetGetShippingLabelRequestOperation
from .types.get_get_shipping_label_request_version import GetGetShippingLabelRequestVersion
from .types.get_get_status_request_action import GetGetStatusRequestAction
from .types.get_get_status_request_operation import GetGetStatusRequestOperation
from .types.get_get_status_request_version import GetGetStatusRequestVersion
from .types.get_list_jobs_request_action import GetListJobsRequestAction
from .types.get_list_jobs_request_operation import GetListJobsRequestOperation
from .types.get_list_jobs_request_version import GetListJobsRequestVersion
from .types.get_update_job_request_action import GetUpdateJobRequestAction
from .types.get_update_job_request_job_type import GetUpdateJobRequestJobType
from .types.get_update_job_request_operation import GetUpdateJobRequestOperation
from .types.get_update_job_request_version import GetUpdateJobRequestVersion
from .types.post_cancel_job_request_action import PostCancelJobRequestAction
from .types.post_cancel_job_request_operation import PostCancelJobRequestOperation
from .types.post_cancel_job_request_version import PostCancelJobRequestVersion
from .types.post_create_job_request_action import PostCreateJobRequestAction
from .types.post_create_job_request_operation import PostCreateJobRequestOperation
from .types.post_create_job_request_version import PostCreateJobRequestVersion
from .types.post_get_shipping_label_request_action import PostGetShippingLabelRequestAction
from .types.post_get_shipping_label_request_operation import PostGetShippingLabelRequestOperation
from .types.post_get_shipping_label_request_version import PostGetShippingLabelRequestVersion
from .types.post_get_status_request_action import PostGetStatusRequestAction
from .types.post_get_status_request_operation import PostGetStatusRequestOperation
from .types.post_get_status_request_version import PostGetStatusRequestVersion
from .types.post_list_jobs_request_action import PostListJobsRequestAction
from .types.post_list_jobs_request_operation import PostListJobsRequestOperation
from .types.post_list_jobs_request_version import PostListJobsRequestVersion
from .types.post_update_job_request_action import PostUpdateJobRequestAction
from .types.post_update_job_request_operation import PostUpdateJobRequestOperation
from .types.post_update_job_request_version import PostUpdateJobRequestVersion


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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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

    def get_cancel_job(
        self,
        *,
        aws_access_key_id: str,
        action: GetCancelJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetCancelJobRequestVersion,
        signature: str,
        job_id: str,
        operation: GetCancelJobRequestOperation,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetCancelJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetCancelJobRequestVersion

        signature : str

        job_id : str


        operation : GetCancelJobRequestOperation

        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            GetCancelJobRequestAction,
            GetCancelJobRequestOperation,
            GetCancelJobRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_cancel_job(
            aws_access_key_id="AWSAccessKeyId",
            action=GetCancelJobRequestAction.CANCEL_JOB,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=GetCancelJobRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            job_id="JobId",
            operation=GetCancelJobRequestOperation.CANCEL_JOB,
        )
        """
        _response = self._raw_client.get_cancel_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_id=job_id,
            operation=operation,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def post_cancel_job(
        self,
        *,
        aws_access_key_id: str,
        action: PostCancelJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostCancelJobRequestVersion,
        signature: str,
        operation: PostCancelJobRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostCancelJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostCancelJobRequestVersion

        signature : str

        operation : PostCancelJobRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            PostCancelJobRequestAction,
            PostCancelJobRequestOperation,
            PostCancelJobRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_cancel_job(
            aws_access_key_id="AWSAccessKeyId",
            action=PostCancelJobRequestAction.CANCEL_JOB,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=PostCancelJobRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=PostCancelJobRequestOperation.CANCEL_JOB,
        )
        """
        _response = self._raw_client.post_cancel_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    def get_create_job(
        self,
        *,
        aws_access_key_id: str,
        action: GetCreateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetCreateJobRequestVersion,
        signature: str,
        job_type: GetCreateJobRequestJobType,
        manifest: str,
        validate_only: bool,
        operation: GetCreateJobRequestOperation,
        manifest_addendum: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetCreateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetCreateJobRequestVersion

        signature : str

        job_type : GetCreateJobRequestJobType


        manifest : str


        validate_only : bool


        operation : GetCreateJobRequestOperation

        manifest_addendum : typing.Optional[str]


        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            GetCreateJobRequestAction,
            GetCreateJobRequestJobType,
            GetCreateJobRequestOperation,
            GetCreateJobRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_create_job(
            aws_access_key_id="AWSAccessKeyId",
            action=GetCreateJobRequestAction.CREATE_JOB,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=GetCreateJobRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            job_type=GetCreateJobRequestJobType.IMPORT,
            manifest="Manifest",
            validate_only=True,
            operation=GetCreateJobRequestOperation.CREATE_JOB,
        )
        """
        _response = self._raw_client.get_create_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_type=job_type,
            manifest=manifest,
            validate_only=validate_only,
            operation=operation,
            manifest_addendum=manifest_addendum,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def post_create_job(
        self,
        *,
        aws_access_key_id: str,
        action: PostCreateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostCreateJobRequestVersion,
        signature: str,
        operation: PostCreateJobRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostCreateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostCreateJobRequestVersion

        signature : str

        operation : PostCreateJobRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            PostCreateJobRequestAction,
            PostCreateJobRequestOperation,
            PostCreateJobRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_create_job(
            aws_access_key_id="AWSAccessKeyId",
            action=PostCreateJobRequestAction.CREATE_JOB,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=PostCreateJobRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=PostCreateJobRequestOperation.CREATE_JOB,
        )
        """
        _response = self._raw_client.post_create_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    def get_get_shipping_label(
        self,
        *,
        aws_access_key_id: str,
        action: GetGetShippingLabelRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetGetShippingLabelRequestVersion,
        signature: str,
        operation: GetGetShippingLabelRequestOperation,
        job_ids: typing.Optional[typing.Union[GenericString, typing.Sequence[GenericString]]] = None,
        name: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        state_or_province: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        street1: typing.Optional[str] = None,
        street2: typing.Optional[str] = None,
        street3: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetGetShippingLabelRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetGetShippingLabelRequestVersion

        signature : str

        operation : GetGetShippingLabelRequestOperation

        job_ids : typing.Optional[typing.Union[GenericString, typing.Sequence[GenericString]]]


        name : typing.Optional[str]


        company : typing.Optional[str]


        phone_number : typing.Optional[str]


        country : typing.Optional[str]


        state_or_province : typing.Optional[str]


        city : typing.Optional[str]


        postal_code : typing.Optional[str]


        street1 : typing.Optional[str]


        street2 : typing.Optional[str]


        street3 : typing.Optional[str]


        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            GetGetShippingLabelRequestAction,
            GetGetShippingLabelRequestOperation,
            GetGetShippingLabelRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_get_shipping_label(
            aws_access_key_id="AWSAccessKeyId",
            action=GetGetShippingLabelRequestAction.GET_SHIPPING_LABEL,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=GetGetShippingLabelRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=GetGetShippingLabelRequestOperation.GET_SHIPPING_LABEL,
        )
        """
        _response = self._raw_client.get_get_shipping_label(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            job_ids=job_ids,
            name=name,
            company=company,
            phone_number=phone_number,
            country=country,
            state_or_province=state_or_province,
            city=city,
            postal_code=postal_code,
            street1=street1,
            street2=street2,
            street3=street3,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def post_get_shipping_label(
        self,
        *,
        aws_access_key_id: str,
        action: PostGetShippingLabelRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostGetShippingLabelRequestVersion,
        signature: str,
        operation: PostGetShippingLabelRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostGetShippingLabelRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostGetShippingLabelRequestVersion

        signature : str

        operation : PostGetShippingLabelRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            PostGetShippingLabelRequestAction,
            PostGetShippingLabelRequestOperation,
            PostGetShippingLabelRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_get_shipping_label(
            aws_access_key_id="AWSAccessKeyId",
            action=PostGetShippingLabelRequestAction.GET_SHIPPING_LABEL,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=PostGetShippingLabelRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=PostGetShippingLabelRequestOperation.GET_SHIPPING_LABEL,
        )
        """
        _response = self._raw_client.post_get_shipping_label(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    def get_get_status(
        self,
        *,
        aws_access_key_id: str,
        action: GetGetStatusRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetGetStatusRequestVersion,
        signature: str,
        job_id: str,
        operation: GetGetStatusRequestOperation,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetGetStatusRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetGetStatusRequestVersion

        signature : str

        job_id : str


        operation : GetGetStatusRequestOperation

        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            GetGetStatusRequestAction,
            GetGetStatusRequestOperation,
            GetGetStatusRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_get_status(
            aws_access_key_id="AWSAccessKeyId",
            action=GetGetStatusRequestAction.GET_STATUS,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=GetGetStatusRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            job_id="JobId",
            operation=GetGetStatusRequestOperation.GET_STATUS,
        )
        """
        _response = self._raw_client.get_get_status(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_id=job_id,
            operation=operation,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def post_get_status(
        self,
        *,
        aws_access_key_id: str,
        action: PostGetStatusRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostGetStatusRequestVersion,
        signature: str,
        operation: PostGetStatusRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostGetStatusRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostGetStatusRequestVersion

        signature : str

        operation : PostGetStatusRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            PostGetStatusRequestAction,
            PostGetStatusRequestOperation,
            PostGetStatusRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_get_status(
            aws_access_key_id="AWSAccessKeyId",
            action=PostGetStatusRequestAction.GET_STATUS,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=PostGetStatusRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=PostGetStatusRequestOperation.GET_STATUS,
        )
        """
        _response = self._raw_client.post_get_status(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    def get_list_jobs(
        self,
        *,
        aws_access_key_id: str,
        action: GetListJobsRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetListJobsRequestVersion,
        signature: str,
        operation: GetListJobsRequestOperation,
        max_jobs: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetListJobsRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetListJobsRequestVersion

        signature : str

        operation : GetListJobsRequestOperation

        max_jobs : typing.Optional[int]


        marker : typing.Optional[str]


        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            GetListJobsRequestAction,
            GetListJobsRequestOperation,
            GetListJobsRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_list_jobs(
            aws_access_key_id="AWSAccessKeyId",
            action=GetListJobsRequestAction.LIST_JOBS,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=GetListJobsRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=GetListJobsRequestOperation.LIST_JOBS,
        )
        """
        _response = self._raw_client.get_list_jobs(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            max_jobs=max_jobs,
            marker=marker,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def post_list_jobs(
        self,
        *,
        aws_access_key_id: str,
        action: PostListJobsRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostListJobsRequestVersion,
        signature: str,
        operation: PostListJobsRequestOperation,
        max_jobs: typing.Optional[str] = None,
        marker: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostListJobsRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostListJobsRequestVersion

        signature : str

        operation : PostListJobsRequestOperation

        max_jobs : typing.Optional[str]
            Pagination limit

        marker : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            PostListJobsRequestAction,
            PostListJobsRequestOperation,
            PostListJobsRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_list_jobs(
            aws_access_key_id="AWSAccessKeyId",
            action=PostListJobsRequestAction.LIST_JOBS,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=PostListJobsRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=PostListJobsRequestOperation.LIST_JOBS,
        )
        """
        _response = self._raw_client.post_list_jobs(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            max_jobs=max_jobs,
            marker=marker,
            request_options=request_options,
        )
        return _response.data

    def get_update_job(
        self,
        *,
        aws_access_key_id: str,
        action: GetUpdateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetUpdateJobRequestVersion,
        signature: str,
        job_id: str,
        manifest: str,
        job_type: GetUpdateJobRequestJobType,
        validate_only: bool,
        operation: GetUpdateJobRequestOperation,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetUpdateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetUpdateJobRequestVersion

        signature : str

        job_id : str


        manifest : str


        job_type : GetUpdateJobRequestJobType


        validate_only : bool


        operation : GetUpdateJobRequestOperation

        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            GetUpdateJobRequestAction,
            GetUpdateJobRequestJobType,
            GetUpdateJobRequestOperation,
            GetUpdateJobRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_update_job(
            aws_access_key_id="AWSAccessKeyId",
            action=GetUpdateJobRequestAction.UPDATE_JOB,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=GetUpdateJobRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            job_id="JobId",
            manifest="Manifest",
            job_type=GetUpdateJobRequestJobType.IMPORT,
            validate_only=True,
            operation=GetUpdateJobRequestOperation.UPDATE_JOB,
        )
        """
        _response = self._raw_client.get_update_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_id=job_id,
            manifest=manifest,
            job_type=job_type,
            validate_only=validate_only,
            operation=operation,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    def post_update_job(
        self,
        *,
        aws_access_key_id: str,
        action: PostUpdateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostUpdateJobRequestVersion,
        signature: str,
        operation: PostUpdateJobRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostUpdateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostUpdateJobRequestVersion

        signature : str

        operation : PostUpdateJobRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import (
            FernApi,
            PostUpdateJobRequestAction,
            PostUpdateJobRequestOperation,
            PostUpdateJobRequestVersion,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_update_job(
            aws_access_key_id="AWSAccessKeyId",
            action=PostUpdateJobRequestAction.UPDATE_JOB,
            signature_method="SignatureMethod",
            signature_version="SignatureVersion",
            timestamp="Timestamp",
            version=PostUpdateJobRequestVersion.TWO_THOUSAND_TEN0601,
            signature="Signature",
            operation=PostUpdateJobRequestOperation.UPDATE_JOB,
        )
        """
        _response = self._raw_client.post_update_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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

    async def get_cancel_job(
        self,
        *,
        aws_access_key_id: str,
        action: GetCancelJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetCancelJobRequestVersion,
        signature: str,
        job_id: str,
        operation: GetCancelJobRequestOperation,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetCancelJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetCancelJobRequestVersion

        signature : str

        job_id : str


        operation : GetCancelJobRequestOperation

        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GetCancelJobRequestAction,
            GetCancelJobRequestOperation,
            GetCancelJobRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_cancel_job(
                aws_access_key_id="AWSAccessKeyId",
                action=GetCancelJobRequestAction.CANCEL_JOB,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=GetCancelJobRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                job_id="JobId",
                operation=GetCancelJobRequestOperation.CANCEL_JOB,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cancel_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_id=job_id,
            operation=operation,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def post_cancel_job(
        self,
        *,
        aws_access_key_id: str,
        action: PostCancelJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostCancelJobRequestVersion,
        signature: str,
        operation: PostCancelJobRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostCancelJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostCancelJobRequestVersion

        signature : str

        operation : PostCancelJobRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostCancelJobRequestAction,
            PostCancelJobRequestOperation,
            PostCancelJobRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_cancel_job(
                aws_access_key_id="AWSAccessKeyId",
                action=PostCancelJobRequestAction.CANCEL_JOB,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=PostCancelJobRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=PostCancelJobRequestOperation.CANCEL_JOB,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_cancel_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    async def get_create_job(
        self,
        *,
        aws_access_key_id: str,
        action: GetCreateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetCreateJobRequestVersion,
        signature: str,
        job_type: GetCreateJobRequestJobType,
        manifest: str,
        validate_only: bool,
        operation: GetCreateJobRequestOperation,
        manifest_addendum: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetCreateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetCreateJobRequestVersion

        signature : str

        job_type : GetCreateJobRequestJobType


        manifest : str


        validate_only : bool


        operation : GetCreateJobRequestOperation

        manifest_addendum : typing.Optional[str]


        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GetCreateJobRequestAction,
            GetCreateJobRequestJobType,
            GetCreateJobRequestOperation,
            GetCreateJobRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_create_job(
                aws_access_key_id="AWSAccessKeyId",
                action=GetCreateJobRequestAction.CREATE_JOB,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=GetCreateJobRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                job_type=GetCreateJobRequestJobType.IMPORT,
                manifest="Manifest",
                validate_only=True,
                operation=GetCreateJobRequestOperation.CREATE_JOB,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_create_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_type=job_type,
            manifest=manifest,
            validate_only=validate_only,
            operation=operation,
            manifest_addendum=manifest_addendum,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def post_create_job(
        self,
        *,
        aws_access_key_id: str,
        action: PostCreateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostCreateJobRequestVersion,
        signature: str,
        operation: PostCreateJobRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostCreateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostCreateJobRequestVersion

        signature : str

        operation : PostCreateJobRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostCreateJobRequestAction,
            PostCreateJobRequestOperation,
            PostCreateJobRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_create_job(
                aws_access_key_id="AWSAccessKeyId",
                action=PostCreateJobRequestAction.CREATE_JOB,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=PostCreateJobRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=PostCreateJobRequestOperation.CREATE_JOB,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_create_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    async def get_get_shipping_label(
        self,
        *,
        aws_access_key_id: str,
        action: GetGetShippingLabelRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetGetShippingLabelRequestVersion,
        signature: str,
        operation: GetGetShippingLabelRequestOperation,
        job_ids: typing.Optional[typing.Union[GenericString, typing.Sequence[GenericString]]] = None,
        name: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        state_or_province: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        street1: typing.Optional[str] = None,
        street2: typing.Optional[str] = None,
        street3: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetGetShippingLabelRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetGetShippingLabelRequestVersion

        signature : str

        operation : GetGetShippingLabelRequestOperation

        job_ids : typing.Optional[typing.Union[GenericString, typing.Sequence[GenericString]]]


        name : typing.Optional[str]


        company : typing.Optional[str]


        phone_number : typing.Optional[str]


        country : typing.Optional[str]


        state_or_province : typing.Optional[str]


        city : typing.Optional[str]


        postal_code : typing.Optional[str]


        street1 : typing.Optional[str]


        street2 : typing.Optional[str]


        street3 : typing.Optional[str]


        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GetGetShippingLabelRequestAction,
            GetGetShippingLabelRequestOperation,
            GetGetShippingLabelRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_get_shipping_label(
                aws_access_key_id="AWSAccessKeyId",
                action=GetGetShippingLabelRequestAction.GET_SHIPPING_LABEL,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=GetGetShippingLabelRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=GetGetShippingLabelRequestOperation.GET_SHIPPING_LABEL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_get_shipping_label(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            job_ids=job_ids,
            name=name,
            company=company,
            phone_number=phone_number,
            country=country,
            state_or_province=state_or_province,
            city=city,
            postal_code=postal_code,
            street1=street1,
            street2=street2,
            street3=street3,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def post_get_shipping_label(
        self,
        *,
        aws_access_key_id: str,
        action: PostGetShippingLabelRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostGetShippingLabelRequestVersion,
        signature: str,
        operation: PostGetShippingLabelRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostGetShippingLabelRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostGetShippingLabelRequestVersion

        signature : str

        operation : PostGetShippingLabelRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostGetShippingLabelRequestAction,
            PostGetShippingLabelRequestOperation,
            PostGetShippingLabelRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_get_shipping_label(
                aws_access_key_id="AWSAccessKeyId",
                action=PostGetShippingLabelRequestAction.GET_SHIPPING_LABEL,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=PostGetShippingLabelRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=PostGetShippingLabelRequestOperation.GET_SHIPPING_LABEL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_get_shipping_label(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    async def get_get_status(
        self,
        *,
        aws_access_key_id: str,
        action: GetGetStatusRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetGetStatusRequestVersion,
        signature: str,
        job_id: str,
        operation: GetGetStatusRequestOperation,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetGetStatusRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetGetStatusRequestVersion

        signature : str

        job_id : str


        operation : GetGetStatusRequestOperation

        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GetGetStatusRequestAction,
            GetGetStatusRequestOperation,
            GetGetStatusRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_get_status(
                aws_access_key_id="AWSAccessKeyId",
                action=GetGetStatusRequestAction.GET_STATUS,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=GetGetStatusRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                job_id="JobId",
                operation=GetGetStatusRequestOperation.GET_STATUS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_get_status(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_id=job_id,
            operation=operation,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def post_get_status(
        self,
        *,
        aws_access_key_id: str,
        action: PostGetStatusRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostGetStatusRequestVersion,
        signature: str,
        operation: PostGetStatusRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostGetStatusRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostGetStatusRequestVersion

        signature : str

        operation : PostGetStatusRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostGetStatusRequestAction,
            PostGetStatusRequestOperation,
            PostGetStatusRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_get_status(
                aws_access_key_id="AWSAccessKeyId",
                action=PostGetStatusRequestAction.GET_STATUS,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=PostGetStatusRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=PostGetStatusRequestOperation.GET_STATUS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_get_status(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data

    async def get_list_jobs(
        self,
        *,
        aws_access_key_id: str,
        action: GetListJobsRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetListJobsRequestVersion,
        signature: str,
        operation: GetListJobsRequestOperation,
        max_jobs: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetListJobsRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetListJobsRequestVersion

        signature : str

        operation : GetListJobsRequestOperation

        max_jobs : typing.Optional[int]


        marker : typing.Optional[str]


        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GetListJobsRequestAction,
            GetListJobsRequestOperation,
            GetListJobsRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_list_jobs(
                aws_access_key_id="AWSAccessKeyId",
                action=GetListJobsRequestAction.LIST_JOBS,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=GetListJobsRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=GetListJobsRequestOperation.LIST_JOBS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_list_jobs(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            max_jobs=max_jobs,
            marker=marker,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def post_list_jobs(
        self,
        *,
        aws_access_key_id: str,
        action: PostListJobsRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostListJobsRequestVersion,
        signature: str,
        operation: PostListJobsRequestOperation,
        max_jobs: typing.Optional[str] = None,
        marker: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostListJobsRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostListJobsRequestVersion

        signature : str

        operation : PostListJobsRequestOperation

        max_jobs : typing.Optional[str]
            Pagination limit

        marker : typing.Optional[str]
            Pagination token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostListJobsRequestAction,
            PostListJobsRequestOperation,
            PostListJobsRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_list_jobs(
                aws_access_key_id="AWSAccessKeyId",
                action=PostListJobsRequestAction.LIST_JOBS,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=PostListJobsRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=PostListJobsRequestOperation.LIST_JOBS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_list_jobs(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            max_jobs=max_jobs,
            marker=marker,
            request_options=request_options,
        )
        return _response.data

    async def get_update_job(
        self,
        *,
        aws_access_key_id: str,
        action: GetUpdateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: GetUpdateJobRequestVersion,
        signature: str,
        job_id: str,
        manifest: str,
        job_type: GetUpdateJobRequestJobType,
        validate_only: bool,
        operation: GetUpdateJobRequestOperation,
        api_version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : GetUpdateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : GetUpdateJobRequestVersion

        signature : str

        job_id : str


        manifest : str


        job_type : GetUpdateJobRequestJobType


        validate_only : bool


        operation : GetUpdateJobRequestOperation

        api_version : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GetUpdateJobRequestAction,
            GetUpdateJobRequestJobType,
            GetUpdateJobRequestOperation,
            GetUpdateJobRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_update_job(
                aws_access_key_id="AWSAccessKeyId",
                action=GetUpdateJobRequestAction.UPDATE_JOB,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=GetUpdateJobRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                job_id="JobId",
                manifest="Manifest",
                job_type=GetUpdateJobRequestJobType.IMPORT,
                validate_only=True,
                operation=GetUpdateJobRequestOperation.UPDATE_JOB,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_update_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            job_id=job_id,
            manifest=manifest,
            job_type=job_type,
            validate_only=validate_only,
            operation=operation,
            api_version=api_version,
            request_options=request_options,
        )
        return _response.data

    async def post_update_job(
        self,
        *,
        aws_access_key_id: str,
        action: PostUpdateJobRequestAction,
        signature_method: str,
        signature_version: str,
        timestamp: str,
        version: PostUpdateJobRequestVersion,
        signature: str,
        operation: PostUpdateJobRequestOperation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

        Parameters
        ----------
        aws_access_key_id : str

        action : PostUpdateJobRequestAction

        signature_method : str

        signature_version : str

        timestamp : str

        version : PostUpdateJobRequestVersion

        signature : str

        operation : PostUpdateJobRequestOperation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PostUpdateJobRequestAction,
            PostUpdateJobRequestOperation,
            PostUpdateJobRequestVersion,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_update_job(
                aws_access_key_id="AWSAccessKeyId",
                action=PostUpdateJobRequestAction.UPDATE_JOB,
                signature_method="SignatureMethod",
                signature_version="SignatureVersion",
                timestamp="Timestamp",
                version=PostUpdateJobRequestVersion.TWO_THOUSAND_TEN0601,
                signature="Signature",
                operation=PostUpdateJobRequestOperation.UPDATE_JOB,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_update_job(
            aws_access_key_id=aws_access_key_id,
            action=action,
            signature_method=signature_method,
            signature_version=signature_version,
            timestamp=timestamp,
            version=version,
            signature=signature,
            operation=operation,
            request_options=request_options,
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
