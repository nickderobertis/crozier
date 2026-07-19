

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n1n2msg_txfr_err_detail import N1N2MsgTxfrErrDetail
from .problem_details import ProblemDetails


class N1N2MessageTransferError(UniversalBaseModel):
    error: ProblemDetails
    err_info: typing_extensions.Annotated[
        typing.Optional[N1N2MsgTxfrErrDetail], FieldMetadata(alias="errInfo"), pydantic.Field(alias="errInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
