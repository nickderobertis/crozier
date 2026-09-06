

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_package_report import UpdateSystemModelsPackageReport


class UpdateSystemModelsClientInfo(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientID"),
        pydantic.Field(alias="ClientID", description="The id of the client"),
    ] = None
    """
    The id of the client
    """

    package: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsPackageReport]],
        FieldMetadata(alias="Package"),
        pydantic.Field(alias="Package", description="The packages"),
    ] = None
    """
    The packages
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
