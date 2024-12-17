-- AIRPORTS

create or replace TABLE SANDBOX_AZULCARGO.ANACBR.AIRPORTS 
(
	IDAIRPORT NUMBER(38,0),
	ICAO VARCHAR(8),
	IATA VARCHAR(8),
	AIRPORTNAME VARCHAR(512),
	TOWN VARCHAR(512),
	UF VARCHAR(8),
	REGION VARCHAR(512),
	COUNTRY VARCHAR(512),
	CONTINENT VARCHAR(512),
	IDRPROCESS NUMBER(38,0)
);



create or replace procedure SANDBOX_AZULCARGO.ANACBR.dimAirports(idrProcess NUMBER(38,0))
    returns VARCHAR
    language sql
AS
declare
    msg VARCHAR DEFAULT '';
	begin
		begin
			INSERT INTO SANDBOX_AZULCARGO.ANACBR.airports (idAirport, icao, iata, airportName, town, uf, region, country, continent, idrProcess)
			SELECT 		a.ID_AERODROMO AS idAirport,
						CASE WHEN a.SG_ICAO = 'unknown' THEN NULL ELSE a.SG_ICAO END AS icao,
						CASE WHEN a.SG_IATA = 'unknown' THEN NULL ELSE a.SG_IATA END AS iata,
						CASE WHEN a.NM_AERODROMO = 'unknown' THEN NULL ELSE a.NM_AERODROMO END AS airportName,
						CASE WHEN a.NM_MUNICIPIO = 'unknown' THEN NULL ELSE a.NM_MUNICIPIO END AS town,
						CASE WHEN a.SG_UF = 'unknown' THEN NULL ELSE a.SG_UF END AS uf,
						CASE WHEN a.NM_REGIAO = 'unknown' THEN NULL ELSE a.NM_REGIAO END AS region,
						CASE WHEN a.NM_PAIS = 'unknown' THEN NULL ELSE a.NM_PAIS END AS country,
						CASE WHEN a.NM_CONTINENTE = 'unknown' THEN NULL ELSE a.NM_CONTINENTE END AS continent,
						a.IDRPROCESS
			FROM 		SANDBOX_AZULCARGO.ANACBR.RAWAIRPORTS a
			LEFT JOIN 	SANDBOX_AZULCARGO.ANACBR.AIRPORTS b ON a.SG_ICAO = b.icao
			WHERE 		b.idAirport IS NULL
			and			a.IDRPROCESS = :idrProcess;
			msg := 'OK';
		exception
			when other then msg := 'NOOK';
	end;
	return msg;
end;