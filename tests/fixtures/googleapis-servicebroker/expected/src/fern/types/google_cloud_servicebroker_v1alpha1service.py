

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .google_cloud_servicebroker_v1alpha1dashboard_client import GoogleCloudServicebrokerV1Alpha1DashboardClient
from .google_cloud_servicebroker_v1alpha1plan import GoogleCloudServicebrokerV1Alpha1Plan


class GoogleCloudServicebrokerV1Alpha1Service(UniversalBaseModel):
    """
    The resource model mostly follows the Open Service Broker API, as
    described here:
    https://github.com/openservicebrokerapi/servicebroker/blob/master/_spec.md
    Though due to Google Specifics it has additional optional fields.
    """

    bindable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether instances of the service can be bound to applications.
    Required.
    """

    binding_retrievable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the service provides an endpoint to get service bindings.
    """

    dashboard_client: typing.Optional[GoogleCloudServicebrokerV1Alpha1DashboardClient] = pydantic.Field(default=None)
    """
    Information to activate Dashboard SSO feature.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the service. Required.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID is a globally unique identifier used to uniquely identify the service.
    ID is an opaque string.
    """

    instance_retrievable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the service provides an endpoint to get service instances.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A list of metadata for a service offering.
    Metadata is an arbitrary JSON object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User friendly service name.
    Name must match [a-z0-9]+ regexp.
    The name must be globally unique within GCP project.
    Note, which is different from ("This must be globally unique within a
    platform marketplace").
    Required.
    """

    plan_updateable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the service supports upgrade/downgrade for some plans.
    """

    plans: typing.Optional[typing.List[GoogleCloudServicebrokerV1Alpha1Plan]] = pydantic.Field(default=None)
    """
    A list of plans for this service.
    At least one plan is required.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags provide a flexible mechanism to expose a classification, attribute, or
    base technology of a service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
