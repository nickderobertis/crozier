

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReimbursementType(UniversalBaseModel):
    account_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AccountCode"),
        pydantic.Field(alias="AccountCode", description="See Accounts"),
    ] = None
    """
    See Accounts
    """

    current_record: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="CurrentRecord"),
        pydantic.Field(alias="CurrentRecord", description="Is the current record"),
    ] = None
    """
    Is the current record
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Name of the earnings rate (max length = 100)"),
    ] = None
    """
    Name of the earnings rate (max length = 100)
    """

    reimbursement_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReimbursementTypeID"),
        pydantic.Field(alias="ReimbursementTypeID", description="Xero identifier"),
    ] = None
    """
    Xero identifier
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
