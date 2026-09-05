



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_version import ApiVersion
    from .artifact import Artifact
    from .artifact_list import ArtifactList
    from .bucket_permission_exception import BucketPermissionException
    from .cancel_job_input import CancelJobInput
    from .cancel_job_output import CancelJobOutput
    from .canceled_job_id_exception import CanceledJobIdException
    from .carrier import Carrier
    from .city import City
    from .company import Company
    from .country import Country
    from .create_job_input import CreateJobInput
    from .create_job_output import CreateJobOutput
    from .create_job_quota_exceeded_exception import CreateJobQuotaExceededException
    from .creation_date import CreationDate
    from .current_manifest import CurrentManifest
    from .description import Description
    from .error_count import ErrorCount
    from .error_message import ErrorMessage
    from .expired_job_id_exception import ExpiredJobIdException
    from .generic_string import GenericString
    from .get_cancel_job_request_action import GetCancelJobRequestAction
    from .get_cancel_job_request_operation import GetCancelJobRequestOperation
    from .get_cancel_job_request_version import GetCancelJobRequestVersion
    from .get_create_job_request_action import GetCreateJobRequestAction
    from .get_create_job_request_job_type import GetCreateJobRequestJobType
    from .get_create_job_request_operation import GetCreateJobRequestOperation
    from .get_create_job_request_version import GetCreateJobRequestVersion
    from .get_get_shipping_label_request_action import GetGetShippingLabelRequestAction
    from .get_get_shipping_label_request_operation import GetGetShippingLabelRequestOperation
    from .get_get_shipping_label_request_version import GetGetShippingLabelRequestVersion
    from .get_get_status_request_action import GetGetStatusRequestAction
    from .get_get_status_request_operation import GetGetStatusRequestOperation
    from .get_get_status_request_version import GetGetStatusRequestVersion
    from .get_list_jobs_request_action import GetListJobsRequestAction
    from .get_list_jobs_request_operation import GetListJobsRequestOperation
    from .get_list_jobs_request_version import GetListJobsRequestVersion
    from .get_shipping_label_input import GetShippingLabelInput
    from .get_shipping_label_output import GetShippingLabelOutput
    from .get_status_input import GetStatusInput
    from .get_status_output import GetStatusOutput
    from .get_update_job_request_action import GetUpdateJobRequestAction
    from .get_update_job_request_job_type import GetUpdateJobRequestJobType
    from .get_update_job_request_operation import GetUpdateJobRequestOperation
    from .get_update_job_request_version import GetUpdateJobRequestVersion
    from .invalid_access_key_id_exception import InvalidAccessKeyIdException
    from .invalid_address_exception import InvalidAddressException
    from .invalid_customs_exception import InvalidCustomsException
    from .invalid_file_system_exception import InvalidFileSystemException
    from .invalid_job_id_exception import InvalidJobIdException
    from .invalid_manifest_field_exception import InvalidManifestFieldException
    from .invalid_parameter_exception import InvalidParameterException
    from .invalid_version_exception import InvalidVersionException
    from .is_canceled import IsCanceled
    from .is_truncated import IsTruncated
    from .job import Job
    from .job_id import JobId
    from .job_id_list import JobIdList
    from .job_type import JobType
    from .jobs_list import JobsList
    from .list_jobs_input import ListJobsInput
    from .list_jobs_output import ListJobsOutput
    from .location_code import LocationCode
    from .location_message import LocationMessage
    from .log_bucket import LogBucket
    from .log_key import LogKey
    from .malformed_manifest_exception import MalformedManifestException
    from .manifest import Manifest
    from .manifest_addendum import ManifestAddendum
    from .marker import Marker
    from .max_jobs import MaxJobs
    from .missing_customs_exception import MissingCustomsException
    from .missing_manifest_field_exception import MissingManifestFieldException
    from .missing_parameter_exception import MissingParameterException
    from .multiple_regions_exception import MultipleRegionsException
    from .name import Name
    from .no_such_bucket_exception import NoSuchBucketException
    from .phone_number import PhoneNumber
    from .post_cancel_job_request_action import PostCancelJobRequestAction
    from .post_cancel_job_request_operation import PostCancelJobRequestOperation
    from .post_cancel_job_request_version import PostCancelJobRequestVersion
    from .post_create_job_request_action import PostCreateJobRequestAction
    from .post_create_job_request_operation import PostCreateJobRequestOperation
    from .post_create_job_request_version import PostCreateJobRequestVersion
    from .post_get_shipping_label_request_action import PostGetShippingLabelRequestAction
    from .post_get_shipping_label_request_operation import PostGetShippingLabelRequestOperation
    from .post_get_shipping_label_request_version import PostGetShippingLabelRequestVersion
    from .post_get_status_request_action import PostGetStatusRequestAction
    from .post_get_status_request_operation import PostGetStatusRequestOperation
    from .post_get_status_request_version import PostGetStatusRequestVersion
    from .post_list_jobs_request_action import PostListJobsRequestAction
    from .post_list_jobs_request_operation import PostListJobsRequestOperation
    from .post_list_jobs_request_version import PostListJobsRequestVersion
    from .post_update_job_request_action import PostUpdateJobRequestAction
    from .post_update_job_request_operation import PostUpdateJobRequestOperation
    from .post_update_job_request_version import PostUpdateJobRequestVersion
    from .postal_code import PostalCode
    from .progress_code import ProgressCode
    from .progress_message import ProgressMessage
    from .signature import Signature
    from .signature_file_contents import SignatureFileContents
    from .state_or_province import StateOrProvince
    from .street1 import Street1
    from .street2 import Street2
    from .street3 import Street3
    from .success import Success
    from .tracking_number import TrackingNumber
    from .unable_to_cancel_job_id_exception import UnableToCancelJobIdException
    from .unable_to_update_job_id_exception import UnableToUpdateJobIdException
    from .update_job_input import UpdateJobInput
    from .update_job_output import UpdateJobOutput
    from .url import Url
    from .validate_only import ValidateOnly
    from .warning_message import WarningMessage
