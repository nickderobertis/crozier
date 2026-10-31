

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem(UniversalBaseModel):
    available_payments: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="availablePayments"),
        pydantic.Field(alias="availablePayments", description="Availability of payment."),
    ] = None
    """
    Availability of payment.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description.
    """

    display_document: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="displayDocument"),
        pydantic.Field(alias="displayDocument", description="Indicates whether a document is shown."),
    ] = None
    """
    Indicates whether a document is shown.
    """

    due_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dueDate"),
        pydantic.Field(alias="dueDate", description="Payment due date."),
    ] = None
    """
    Payment due date.
    """

    group_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="groupName"),
        pydantic.Field(alias="groupName", description="Payment group name."),
    ] = None
    """
    Payment group name.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Payment system ID.
    """

    is_custom: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCustom"),
        pydantic.Field(alias="isCustom", description="Indicates whether it is custom."),
    ] = None
    """
    Indicates whether it is custom.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment system name.
    """

    requires_authentication: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="requiresAuthentication"),
        pydantic.Field(alias="requiresAuthentication", description="Indicates whether a authentication is required."),
    ] = None
    """
    Indicates whether a authentication is required.
    """

    requires_document: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="requiresDocument"),
        pydantic.Field(alias="requiresDocument", description="Indicates whether a document is required."),
    ] = None
    """
    Indicates whether a document is required.
    """

    string_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stringId"),
        pydantic.Field(alias="stringId", description="String ID."),
    ] = None
    """
    String ID.
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Template.
    """

    validator: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Payment system validator.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
