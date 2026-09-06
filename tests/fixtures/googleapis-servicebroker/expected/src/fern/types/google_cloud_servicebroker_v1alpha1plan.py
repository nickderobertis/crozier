

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleCloudServicebrokerV1Alpha1Plan(UniversalBaseModel):
    """
    Plan message describes a Service Plan.
    """

    bindable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether instances of the service can be bound to applications.
    If not specified, `Service.bindable` will be presumed.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the plan. Optional.
    """

    free: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the service is free.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID is a globally unique identifier used to uniquely identify the plan.
    User must make no presumption about the format of this field.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A list of metadata for a service offering.
    Metadata is an arbitrary JSON object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User friendly name of the plan.
    The name must be globally unique within GCP project.
    Note, which is different from ("This must be globally unique within a
    platform marketplace").
    """

    schemas: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Schema definitions for service instances and bindings for the plan.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
