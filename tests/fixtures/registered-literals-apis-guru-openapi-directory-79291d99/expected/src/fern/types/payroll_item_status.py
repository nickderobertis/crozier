

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayrollItemStatus(UniversalBaseModel):
    """
    Details about the status of the payroll item.
    """

    processing_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Denotes the processing status for the verification.
    
    `UNKNOWN`: The processing status could not be determined.
    
    `PROCESSING_COMPLETE`: The processing has completed and the user has approved for sharing. The data is available to be retrieved.
    
    `PROCESSING`: The verification is still processing. The data is not available yet.
    
    `FAILED`: The processing failed to complete successfully.
    
    `APPROVAL_STATUS_PENDING`: The processing has completed but the user has not yet approved the sharing of the data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
