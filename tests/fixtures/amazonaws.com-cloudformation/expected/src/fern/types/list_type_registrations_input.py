

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_type_registrations_input_registration_status_filter import ListTypeRegistrationsInputRegistrationStatusFilter
from .list_type_registrations_input_type import ListTypeRegistrationsInputType


class ListTypeRegistrationsInput(UniversalBaseModel):
    type: typing_extensions.Annotated[typing.Optional[ListTypeRegistrationsInputType], FieldMetadata(alias="Type")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeName")] = pydantic.Field(
        default=None
    )
    """
    <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    type_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeArn")] = pydantic.Field(
        default=None
    )
    """
    <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    registration_status_filter: typing_extensions.Annotated[
        typing.Optional[ListTypeRegistrationsInputRegistrationStatusFilter],
        FieldMetadata(alias="RegistrationStatusFilter"),
    ] = pydantic.Field(default=None)
    """
    <p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>
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
