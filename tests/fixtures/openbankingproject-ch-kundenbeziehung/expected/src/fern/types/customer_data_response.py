

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CustomerDataResponse(UniversalBaseModel):
    available_modules: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="availableModules"),
        pydantic.Field(alias="availableModules"),
    ] = None
    module_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="moduleData"),
        pydantic.Field(alias="moduleData", description="Bereitgestellte Datenbausteine"),
    ] = None
    """
    Bereitgestellte Datenbausteine
    """

    verification_status: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="verificationStatus"),
        pydantic.Field(alias="verificationStatus"),
    ] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
