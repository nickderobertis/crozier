

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutListingsSlugRequestConditionUuid(enum.StrEnum):
    """
    Condition UUID
    """

    FBF3566896A04BAA_BCDE_AB18D6B1B329 = "fbf35668-96a0-4baa-bcde-ab18d6b1b329"
    SIX_A9DFCAD600B46C89E08CE6E5057921E = "6a9dfcad-600b-46c8-9e08-ce6e5057921e"
    UNDEFINED76D044C8865E_BB40E669E934 = "98777886-76d0-44c8-865e-bb40e669e934"
    F7A3F48C972A44C6B01A0CD27488D3F6 = "f7a3f48c-972a-44c6-b01a-0cd27488d3f6"
    AE4D91141BD74EC5A4BA6653AF5AC84D = "ae4d9114-1bd7-4ec5-a4ba-6653af5ac84d"
    DF268AD1C4624BA6B6DB_E007E23922EA = "df268ad1-c462-4ba6-b6db-e007e23922ea"
    AC5B9C1E_DC78466DB0B37CF712967A48 = "ac5b9c1e-dc78-466d-b0b3-7cf712967a48"
    SIX_DB7DF88293B4017A1C1CDB5E599FA1A = "6db7df88-293b-4017-a1c1-cdb5e599fa1a"
    UNDEFINED_F60C24413AD181F5EBA7A856F = "9225283f-60c2-4413-ad18-1f5eba7a856f"
    SEVEN_C3F45DE2AE04C818400FDB6B1D74890 = "7c3f45de-2ae0-4c81-8400-fdb6b1d74890"

    def visit(
        self,
        fbf3566896a04baa_bcde_ab18d6b1b329: typing.Callable[[], T_Result],
        six_a9dfcad600b46c89e08ce6e5057921e: typing.Callable[[], T_Result],
        undefined76d044c8865e_bb40e669e934: typing.Callable[[], T_Result],
        f7a3f48c972a44c6b01a0cd27488d3f6: typing.Callable[[], T_Result],
        ae4d91141bd74ec5a4ba6653af5ac84d: typing.Callable[[], T_Result],
        df268ad1c4624ba6b6db_e007e23922ea: typing.Callable[[], T_Result],
        ac5b9c1e_dc78466db0b37cf712967a48: typing.Callable[[], T_Result],
        six_db7df88293b4017a1c1cdb5e599fa1a: typing.Callable[[], T_Result],
        undefined_f60c24413ad181f5eba7a856f: typing.Callable[[], T_Result],
        seven_c3f45de2ae04c818400fdb6b1d74890: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutListingsSlugRequestConditionUuid.FBF3566896A04BAA_BCDE_AB18D6B1B329:
            return fbf3566896a04baa_bcde_ab18d6b1b329()
        if self is PutListingsSlugRequestConditionUuid.SIX_A9DFCAD600B46C89E08CE6E5057921E:
            return six_a9dfcad600b46c89e08ce6e5057921e()
        if self is PutListingsSlugRequestConditionUuid.UNDEFINED76D044C8865E_BB40E669E934:
            return undefined76d044c8865e_bb40e669e934()
        if self is PutListingsSlugRequestConditionUuid.F7A3F48C972A44C6B01A0CD27488D3F6:
            return f7a3f48c972a44c6b01a0cd27488d3f6()
        if self is PutListingsSlugRequestConditionUuid.AE4D91141BD74EC5A4BA6653AF5AC84D:
            return ae4d91141bd74ec5a4ba6653af5ac84d()
        if self is PutListingsSlugRequestConditionUuid.DF268AD1C4624BA6B6DB_E007E23922EA:
            return df268ad1c4624ba6b6db_e007e23922ea()
        if self is PutListingsSlugRequestConditionUuid.AC5B9C1E_DC78466DB0B37CF712967A48:
            return ac5b9c1e_dc78466db0b37cf712967a48()
        if self is PutListingsSlugRequestConditionUuid.SIX_DB7DF88293B4017A1C1CDB5E599FA1A:
            return six_db7df88293b4017a1c1cdb5e599fa1a()
        if self is PutListingsSlugRequestConditionUuid.UNDEFINED_F60C24413AD181F5EBA7A856F:
            return undefined_f60c24413ad181f5eba7a856f()
        if self is PutListingsSlugRequestConditionUuid.SEVEN_C3F45DE2AE04C818400FDB6B1D74890:
            return seven_c3f45de2ae04c818400fdb6b1d74890()
