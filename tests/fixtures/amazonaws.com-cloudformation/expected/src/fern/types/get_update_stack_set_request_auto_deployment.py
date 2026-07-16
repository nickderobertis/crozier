

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetUpdateStackSetRequestAutoDeployment(UniversalBaseModel):
    """
    [Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU).
    """

    enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="Enabled")] = pydantic.Field(
        default=None
    )
    """
    If set to <code>true</code>, StackSets automatically deploys additional stack instances to Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.
    """

    retain_stacks_on_account_removal: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="RetainStacksOnAccountRemoval")
    ] = pydantic.Field(default=None)
    """
    If set to <code>true</code>, stack resources are retained when an account is removed from a target organization or OU. If set to <code>false</code>, stack resources are deleted. Specify only if <code>Enabled</code> is set to <code>True</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
