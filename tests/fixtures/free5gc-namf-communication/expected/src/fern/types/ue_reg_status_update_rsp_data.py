

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UeRegStatusUpdateRspData(UniversalBaseModel):
    reg_status_transfer_complete: typing_extensions.Annotated[
        bool, FieldMetadata(alias="regStatusTransferComplete"), pydantic.Field(alias="regStatusTransferComplete")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
