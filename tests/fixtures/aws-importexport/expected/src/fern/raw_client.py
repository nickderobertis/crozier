

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
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
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=CancelJob&Action=CancelJob",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobId": job_id,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=CancelJob&Action=CancelJob",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=CreateJob&Action=CreateJob",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobType": job_type,
                "Manifest": manifest,
                "ManifestAddendum": manifest_addendum,
                "ValidateOnly": validate_only,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=CreateJob&Action=CreateJob",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=GetShippingLabel&Action=GetShippingLabel",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "jobIds": job_ids,
                "name": name,
                "company": company,
                "phoneNumber": phone_number,
                "country": country,
                "stateOrProvince": state_or_province,
                "city": city,
                "postalCode": postal_code,
                "street1": street1,
                "street2": street2,
                "street3": street3,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=GetShippingLabel&Action=GetShippingLabel",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=GetStatus&Action=GetStatus",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobId": job_id,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=GetStatus&Action=GetStatus",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=ListJobs&Action=ListJobs",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "MaxJobs": max_jobs,
                "Marker": marker,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=ListJobs&Action=ListJobs",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "MaxJobs": max_jobs,
                "Marker": marker,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=UpdateJob&Action=UpdateJob",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobId": job_id,
                "Manifest": manifest,
                "JobType": job_type,
                "ValidateOnly": validate_only,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "#Operation=UpdateJob&Action=UpdateJob",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=CancelJob&Action=CancelJob",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobId": job_id,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=CancelJob&Action=CancelJob",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=CreateJob&Action=CreateJob",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobType": job_type,
                "Manifest": manifest,
                "ManifestAddendum": manifest_addendum,
                "ValidateOnly": validate_only,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=CreateJob&Action=CreateJob",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=GetShippingLabel&Action=GetShippingLabel",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "jobIds": job_ids,
                "name": name,
                "company": company,
                "phoneNumber": phone_number,
                "country": country,
                "stateOrProvince": state_or_province,
                "city": city,
                "postalCode": postal_code,
                "street1": street1,
                "street2": street2,
                "street3": street3,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=GetShippingLabel&Action=GetShippingLabel",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=GetStatus&Action=GetStatus",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobId": job_id,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=GetStatus&Action=GetStatus",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=ListJobs&Action=ListJobs",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "MaxJobs": max_jobs,
                "Marker": marker,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=ListJobs&Action=ListJobs",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "MaxJobs": max_jobs,
                "Marker": marker,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=UpdateJob&Action=UpdateJob",
            method="GET",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "JobId": job_id,
                "Manifest": manifest,
                "JobType": job_type,
                "ValidateOnly": validate_only,
                "APIVersion": api_version,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "#Operation=UpdateJob&Action=UpdateJob",
            method="POST",
            params={
                "AWSAccessKeyId": aws_access_key_id,
                "Action": action,
                "SignatureMethod": signature_method,
                "SignatureVersion": signature_version,
                "Timestamp": timestamp,
                "Version": version,
                "Signature": signature,
                "Operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
