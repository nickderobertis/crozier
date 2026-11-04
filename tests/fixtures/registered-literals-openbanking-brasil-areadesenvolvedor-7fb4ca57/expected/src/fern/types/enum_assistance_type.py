

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumAssistanceType(enum.StrEnum):
    """
    Lista padronizada de tipo de assistências ofertadas vinculadas ao produto. Por exemplo, Funeral, Bicicleta, Assistência PET – Tabela padrão a ser consolidada com retorno das empresas com a relação de assistências, permitindo um campo ‘Outros’ para assistências não contempladas na tabela padronizada.
    """

    ACOMPANHANTE_CASO_HOSPITALIZACAO_PROLONGADA = "ACOMPANHANTE_CASO_HOSPITALIZACAO_PROLONGADA"
    ARQUITETO_VIRTUAL = "ARQUITETO_VIRTUAL"
    ASSESSORIA_FINANCEIRA = "ASSESSORIA_FINANCEIRA"
    AUTOMOVEL = "AUTOMOVEL"
    AUXILIO_NATALIDADE = "AUXILIO_NATALIDADE"
    AVALIACAO_CLINICA_PREVENTIVA = "AVALIACAO_CLINICA_PREVENTIVA"
    BOLSA_PROTEGIDA = "BOLSA_PROTEGIDA"
    CESTA_BASICA = "CESTA_BASICA"
    CHECKUP_ODONTOLOGICO = "CHECKUP_ODONTOLOGICO"
    CLUBE_VANTAGENS_BENEFICIOS = "CLUBE_VANTAGENS_BENEFICIOS"
    CONVALESCENCIA = "CONVALESCENCIA"
    DECESSO = "DECESSO"
    DESCONTO_FARMACIAS_MEDICAMENTOS = "DESCONTO_FARMACIAS_MEDICAMENTOS"
    DESPESAS_FARMACEUTICAS_VIAGEM = "DESPESAS_FARMACEUTICAS_VIAGEM"
    DIGITAL = "DIGITAL"
    EDUCACIONAL = "EDUCACIONAL"
    EMPRESARIAL = "EMPRESARIAL"
    ENCANADOR = "ENCANADOR"
    ENTRETENIMENTO = "ENTRETENIMENTO"
    EQUIPAMENTOS_MEDICOS = "EQUIPAMENTOS_MEDICOS"
    FIANCAS_DESPESAS_LEGAIS = "FIANCAS_DESPESAS_LEGAIS"
    FISIOTERAPIA = "FISIOTERAPIA"
    FUNERAL = "FUNERAL"
    HELP_LINE = "HELP_LINE"
    HOSPEDAGEM_ACOMPANHANTE = "HOSPEDAGEM_ACOMPANHANTE"
    INTERRUPCAO_VIAGEM = "INTERRUPCAO_VIAGEM"
    INVENTARIO = "INVENTARIO"
    MAIS_VIDA = "MAIS_VIDA"
    MAMAE_BEBE = "MAMAE_BEBE"
    MEDICA_ACIDENTE_DOENCA = "MEDICA_ACIDENTE_DOENCA"
    MOTOCICLETA = "MOTOCICLETA"
    MULHER = "MULHER"
    NUTRICIONISTA = "NUTRICIONISTA"
    ODONTOLOGICA = "ODONTOLOGICA"
    ORIENTACAO_FITNESS = "ORIENTACAO_FITNESS"
    ORIENTACAO_JURIDICA = "ORIENTACAO_JURIDICA"
    ORIENTACAO_NUTRICIONAL = "ORIENTACAO_NUTRICIONAL"
    PERSONAL_FITNESS = "PERSONAL_FITNESS"
    ORIENTACAO_PSICOSSOCIAL_FAMILIAR = "ORIENTACAO_PSICOSSOCIAL_FAMILIAR"
    PERDA_ROUBO_CARTAO = "PERDA_ROUBO_CARTAO"
    PET = "PET"
    PRORROGACAO_ESTADIA = "PRORROGACAO_ESTADIA"
    PROTECAO_DADOS = "PROTECAO_DADOS"
    RECOLOCACAO_PROFISSIONAL = "RECOLOCACAO_PROFISSIONAL"
    REDE_DESCONTO_NUTRICIONAL = "REDE_DESCONTO_NUTRICIONAL"
    RESIDENCIAL = "RESIDENCIAL"
    RETORNO_MENORES_SEGURADO = "RETORNO_MENORES_SEGURADO"
    SAQUE_COACAO = "SAQUE_COACAO"
    SAUDE_BEM_ESTAR = "SAUDE_BEM_ESTAR"
    SEGUNDA_OPINIAO_MEDICA = "SEGUNDA_OPINIAO_MEDICA"
    SENIOR = "SENIOR"
    SUSTENTAVEL_DESCARTE_ECOLOGICO = "SUSTENTAVEL_DESCARTE_ECOLOGICO"
    TELEMEDICINA = "TELEMEDICINA"
    VIAGEM = "VIAGEM"
    VITIMA = "VITIMA"
    OUTROS = "OUTROS"

    def visit(
        self,
        acompanhante_caso_hospitalizacao_prolongada: typing.Callable[[], T_Result],
        arquiteto_virtual: typing.Callable[[], T_Result],
        assessoria_financeira: typing.Callable[[], T_Result],
        automovel: typing.Callable[[], T_Result],
        auxilio_natalidade: typing.Callable[[], T_Result],
        avaliacao_clinica_preventiva: typing.Callable[[], T_Result],
        bolsa_protegida: typing.Callable[[], T_Result],
        cesta_basica: typing.Callable[[], T_Result],
        checkup_odontologico: typing.Callable[[], T_Result],
        clube_vantagens_beneficios: typing.Callable[[], T_Result],
        convalescencia: typing.Callable[[], T_Result],
        decesso: typing.Callable[[], T_Result],
        desconto_farmacias_medicamentos: typing.Callable[[], T_Result],
        despesas_farmaceuticas_viagem: typing.Callable[[], T_Result],
        digital: typing.Callable[[], T_Result],
        educacional: typing.Callable[[], T_Result],
        empresarial: typing.Callable[[], T_Result],
        encanador: typing.Callable[[], T_Result],
        entretenimento: typing.Callable[[], T_Result],
        equipamentos_medicos: typing.Callable[[], T_Result],
        fiancas_despesas_legais: typing.Callable[[], T_Result],
        fisioterapia: typing.Callable[[], T_Result],
        funeral: typing.Callable[[], T_Result],
        help_line: typing.Callable[[], T_Result],
        hospedagem_acompanhante: typing.Callable[[], T_Result],
        interrupcao_viagem: typing.Callable[[], T_Result],
        inventario: typing.Callable[[], T_Result],
        mais_vida: typing.Callable[[], T_Result],
        mamae_bebe: typing.Callable[[], T_Result],
        medica_acidente_doenca: typing.Callable[[], T_Result],
        motocicleta: typing.Callable[[], T_Result],
        mulher: typing.Callable[[], T_Result],
        nutricionista: typing.Callable[[], T_Result],
        odontologica: typing.Callable[[], T_Result],
        orientacao_fitness: typing.Callable[[], T_Result],
        orientacao_juridica: typing.Callable[[], T_Result],
        orientacao_nutricional: typing.Callable[[], T_Result],
        personal_fitness: typing.Callable[[], T_Result],
        orientacao_psicossocial_familiar: typing.Callable[[], T_Result],
        perda_roubo_cartao: typing.Callable[[], T_Result],
        pet: typing.Callable[[], T_Result],
        prorrogacao_estadia: typing.Callable[[], T_Result],
        protecao_dados: typing.Callable[[], T_Result],
        recolocacao_profissional: typing.Callable[[], T_Result],
        rede_desconto_nutricional: typing.Callable[[], T_Result],
        residencial: typing.Callable[[], T_Result],
        retorno_menores_segurado: typing.Callable[[], T_Result],
        saque_coacao: typing.Callable[[], T_Result],
        saude_bem_estar: typing.Callable[[], T_Result],
        segunda_opiniao_medica: typing.Callable[[], T_Result],
        senior: typing.Callable[[], T_Result],
        sustentavel_descarte_ecologico: typing.Callable[[], T_Result],
        telemedicina: typing.Callable[[], T_Result],
        viagem: typing.Callable[[], T_Result],
        vitima: typing.Callable[[], T_Result],
        outros: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumAssistanceType.ACOMPANHANTE_CASO_HOSPITALIZACAO_PROLONGADA:
            return acompanhante_caso_hospitalizacao_prolongada()
        if self is EnumAssistanceType.ARQUITETO_VIRTUAL:
            return arquiteto_virtual()
        if self is EnumAssistanceType.ASSESSORIA_FINANCEIRA:
            return assessoria_financeira()
        if self is EnumAssistanceType.AUTOMOVEL:
            return automovel()
        if self is EnumAssistanceType.AUXILIO_NATALIDADE:
            return auxilio_natalidade()
        if self is EnumAssistanceType.AVALIACAO_CLINICA_PREVENTIVA:
            return avaliacao_clinica_preventiva()
        if self is EnumAssistanceType.BOLSA_PROTEGIDA:
            return bolsa_protegida()
        if self is EnumAssistanceType.CESTA_BASICA:
            return cesta_basica()
        if self is EnumAssistanceType.CHECKUP_ODONTOLOGICO:
            return checkup_odontologico()
        if self is EnumAssistanceType.CLUBE_VANTAGENS_BENEFICIOS:
            return clube_vantagens_beneficios()
        if self is EnumAssistanceType.CONVALESCENCIA:
            return convalescencia()
        if self is EnumAssistanceType.DECESSO:
            return decesso()
        if self is EnumAssistanceType.DESCONTO_FARMACIAS_MEDICAMENTOS:
            return desconto_farmacias_medicamentos()
        if self is EnumAssistanceType.DESPESAS_FARMACEUTICAS_VIAGEM:
            return despesas_farmaceuticas_viagem()
        if self is EnumAssistanceType.DIGITAL:
            return digital()
        if self is EnumAssistanceType.EDUCACIONAL:
            return educacional()
        if self is EnumAssistanceType.EMPRESARIAL:
            return empresarial()
        if self is EnumAssistanceType.ENCANADOR:
            return encanador()
        if self is EnumAssistanceType.ENTRETENIMENTO:
            return entretenimento()
        if self is EnumAssistanceType.EQUIPAMENTOS_MEDICOS:
            return equipamentos_medicos()
        if self is EnumAssistanceType.FIANCAS_DESPESAS_LEGAIS:
            return fiancas_despesas_legais()
        if self is EnumAssistanceType.FISIOTERAPIA:
            return fisioterapia()
        if self is EnumAssistanceType.FUNERAL:
            return funeral()
        if self is EnumAssistanceType.HELP_LINE:
            return help_line()
        if self is EnumAssistanceType.HOSPEDAGEM_ACOMPANHANTE:
            return hospedagem_acompanhante()
        if self is EnumAssistanceType.INTERRUPCAO_VIAGEM:
            return interrupcao_viagem()
        if self is EnumAssistanceType.INVENTARIO:
            return inventario()
        if self is EnumAssistanceType.MAIS_VIDA:
            return mais_vida()
        if self is EnumAssistanceType.MAMAE_BEBE:
            return mamae_bebe()
        if self is EnumAssistanceType.MEDICA_ACIDENTE_DOENCA:
            return medica_acidente_doenca()
        if self is EnumAssistanceType.MOTOCICLETA:
            return motocicleta()
        if self is EnumAssistanceType.MULHER:
            return mulher()
        if self is EnumAssistanceType.NUTRICIONISTA:
            return nutricionista()
        if self is EnumAssistanceType.ODONTOLOGICA:
            return odontologica()
        if self is EnumAssistanceType.ORIENTACAO_FITNESS:
            return orientacao_fitness()
        if self is EnumAssistanceType.ORIENTACAO_JURIDICA:
            return orientacao_juridica()
        if self is EnumAssistanceType.ORIENTACAO_NUTRICIONAL:
            return orientacao_nutricional()
        if self is EnumAssistanceType.PERSONAL_FITNESS:
            return personal_fitness()
        if self is EnumAssistanceType.ORIENTACAO_PSICOSSOCIAL_FAMILIAR:
            return orientacao_psicossocial_familiar()
        if self is EnumAssistanceType.PERDA_ROUBO_CARTAO:
            return perda_roubo_cartao()
        if self is EnumAssistanceType.PET:
            return pet()
        if self is EnumAssistanceType.PRORROGACAO_ESTADIA:
            return prorrogacao_estadia()
        if self is EnumAssistanceType.PROTECAO_DADOS:
            return protecao_dados()
        if self is EnumAssistanceType.RECOLOCACAO_PROFISSIONAL:
            return recolocacao_profissional()
        if self is EnumAssistanceType.REDE_DESCONTO_NUTRICIONAL:
            return rede_desconto_nutricional()
        if self is EnumAssistanceType.RESIDENCIAL:
            return residencial()
        if self is EnumAssistanceType.RETORNO_MENORES_SEGURADO:
            return retorno_menores_segurado()
        if self is EnumAssistanceType.SAQUE_COACAO:
            return saque_coacao()
        if self is EnumAssistanceType.SAUDE_BEM_ESTAR:
            return saude_bem_estar()
        if self is EnumAssistanceType.SEGUNDA_OPINIAO_MEDICA:
            return segunda_opiniao_medica()
        if self is EnumAssistanceType.SENIOR:
            return senior()
        if self is EnumAssistanceType.SUSTENTAVEL_DESCARTE_ECOLOGICO:
            return sustentavel_descarte_ecologico()
        if self is EnumAssistanceType.TELEMEDICINA:
            return telemedicina()
        if self is EnumAssistanceType.VIAGEM:
            return viagem()
        if self is EnumAssistanceType.VITIMA:
            return vitima()
        if self is EnumAssistanceType.OUTROS:
            return outros()
