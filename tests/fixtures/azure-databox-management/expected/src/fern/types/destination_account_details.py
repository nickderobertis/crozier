

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_account_details_data_destination_type import DestinationAccountDetailsDataDestinationType


class DestinationAccountDetails(UniversalBaseModel):
    """
    Details of the destination storage accounts.
    """

    account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountId"),
        pydantic.Field(alias="accountId", description="Arm Id of the destination where the data has to be moved."),
    ] = None
    """
    Arm Id of the destination where the data has to be moved.
    """

    data_destination_type: typing_extensions.Annotated[
        DestinationAccountDetailsDataDestinationType,
        FieldMetadata(alias="dataDestinationType"),
        pydantic.Field(alias="dataDestinationType", description="Data Destination Type."),
    ]
    """
    Data Destination Type.
    """

    share_password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sharePassword"),
        pydantic.Field(alias="sharePassword", description="Share password to be shared by all shares in SA."),
    ] = None
    """
    Share password to be shared by all shares in SA.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
