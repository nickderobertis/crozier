

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExportReadyResponse(UniversalBaseModel):
    export_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="export-uri"),
        pydantic.Field(alias="export-uri", description="A unique URL. Should be a short-lived resource."),
    ] = None
    """
    A unique URL. Should be a short-lived resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
