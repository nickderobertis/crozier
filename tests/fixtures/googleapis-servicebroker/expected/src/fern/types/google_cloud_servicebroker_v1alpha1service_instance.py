

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GoogleCloudServicebrokerV1Alpha1ServiceInstance(UniversalBaseModel):
    """
    Message describing inputs to Provision and Update Service instance requests.
    """

    context: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Platform specific contextual information under which the service instance
    is to be provisioned. This replaces organization_guid and space_guid.
    But can also contain anything.
    Currently only used for logging context information.
    """

    create_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createTime"),
        pydantic.Field(alias="createTime", description="Output only. Timestamp for when the instance was created."),
    ] = None
    """
    Output only. Timestamp for when the instance was created.
    """

    deployment_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deploymentName"),
        pydantic.Field(
            alias="deploymentName",
            description="Output only. Name of the Deployment Manager deployment used for provisioning of this\nservice instance.",
        ),
    ] = None
    """
    Output only. Name of the Deployment Manager deployment used for provisioning of this
    service instance.
    """

    instance_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the service instance. Must be unique within GCP project.
    Maximum length is 64, GUID recommended.
    Required.
    """

    organization_guid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The platform GUID for the organization under which the service is to be
    provisioned.
    Required.
    """

    parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Configuration options for the service instance.
    Parameters is JSON object serialized to string.
    """

    plan_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the plan. See `Service` and `Plan` resources for details.
    Maximum length is 64, GUID recommended.
    Required.
    """

    previous_values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Used only in UpdateServiceInstance request to optionally specify previous
    fields.
    """

    resource_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceName"),
        pydantic.Field(
            alias="resourceName",
            description="Output only. The resource name of the instance, e.g.\nprojects/project_id/brokers/broker_id/service_instances/instance_id",
        ),
    ] = None
    """
    Output only. The resource name of the instance, e.g.
    projects/project_id/brokers/broker_id/service_instances/instance_id
    """

    service_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the service. Must be a valid identifier of a service
    contained in the list from a `ListServices()` call.
    Maximum length is 64, GUID recommended.
    Required.
    """

    space_guid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier for the project space within the platform organization.
    Required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