_dynamic_imports: typing.Dict[str, str] = {
    "ApiVersion": ".api_version",
    "Artifact": ".artifact",
    "ArtifactList": ".artifact_list",
    "BucketPermissionException": ".bucket_permission_exception",
    "CancelJobInput": ".cancel_job_input",
    "CancelJobOutput": ".cancel_job_output",
    "CanceledJobIdException": ".canceled_job_id_exception",
    "Carrier": ".carrier",
    "City": ".city",
    "Company": ".company",
    "Country": ".country",
    "CreateJobInput": ".create_job_input",
    "CreateJobOutput": ".create_job_output",
    "CreateJobQuotaExceededException": ".create_job_quota_exceeded_exception",
    "CreationDate": ".creation_date",
    "CurrentManifest": ".current_manifest",
    "Description": ".description",
    "ErrorCount": ".error_count",
    "ErrorMessage": ".error_message",
    "ExpiredJobIdException": ".expired_job_id_exception",
    "GenericString": ".generic_string",
    "GetCancelJobRequestAction": ".get_cancel_job_request_action",
    "GetCancelJobRequestOperation": ".get_cancel_job_request_operation",
    "GetCancelJobRequestVersion": ".get_cancel_job_request_version",
    "GetCreateJobRequestAction": ".get_create_job_request_action",
    "GetCreateJobRequestJobType": ".get_create_job_request_job_type",
    "GetCreateJobRequestOperation": ".get_create_job_request_operation",
    "GetCreateJobRequestVersion": ".get_create_job_request_version",
    "GetGetShippingLabelRequestAction": ".get_get_shipping_label_request_action",
    "GetGetShippingLabelRequestOperation": ".get_get_shipping_label_request_operation",
    "GetGetShippingLabelRequestVersion": ".get_get_shipping_label_request_version",
    "GetGetStatusRequestAction": ".get_get_status_request_action",
    "GetGetStatusRequestOperation": ".get_get_status_request_operation",
    "GetGetStatusRequestVersion": ".get_get_status_request_version",
    "GetListJobsRequestAction": ".get_list_jobs_request_action",
    "GetListJobsRequestOperation": ".get_list_jobs_request_operation",
    "GetListJobsRequestVersion": ".get_list_jobs_request_version",
    "GetShippingLabelInput": ".get_shipping_label_input",
    "GetShippingLabelOutput": ".get_shipping_label_output",
    "GetStatusInput": ".get_status_input",
    "GetStatusOutput": ".get_status_output",
    "GetUpdateJobRequestAction": ".get_update_job_request_action",
    "GetUpdateJobRequestJobType": ".get_update_job_request_job_type",
    "GetUpdateJobRequestOperation": ".get_update_job_request_operation",
    "GetUpdateJobRequestVersion": ".get_update_job_request_version",
    "InvalidAccessKeyIdException": ".invalid_access_key_id_exception",
    "InvalidAddressException": ".invalid_address_exception",
    "InvalidCustomsException": ".invalid_customs_exception",
    "InvalidFileSystemException": ".invalid_file_system_exception",
    "InvalidJobIdException": ".invalid_job_id_exception",
    "InvalidManifestFieldException": ".invalid_manifest_field_exception",
    "InvalidParameterException": ".invalid_parameter_exception",
    "InvalidVersionException": ".invalid_version_exception",
    "IsCanceled": ".is_canceled",
    "IsTruncated": ".is_truncated",
    "Job": ".job",
    "JobId": ".job_id",
    "JobIdList": ".job_id_list",
    "JobType": ".job_type",
    "JobsList": ".jobs_list",
    "ListJobsInput": ".list_jobs_input",
    "ListJobsOutput": ".list_jobs_output",
    "LocationCode": ".location_code",
    "LocationMessage": ".location_message",
    "LogBucket": ".log_bucket",
    "LogKey": ".log_key",
    "MalformedManifestException": ".malformed_manifest_exception",
    "Manifest": ".manifest",
    "ManifestAddendum": ".manifest_addendum",
    "Marker": ".marker",
    "MaxJobs": ".max_jobs",
    "MissingCustomsException": ".missing_customs_exception",
    "MissingManifestFieldException": ".missing_manifest_field_exception",
    "MissingParameterException": ".missing_parameter_exception",
    "MultipleRegionsException": ".multiple_regions_exception",
    "Name": ".name",
    "NoSuchBucketException": ".no_such_bucket_exception",
    "PhoneNumber": ".phone_number",
    "PostCancelJobRequestAction": ".post_cancel_job_request_action",
    "PostCancelJobRequestOperation": ".post_cancel_job_request_operation",
    "PostCancelJobRequestVersion": ".post_cancel_job_request_version",
    "PostCreateJobRequestAction": ".post_create_job_request_action",
    "PostCreateJobRequestOperation": ".post_create_job_request_operation",
    "PostCreateJobRequestVersion": ".post_create_job_request_version",
    "PostGetShippingLabelRequestAction": ".post_get_shipping_label_request_action",
    "PostGetShippingLabelRequestOperation": ".post_get_shipping_label_request_operation",
    "PostGetShippingLabelRequestVersion": ".post_get_shipping_label_request_version",
    "PostGetStatusRequestAction": ".post_get_status_request_action",
    "PostGetStatusRequestOperation": ".post_get_status_request_operation",
    "PostGetStatusRequestVersion": ".post_get_status_request_version",
    "PostListJobsRequestAction": ".post_list_jobs_request_action",
    "PostListJobsRequestOperation": ".post_list_jobs_request_operation",
    "PostListJobsRequestVersion": ".post_list_jobs_request_version",
    "PostUpdateJobRequestAction": ".post_update_job_request_action",
    "PostUpdateJobRequestOperation": ".post_update_job_request_operation",
    "PostUpdateJobRequestVersion": ".post_update_job_request_version",
    "PostalCode": ".postal_code",
    "ProgressCode": ".progress_code",
    "ProgressMessage": ".progress_message",
    "Signature": ".signature",
    "SignatureFileContents": ".signature_file_contents",
    "StateOrProvince": ".state_or_province",
    "Street1": ".street1",
    "Street2": ".street2",
    "Street3": ".street3",
    "Success": ".success",
    "TrackingNumber": ".tracking_number",
    "UnableToCancelJobIdException": ".unable_to_cancel_job_id_exception",
    "UnableToUpdateJobIdException": ".unable_to_update_job_id_exception",
    "UpdateJobInput": ".update_job_input",
    "UpdateJobOutput": ".update_job_output",
    "Url": ".url",
    "ValidateOnly": ".validate_only",
    "WarningMessage": ".warning_message",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "ApiVersion",
    "Artifact",
    "ArtifactList",
    "BucketPermissionException",
    "CancelJobInput",
    "CancelJobOutput",
    "CanceledJobIdException",
    "Carrier",
    "City",
    "Company",
    "Country",
    "CreateJobInput",
    "CreateJobOutput",
    "CreateJobQuotaExceededException",
    "CreationDate",
    "CurrentManifest",
    "Description",
    "ErrorCount",
    "ErrorMessage",
    "ExpiredJobIdException",
    "GenericString",
    "GetCancelJobRequestAction",
    "GetCancelJobRequestOperation",
    "GetCancelJobRequestVersion",
    "GetCreateJobRequestAction",
    "GetCreateJobRequestJobType",
    "GetCreateJobRequestOperation",
    "GetCreateJobRequestVersion",
    "GetGetShippingLabelRequestAction",
    "GetGetShippingLabelRequestOperation",
    "GetGetShippingLabelRequestVersion",
    "GetGetStatusRequestAction",
    "GetGetStatusRequestOperation",
    "GetGetStatusRequestVersion",
    "GetListJobsRequestAction",
    "GetListJobsRequestOperation",
    "GetListJobsRequestVersion",
    "GetShippingLabelInput",
    "GetShippingLabelOutput",
    "GetStatusInput",
    "GetStatusOutput",
    "GetUpdateJobRequestAction",
    "GetUpdateJobRequestJobType",
    "GetUpdateJobRequestOperation",
    "GetUpdateJobRequestVersion",
    "InvalidAccessKeyIdException",
    "InvalidAddressException",
    "InvalidCustomsException",
    "InvalidFileSystemException",
    "InvalidJobIdException",
    "InvalidManifestFieldException",
    "InvalidParameterException",
    "InvalidVersionException",
    "IsCanceled",
    "IsTruncated",
    "Job",
    "JobId",
    "JobIdList",
    "JobType",
    "JobsList",
    "ListJobsInput",
    "ListJobsOutput",
    "LocationCode",
    "LocationMessage",
    "LogBucket",
    "LogKey",
    "MalformedManifestException",
    "Manifest",
    "ManifestAddendum",
    "Marker",
    "MaxJobs",
    "MissingCustomsException",
    "MissingManifestFieldException",
    "MissingParameterException",
    "MultipleRegionsException",
    "Name",
    "NoSuchBucketException",
    "PhoneNumber",
    "PostCancelJobRequestAction",
    "PostCancelJobRequestOperation",
    "PostCancelJobRequestVersion",
    "PostCreateJobRequestAction",
    "PostCreateJobRequestOperation",
    "PostCreateJobRequestVersion",
    "PostGetShippingLabelRequestAction",
    "PostGetShippingLabelRequestOperation",
    "PostGetShippingLabelRequestVersion",
    "PostGetStatusRequestAction",
    "PostGetStatusRequestOperation",
    "PostGetStatusRequestVersion",
    "PostListJobsRequestAction",
    "PostListJobsRequestOperation",
    "PostListJobsRequestVersion",
    "PostUpdateJobRequestAction",
    "PostUpdateJobRequestOperation",
    "PostUpdateJobRequestVersion",
    "PostalCode",
    "ProgressCode",
    "ProgressMessage",
    "Signature",
    "SignatureFileContents",
    "StateOrProvince",
    "Street1",
    "Street2",
    "Street3",
    "Success",
    "TrackingNumber",
    "UnableToCancelJobIdException",
    "UnableToUpdateJobIdException",
    "UpdateJobInput",
    "UpdateJobOutput",
    "Url",
    "ValidateOnly",
    "WarningMessage",
]
