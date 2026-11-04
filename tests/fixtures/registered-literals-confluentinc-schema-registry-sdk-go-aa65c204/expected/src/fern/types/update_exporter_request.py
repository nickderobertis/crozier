

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_exporter_request_context_type import UpdateExporterRequestContextType


class UpdateExporterRequest(UniversalBaseModel):
    subjects: typing.Optional[typing.List[str]] = None
    context_type: typing_extensions.Annotated[
        typing.Optional[UpdateExporterRequestContextType],
        FieldMetadata(alias="contextType"),
        pydantic.Field(alias="contextType"),
    ] = None
    context: typing.Optional[str] = None
    kek_rename_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kekRenameFormat"), pydantic.Field(alias="kekRenameFormat")
    ] = None
    subject_rename_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="subjectRenameFormat"), pydantic.Field(alias="subjectRenameFormat")
    ] = None
    config: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
