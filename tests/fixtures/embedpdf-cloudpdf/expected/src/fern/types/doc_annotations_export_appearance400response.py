

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_export_appearance400response_code import DocAnnotationsExportAppearance400ResponseCode
from .doc_annotations_export_appearance400response_name import DocAnnotationsExportAppearance400ResponseName


class DocAnnotationsExportAppearance400Response(UniversalBaseModel):
    name: DocAnnotationsExportAppearance400ResponseName
    code: DocAnnotationsExportAppearance400ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
