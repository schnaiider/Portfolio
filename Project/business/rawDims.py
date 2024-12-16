import pandas as pd
from datetime import date

from ..models import  company, identifierDigit, lineType , plane, airport



def rawDims(df: pd.DataFrame):
    # get  raw dim´s
    dfCompanyGroup = df.groupby(['id_empresa', 'sg_empresa_icao', 'sg_empresa_iata', 'nm_empresa', 'nm_pais', 'ds_tipo_empresa']).size().reset_index()
    companys = [company.company(row.id_empresa, row.sg_empresa_icao,row.sg_empresa_iata,row.nm_empresa,row.nm_pais,row.ds_tipo_empresa) for row in dfCompanyGroup.itertuples(index=False)]
    dfCompany = pd.DataFrame([c.__dict__ for c in companys])


    dfCodIdentiGroup = df.groupby(['id_di','cd_di','ds_di','ds_grupo_di']).size().reset_index()
    codIentity = [identifierDigit.diModel(row.id_di, str(row.cd_di), str(row.ds_di), str(row.ds_grupo_di)) for row in dfCodIdentiGroup.itertuples(index=False)]
    dfDigitIndent = pd.DataFrame([c.__dict__ for c in codIentity])

    dfTypeLineGroup = df.groupby(['id_tipo_linha','cd_tipo_linha','ds_tipo_linha','ds_natureza_tipo_linha','ds_servico_tipo_linha','ds_natureza_etapa','ds_tipo_empresa']).size().reset_index()
    typeLine = [lineType.lineType(row.id_tipo_linha,row.cd_tipo_linha,row.ds_tipo_linha,row.ds_natureza_tipo_linha,row.ds_servico_tipo_linha,row.ds_natureza_etapa,row.ds_tipo_empresa) for row in dfTypeLineGroup.itertuples(index=False)]
    dfTypeLine = pd.DataFrame([c.__dict__ for c in typeLine])

    dfPlaneGroup = df.groupby(['id_equipamento','sg_equipamento_icao','ds_modelo','ds_matricula']).size().reset_index()
    planes = [plane.plane(row.id_equipamento,row.sg_equipamento_icao,row.ds_modelo,row.ds_matricula) for row in dfPlaneGroup.itertuples(index=False)]
    dfPlane = pd.DataFrame([c.__dict__ for c in planes])

    dfAirportOrigGroup = df.groupby(['id_aerodromo_origem','sg_icao_origem','sg_iata_origem','nm_aerodromo_origem','nm_municipio_origem','sg_uf_origem','nm_regiao_origem','nm_pais_origem','nm_continente_origem']).size().reset_index()
    origin = [airport.airport(row.id_aerodromo_origem,row.sg_icao_origem,row.sg_iata_origem,row.nm_aerodromo_origem,row.nm_municipio_origem,row.sg_uf_origem,row.nm_regiao_origem,row.nm_pais_origem,row.nm_continente_origem) for row in dfAirportOrigGroup.itertuples(index=False)]
    dfOrigin = pd.DataFrame([c.__dict__ for c in origin])

    dfAirportDestGroup = df.groupby(['id_aerodromo_destino','sg_icao_destino','sg_iata_destino','nm_aerodromo_destino','nm_municipio_destino','sg_uf_destino','nm_regiao_destino','nm_pais_destino','nm_continente_destino']).size().reset_index()
    destination = [airport.airport(row.id_aerodromo_destino,row.sg_icao_destino,row.sg_iata_destino,row.nm_aerodromo_destino,row.nm_municipio_destino,row.sg_uf_destino,row.nm_regiao_destino,row.nm_pais_destino,row.nm_continente_destino) for row in dfAirportDestGroup.itertuples(index=False)]
    dfDestination = pd.DataFrame([c.__dict__ for c in destination])
    
    dfAirports = pd.concat([dfOrigin, dfDestination]).drop_duplicates()

    return dfCompany,dfDigitIndent,dfTypeLine,dfPlane,dfAirports

# get  raw fact 
# dfFactGeral = df[['id_basica','nr_voo','nr_singular','dt_referencia','nr_ano_referencia','nr_semestre_referencia','nm_semestre_referencia','nr_trimestre_referencia','nm_trimestre_referencia','nr_mes_referencia','nm_mes_referencia','nr_semana_referencia','nm_dia_semana_referencia','nr_dia_referencia','nr_ano_mes_referencia','hr_partida_real','dt_partida_real','nr_ano_partida_real','nr_semestre_partida_real','nm_semestre_partida_real','nr_trimestre_partida_real','nm_trimestre_partida_real','nr_mes_partida_real','nm_mes_partida_real','nr_semana_partida_real','nm_dia_semana_partida_real','nr_dia_partida_real','nr_ano_mes_partida_real','nr_etapa','hr_chegada_real','dt_chegada_real','nr_ano_chegada_real','nr_semestre_chegada_real','nm_semestre_chegada_real','nr_trimestre_chegada_real','nm_trimestre_chegada_real','nr_mes_chegada_real','nm_mes_chegada_real','nr_semana_chegada_real','nm_dia_semana_chegada_real','nr_dia_chegada_real','nr_ano_mes_chegada_real','nr_escala_destino','lt_combustivel','nr_assentos_ofertados','kg_payload','km_distancia','nr_passag_pagos','nr_passag_gratis','kg_bagagem_livre','kg_bagagem_excesso','kg_carga_paga','kg_carga_gratis','kg_correio','nr_decolagem','nr_horas_voadas','kg_peso','nr_velocidade_media','nr_pax_gratis_km','nr_carga_paga_km','nr_carga_gratis_km','nr_correio_km','nr_bagagem_paga_km','nr_bagagem_gratis_km','nr_ask','nr_rpk','nr_atk','nr_rtk','id_arquivo','nm_arquivo','nr_linha','dt_sistema']]
# dfFactList = dfFactGeral.apply(lambda row: fact.fact(*row), axis=1).tolist()
# dfFact = pd.DataFrame([obj.__dict__ for obj in dfFactList])