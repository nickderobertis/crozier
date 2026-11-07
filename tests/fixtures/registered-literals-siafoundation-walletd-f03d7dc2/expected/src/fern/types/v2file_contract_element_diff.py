

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2file_contract_element import V2FileContractElement
from .v2file_contract_element_diff_resolution import V2FileContractElementDiffResolution
from .v2file_contract_element_diff_revision import V2FileContractElementDiffRevision


class V2FileContractElementDiff(UniversalBaseModel):
    v2file_contract_element: typing_extensions.Annotated[
        V2FileContractElement,
        FieldMetadata(alias="v2FileContractElement"),
        pydantic.Field(alias="v2FileContractElement"),
    ]
    created: bool
    revision: typing.Optional[V2FileContractElementDiffRevision] = None
    resolution: typing.Optional[V2FileContractElementDiffResolution] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
