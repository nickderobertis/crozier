

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .grouped_project_documents_upload_date import GroupedProjectDocumentsUploadDate
from .project_document import ProjectDocument


class GroupedProjectDocuments(UniversalBaseModel):
    documents: typing.List[ProjectDocument]
    upload_date: GroupedProjectDocumentsUploadDate

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
