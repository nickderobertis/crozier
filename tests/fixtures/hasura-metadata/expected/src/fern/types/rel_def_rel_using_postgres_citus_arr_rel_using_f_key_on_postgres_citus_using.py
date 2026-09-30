

import typing

from .citus_ru_manual import CitusRuManual
from .ruf_key_on_arr_rel_using_f_key_on_postgres_citus import RufKeyOnArrRelUsingFKeyOnPostgresCitus

RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitusUsing = typing.Union[
    RufKeyOnArrRelUsingFKeyOnPostgresCitus, CitusRuManual
]
