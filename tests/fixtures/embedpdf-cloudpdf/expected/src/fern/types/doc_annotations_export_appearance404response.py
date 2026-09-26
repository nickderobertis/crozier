

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_export_appearance404response_code import DocAnnotationsExportAppearance404ResponseCode
from .doc_annotations_export_appearance404response_name import DocAnnotationsExportAppearance404ResponseName


class DocAnnotationsExportAppearance404Response(UniversalBaseModel):
    name: DocAnnotationsExportAppearance404ResponseName
    code: DocAnnotationsExportAppearance404ResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
