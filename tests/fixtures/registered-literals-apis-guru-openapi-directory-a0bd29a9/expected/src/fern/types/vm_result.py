

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .provisioning_status_result import ProvisioningStatusResult
from .vm_connection_info import VmConnectionInfo
from .vm_status import VmStatus


class VmResult(UniversalBaseModel):
    connection: typing.Optional[VmConnectionInfo] = None
    provisioning_status: typing_extensions.Annotated[
        typing.Optional[ProvisioningStatusResult],
        FieldMetadata(alias="provisioningStatus"),
        pydantic.Field(alias="provisioningStatus"),
    ] = None
    status: typing.Optional[VmStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
