<<<<<<< HEAD:sql/crear-pensiones.sql
create table Pensiones (
        cedula integer primary key,
        base_settlement_income real not null,
        current_legal_minimum_wage real not null,
        pension_porcentage real not null
=======
create table if not exists Pensiones (
        cedula integer primary key,
        base_settlement_income real not null,
        current_legal_minimum_wage real not null,
        pension_porcentage real not null
>>>>>>> a43afe1d20d40cd9a90d55b9c4659cfa8716d34b:sql/crear-pension.sql
        );