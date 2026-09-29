

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Investigation(UniversalBaseModel):
    child_documents: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="_childDocuments_"),
        pydantic.Field(alias="_childDocuments_"),
    ] = None
    assay: typing.Optional[str] = None
    document_uuid: typing.Optional[str] = None
    effectendpoint: typing.Optional[str] = None
    endpoint: typing.Optional[str] = None
    endpointcategory: typing.Optional[str] = None
    err: typing.Optional[float] = None
    err_qualifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errQualifier"), pydantic.Field(alias="errQualifier")
    ] = None
    guidance: typing.Optional[str] = None
    investigation: typing.Optional[str] = None
    lo_qualifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="loQualifier"), pydantic.Field(alias="loQualifier")
    ] = None
    lo_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="loValue"), pydantic.Field(alias="loValue")
    ] = None
    name: typing.Optional[str] = None
    owner_name: typing.Optional[str] = None
    publicname: typing.Optional[str] = None
    reference: typing.Optional[str] = None
    reference_owner: typing.Optional[str] = None
    reference_year: typing.Optional[str] = None
    resulttype: typing.Optional[str] = None
    s_uuid: typing.Optional[str] = None
    study_result_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="studyResultType"), pydantic.Field(alias="studyResultType")
    ] = None
    substance_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="substanceType"), pydantic.Field(alias="substanceType")
    ] = None
    text_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="textValue"), pydantic.Field(alias="textValue")
    ] = None
    topcategory: typing.Optional[str] = None
    type_s: typing.Optional[str] = None
    unit: typing.Optional[str] = None
    up_qualifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="upQualifier"), pydantic.Field(alias="upQualifier")
    ] = None
    up_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="upValue"), pydantic.Field(alias="upValue")
    ] = None
    updated: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
