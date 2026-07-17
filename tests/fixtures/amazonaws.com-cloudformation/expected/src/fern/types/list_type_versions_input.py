

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_type_versions_input_deprecated_status import ListTypeVersionsInputDeprecatedStatus
from .list_type_versions_input_type import ListTypeVersionsInputType


class ListTypeVersionsInput(UniversalBaseModel):
    type: typing_extensions.Annotated[
        typing.Optional[ListTypeVersionsInputType],
        FieldMetadata(alias="Type"),
        pydantic.Field(
            alias="Type",
            description="<p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>",
        ),
    ] = None
    """
    <p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description="<p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>",
        ),
    ] = None
    """
    <p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Arn"),
        pydantic.Field(
            alias="Arn",
            description="<p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>",
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    max_results: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MaxResults"),
        pydantic.Field(
            alias="MaxResults",
            description="The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.",
        ),
    ] = None
    """
    The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.",
        ),
    ] = None
    """
    If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    """

    deprecated_status: typing_extensions.Annotated[
        typing.Optional[ListTypeVersionsInputDeprecatedStatus],
        FieldMetadata(alias="DeprecatedStatus"),
        pydantic.Field(
            alias="DeprecatedStatus",
            description="<p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>",
        ),
    ] = None
    """
    <p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>
    """

    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(
            alias="PublisherId",
            description="<p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>",
        ),
    ] = None
    """
    <p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
