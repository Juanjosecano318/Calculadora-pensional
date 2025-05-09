<<<<<<< HEAD:sql/crear-usuarios.sql
create table Usuarios (
    cedula integer primary key,
    nombre text not null,
    base_settlement_income real not null,
    current_legal_minimum_wage real not null,
    pension_porcentage real not null
);

=======
create table if not exists Usuarios (
    cedula integer primary key,
    nombre text not null,
    base_settlement_income real not null,
    current_legal_minimum_wage real not null,
    pension_porcentage real not null
);
>>>>>>> a43afe1d20d40cd9a90d55b9c4659cfa8716d34b:sql/crear-usuario.sql
