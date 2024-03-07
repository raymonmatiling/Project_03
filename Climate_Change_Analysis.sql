CREATE TABLE per_capita_emissions (
    entity VARCHAR(250),
    code VARCHAR(8),
    year INTEGER,
    annual_co2_emissions DOUBLE PRECISION
);

CREATE TABLE annual_emissions (
    entity VARCHAR(250),
    code VARCHAR(8),
    year INTEGER,
    annual_co2_emissions DOUBLE PRECISION
);

select * from annual_emissions