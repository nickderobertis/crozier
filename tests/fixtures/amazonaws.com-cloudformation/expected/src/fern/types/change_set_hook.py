

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_set_hook_failure_mode import ChangeSetHookFailureMode
from .change_set_hook_invocation_point import ChangeSetHookInvocationPoint
from .change_set_hook_target_details import ChangeSetHookTargetDetails


class ChangeSetHook(UniversalBaseModel):
    """
    Specifies the resource, the hook, and the hook version to be invoked.
    """

    invocation_point: typing_extensions.Annotated[
        typing.Optional[ChangeSetHookInvocationPoint], FieldMetadata(alias="InvocationPoint")
    ] = pydantic.Field(default=None)
    """
    Specifies the points in provisioning logic where a hook is invoked.
    """

    failure_mode: typing_extensions.Annotated[
        typing.Optional[ChangeSetHookFailureMode], FieldMetadata(alias="FailureMode")
    ] = pydantic.Field(default=None)
    """
    <p>Specify the hook failure mode for non-compliant resources in the followings ways.</p> <ul> <li> <p> <code>FAIL</code> Stops provisioning resources.</p> </li> <li> <p> <code>WARN</code> Allows provisioning to continue with a warning message.</p> </li> </ul>
    """

    type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeName")] = pydantic.Field(
        default=None
    )
    """
    <p>The unique name for your hook. Specifies a three-part namespace for your hook, with a recommended pattern of <code>Organization::Service::Hook</code>.</p> <note> <p>The following organization namespaces are reserved and can't be used in your hook type names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>ASK</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>
    """

    type_version_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeVersionId")] = (
        pydantic.Field(default=None)
    )
    """
    The version ID of the type specified.
    """

    type_configuration_version_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="TypeConfigurationVersionId")
    ] = pydantic.Field(default=None)
    """
    The version ID of the type configuration.
    """

    target_details: typing_extensions.Annotated[
        typing.Optional[ChangeSetHookTargetDetails], FieldMetadata(alias="TargetDetails")
    ] = pydantic.Field(default=None)
    """
    Specifies details about the target that the hook will run against.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
