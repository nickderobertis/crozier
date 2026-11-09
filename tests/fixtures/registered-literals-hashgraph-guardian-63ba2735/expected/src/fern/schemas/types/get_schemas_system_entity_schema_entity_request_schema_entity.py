

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSchemasSystemEntitySchemaEntityRequestSchemaEntity(enum.StrEnum):
    STANDARD_REGISTRY = "STANDARD_REGISTRY"
    USER = "USER"
    POLICY = "POLICY"
    MINT_TOKEN = "MINT_TOKEN"
    WIPE_TOKEN = "WIPE_TOKEN"
    MINT_NFTOKEN = "MINT_NFTOKEN"

    def visit(
        self,
        standard_registry: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        policy: typing.Callable[[], T_Result],
        mint_token: typing.Callable[[], T_Result],
        wipe_token: typing.Callable[[], T_Result],
        mint_nftoken: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSchemasSystemEntitySchemaEntityRequestSchemaEntity.STANDARD_REGISTRY:
            return standard_registry()
        if self is GetSchemasSystemEntitySchemaEntityRequestSchemaEntity.USER:
            return user()
        if self is GetSchemasSystemEntitySchemaEntityRequestSchemaEntity.POLICY:
            return policy()
        if self is GetSchemasSystemEntitySchemaEntityRequestSchemaEntity.MINT_TOKEN:
            return mint_token()
        if self is GetSchemasSystemEntitySchemaEntityRequestSchemaEntity.WIPE_TOKEN:
            return wipe_token()
        if self is GetSchemasSystemEntitySchemaEntityRequestSchemaEntity.MINT_NFTOKEN:
            return mint_nftoken()
