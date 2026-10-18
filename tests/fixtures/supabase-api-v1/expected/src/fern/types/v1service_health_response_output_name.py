

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ServiceHealthResponseOutputName(enum.StrEnum):
    AUTH = "auth"
    DB = "db"
    DB_POSTGRES_USER = "db_postgres_user"
    POOLER = "pooler"
    REALTIME = "realtime"
    REST = "rest"
    STORAGE = "storage"
    PG_BOUNCER = "pg_bouncer"

    def visit(
        self,
        auth: typing.Callable[[], T_Result],
        db: typing.Callable[[], T_Result],
        db_postgres_user: typing.Callable[[], T_Result],
        pooler: typing.Callable[[], T_Result],
        realtime: typing.Callable[[], T_Result],
        rest: typing.Callable[[], T_Result],
        storage: typing.Callable[[], T_Result],
        pg_bouncer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ServiceHealthResponseOutputName.AUTH:
            return auth()
        if self is V1ServiceHealthResponseOutputName.DB:
            return db()
        if self is V1ServiceHealthResponseOutputName.DB_POSTGRES_USER:
            return db_postgres_user()
        if self is V1ServiceHealthResponseOutputName.POOLER:
            return pooler()
        if self is V1ServiceHealthResponseOutputName.REALTIME:
            return realtime()
        if self is V1ServiceHealthResponseOutputName.REST:
            return rest()
        if self is V1ServiceHealthResponseOutputName.STORAGE:
            return storage()
        if self is V1ServiceHealthResponseOutputName.PG_BOUNCER:
            return pg_bouncer()
