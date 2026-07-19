

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .problem_details import ProblemDetails
from .pws_error_data import PwsErrorData


class N2InformationTransferError(UniversalBaseModel):
    error: ProblemDetails
    pwd_error_info: typing_extensions.Annotated[
        typing.Optional[PwsErrorData], FieldMetadata(alias="pwdErrorInfo"), pydantic.Field(alias="pwdErrorInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
