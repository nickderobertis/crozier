

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_contract_element import FileContractElement
from .file_contract_element_diff_revision import FileContractElementDiffRevision


class FileContractElementDiff(UniversalBaseModel):
    file_contract_element: typing_extensions.Annotated[
        FileContractElement, FieldMetadata(alias="fileContractElement"), pydantic.Field(alias="fileContractElement")
    ]
    created: bool
    revision: typing.Optional[FileContractElementDiffRevision] = None
    resolved: bool
    valid: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
