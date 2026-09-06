

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GoogleCloudServicebrokerV1Alpha1Binding(UniversalBaseModel):
    """
    Describes the binding.
    """

    bind_resource: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A JSON object that contains data for platform resources associated with
    the binding to be created.
    """

    binding_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the binding. Must be unique within GCP project.
    Maximum length is 64, GUID recommended.
    Required.
    """

    create_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createTime"),
        pydantic.Field(alias="createTime", description="Output only. Timestamp for when the binding was created."),
    ] = None
    """
    Output only. Timestamp for when the binding was created.
    """

    parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Configuration options for the service binding.
    """

    plan_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the plan. See `Service` and `Plan` resources for details.
    Maximum length is 64, GUID recommended.
    Required.
    """

    service_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the service. Must be a valid identifier of a service
    contained in the list from a `ListServices()` call.
    Maximum length is 64, GUID recommended.
    Required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
