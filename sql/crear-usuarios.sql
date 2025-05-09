create table if not exists Usuarios (
    cedula integer primary key,
    nombre text not null,
    base_settlement_income real not null,
    current_legal_minimum_wage real not null,
    pension_porcentage real not null
);
