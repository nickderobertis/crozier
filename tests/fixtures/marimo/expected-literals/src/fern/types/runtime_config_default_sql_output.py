

import typing

RuntimeConfigDefaultSqlOutput = typing.Union[
    typing.Literal["auto", "lazy-polars", "native", "pandas", "polars"], typing.Any
]
