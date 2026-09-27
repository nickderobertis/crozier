

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_grpc_services_response_item_methods_item import PutMockserverGrpcServicesResponseItemMethodsItem


class PutMockserverGrpcServicesResponseItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    methods: typing.Optional[typing.List[PutMockserverGrpcServicesResponseItemMethodsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
