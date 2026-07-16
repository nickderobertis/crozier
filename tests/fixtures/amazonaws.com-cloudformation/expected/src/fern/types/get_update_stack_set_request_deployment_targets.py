

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account import Account
from .get_update_stack_set_request_deployment_targets_account_filter_type import (
    GetUpdateStackSetRequestDeploymentTargetsAccountFilterType,
)
from .organizational_unit_id import OrganizationalUnitId


class GetUpdateStackSetRequestDeploymentTargets(UniversalBaseModel):
    """
    <p>[Service-managed permissions] The Organizations accounts to which StackSets deploys. StackSets doesn't deploy stack instances to the organization management account, even if the organization management account is in your organization or in an OU in your organization.</p> <p>For update operations, you can specify either <code>Accounts</code> or <code>OrganizationalUnitIds</code>. For create and delete operations, specify <code>OrganizationalUnitIds</code>.</p>
    """

    accounts: typing_extensions.Annotated[typing.Optional[typing.List[Account]], FieldMetadata(alias="Accounts")] = (
        pydantic.Field(default=None)
    )
    """
    The names of one or more Amazon Web Services accounts for which you want to deploy stack set updates.
    """

    accounts_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="AccountsUrl")] = (
        pydantic.Field(default=None)
    )
    """
    Returns the value of the <code>AccountsUrl</code> property.
    """

    organizational_unit_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[OrganizationalUnitId]], FieldMetadata(alias="OrganizationalUnitIds")
    ] = pydantic.Field(default=None)
    """
    The organization root ID or organizational unit (OU) IDs to which StackSets deploys.
    """

    account_filter_type: typing_extensions.Annotated[
        typing.Optional[GetUpdateStackSetRequestDeploymentTargetsAccountFilterType],
        FieldMetadata(alias="AccountFilterType"),
    ] = pydantic.Field(default=None)
    """
    <p>Limit deployment targets to individual accounts or include additional accounts with provided OUs.</p> <p>The following is a list of possible values for the <code>AccountFilterType</code> operation.</p> <ul> <li> <p> <code>INTERSECTION</code>: StackSets deploys to the accounts specified in <code>Accounts</code> parameter. </p> </li> <li> <p> <code>DIFFERENCE</code>: StackSets excludes the accounts specified in <code>Accounts</code> parameter. This enables user to avoid certain accounts within an OU such as suspended accounts.</p> </li> <li> <p> <code>UNION</code>: StackSets includes additional accounts deployment targets. </p> <p>This is the default value if <code>AccountFilterType</code> is not provided. This enables user to update an entire OU and individual accounts from a different OU in one request, which used to be two separate requests.</p> </li> <li> <p> <code>NONE</code>: Deploys to all the accounts in specified organizational units (OU).</p> </li> </ul>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
