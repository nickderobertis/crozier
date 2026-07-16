

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_types_input_deprecated_status import ListTypesInputDeprecatedStatus
from .list_types_input_filters import ListTypesInputFilters
from .list_types_input_provisioning_type import ListTypesInputProvisioningType
from .list_types_input_type import ListTypesInputType
from .list_types_input_visibility import ListTypesInputVisibility


class ListTypesInput(UniversalBaseModel):
    visibility: typing_extensions.Annotated[
        typing.Optional[ListTypesInputVisibility], FieldMetadata(alias="Visibility")
    ] = pydantic.Field(default=None)
    """
    <p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and region.</p> </li> <li> <p>Public extensions that you have activated in this account and region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>
    """

    provisioning_type: typing_extensions.Annotated[
        typing.Optional[ListTypesInputProvisioningType], FieldMetadata(alias="ProvisioningType")
    ] = pydantic.Field(default=None)
    """
    <p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>
    """

    deprecated_status: typing_extensions.Annotated[
        typing.Optional[ListTypesInputDeprecatedStatus], FieldMetadata(alias="DeprecatedStatus")
    ] = pydantic.Field(default=None)
    """
    <p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>
    """

    type: typing_extensions.Annotated[typing.Optional[ListTypesInputType], FieldMetadata(alias="Type")] = (
        pydantic.Field(default=None)
    )
    """
    The type of extension.
    """

    filters: typing_extensions.Annotated[typing.Optional[ListTypesInputFilters], FieldMetadata(alias="Filters")] = (
        pydantic.Field(default=None)
    )
    """
    <p>Filter criteria to use in determining which extensions to return.</p> <p>Filters must be compatible with <code>Visibility</code> to return valid results. For example, specifying <code>AWS_TYPES</code> for <code>Category</code> and <code>PRIVATE</code> for <code>Visibility</code> returns an empty list of types, but specifying <code>PUBLIC</code> for <code>Visibility</code> returns the desired list.</p>
    """

    max_results: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="MaxResults")] = pydantic.Field(
        default=None
    )
    """
    The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
