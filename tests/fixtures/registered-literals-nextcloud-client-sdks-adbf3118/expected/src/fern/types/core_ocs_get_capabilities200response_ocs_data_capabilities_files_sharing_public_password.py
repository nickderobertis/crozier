

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicPassword(UniversalBaseModel):
    enforced: bool
    ask_for_optional_password: typing_extensions.Annotated[
        bool, FieldMetadata(alias="askForOptionalPassword"), pydantic.Field(alias="askForOptionalPassword")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
