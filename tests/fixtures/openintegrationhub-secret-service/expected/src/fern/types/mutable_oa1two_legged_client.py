

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mutable_oa1two_legged_client_type import MutableOa1TwoLeggedClientType
from .owner import Owner


class MutableOa1TwoLeggedClient(UniversalBaseModel):
    name: str
    owners: typing.List[Owner]
    type: MutableOa1TwoLeggedClientType
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    consumer_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="consumerKey"), pydantic.Field(alias="consumerKey")
    ]
    consumer_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="consumerSecret"), pydantic.Field(alias="consumerSecret")
    ]
    nonce: str
    signature: str
    signature_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="signatureMethod"), pydantic.Field(alias="signatureMethod")
    ]
    verifier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
