

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ace import Ace
from .workflow_parameter import WorkflowParameter


class Workflow(UniversalBaseModel):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="_id"), pydantic.Field(alias="_id")]
    name: str
    created: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="_created"), pydantic.Field(alias="_created")]
    createdby: typing_extensions.Annotated[str, FieldMetadata(alias="_createdby"), pydantic.Field(alias="_createdby")]
    createdbyid: typing_extensions.Annotated[
        str, FieldMetadata(alias="_createdbyid"), pydantic.Field(alias="_createdbyid")
    ]
    modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="_modified"), pydantic.Field(alias="_modified")
    ]
    modifiedby: typing_extensions.Annotated[
        str, FieldMetadata(alias="_modifiedby"), pydantic.Field(alias="_modifiedby")
    ]
    modifiedbyid: typing_extensions.Annotated[
        str, FieldMetadata(alias="_modifiedbyid"), pydantic.Field(alias="_modifiedbyid")
    ]
    type: typing_extensions.Annotated[str, FieldMetadata(alias="_type"), pydantic.Field(alias="_type")]
    acl: typing_extensions.Annotated[typing.List[Ace], FieldMetadata(alias="_acl"), pydantic.Field(alias="_acl")]
    name: typing_extensions.Annotated[str, FieldMetadata(alias="_name"), pydantic.Field(alias="_name")]
    encrypt: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="_encrypt"), pydantic.Field(alias="_encrypt")
    ]
    version: typing_extensions.Annotated[float, FieldMetadata(alias="_version"), pydantic.Field(alias="_version")]
    parameters: typing_extensions.Annotated[
        typing.List[WorkflowParameter], FieldMetadata(alias="Parameters"), pydantic.Field(alias="Parameters")
    ]
    background: bool
    serializable: typing_extensions.Annotated[
        bool, FieldMetadata(alias="Serializable"), pydantic.Field(alias="Serializable")
    ]
    filename: typing_extensions.Annotated[str, FieldMetadata(alias="Filename"), pydantic.Field(alias="Filename")]
    projectandname: str
    xaml: typing_extensions.Annotated[str, FieldMetadata(alias="Xaml"), pydantic.Field(alias="Xaml")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
