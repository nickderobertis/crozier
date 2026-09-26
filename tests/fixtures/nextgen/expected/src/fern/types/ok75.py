

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok75(UniversalBaseModel):
    drug_name: typing_extensions.Annotated[str, FieldMetadata(alias="drugName"), pydantic.Field(alias="drugName")]
    medication_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicationName"), pydantic.Field(alias="medicationName")
    ]
    gcn_sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="gcnSequenceNumber"), pydantic.Field(alias="gcnSequenceNumber")
    ]
    monograph_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="monographCode"), pydantic.Field(alias="monographCode")
    ]
    monograph: typing.List[str]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
