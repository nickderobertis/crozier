

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_account_details import DestinationAccountDetails
from .update_job_details import UpdateJobDetails


class UpdateJobProperties(UniversalBaseModel):
    """
    Job Properties for update
    """

    destination_account_details: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinationAccountDetails]],
        FieldMetadata(alias="destinationAccountDetails"),
        pydantic.Field(alias="destinationAccountDetails", description="Destination account details."),
    ] = None
    """
    Destination account details.
    """

    details: typing.Optional[UpdateJobDetails] = pydantic.Field(default=None)
    """
    Details of a job to be updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
