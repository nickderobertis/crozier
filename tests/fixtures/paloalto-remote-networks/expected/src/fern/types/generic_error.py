

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_detail_cause_infos import ErrorDetailCauseInfos


class GenericError(UniversalBaseModel):
    errors: typing_extensions.Annotated[
        typing.Optional[ErrorDetailCauseInfos], FieldMetadata(alias="_errors"), pydantic.Field(alias="_errors")
    ] = None
    request_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_request_id"), pydantic.Field(alias="_request_id")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
