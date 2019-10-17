#Adding Tipo De Denuncia
insert into rotasegura.tipo_denuncia_tipodenuncia(descricao, created_at, updated_at, icone)
values('Problemas de Trafego', sysdate(), sysdate(), 'traffic-light');

insert into rotasegura.tipo_denuncia_tipodenuncia(descricao, created_at, updated_at, icone)
values('Problemas de Acessibilidade', sysdate(), sysdate(), 'universal-access');

insert into rotasegura.tipo_denuncia_tipodenuncia(descricao, created_at, updated_at, icone)
values('Desastres Naturais', sysdate(), sysdate(), 'meteor');

insert into rotasegura.tipo_denuncia_tipodenuncia(descricao, created_at, updated_at, icone)
values('Criminalidades', sysdate(), sysdate(), 'user-ninja');

insert into rotasegura.tipo_denuncia_tipodenuncia(descricao, created_at, updated_at, icone)
values('Outros', sysdate(), sysdate(), 'exclamation-triangle');

#Adding Denuncia

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Tráfego Intenso', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Problemas de Trafego'), 'traffic-light');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Acidente', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Problemas de Trafego'), 'car-crash');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Obras na Pista', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Problemas de Trafego'), 'tools');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Trovejada Intensa', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Desastres Naturais'), 'bolt');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Nevasca', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Desastres Naturais'), 'snowflake');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Chuvas Intensas', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Desastres Naturais'), 'cloud-showers-heavy');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Chuvas de Granizo', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Desastres Naturais'), 'cloud-meatball');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Trafico de Drogas', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Criminalidades'), 'cannabis');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Assasinato', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Criminalidades'), 'skull');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Assaltantes', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Criminalidades'), 'user-ninja');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Radiação', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Outros'), 'radiation');

insert into rotasegura.denuncias_denuncia(descricao, created_at, tipo_denuncia_id, icone)
values('Animal Perdido', sysdate(), (select id from rotasegura.tipo_denuncia_tipodenuncia where descricao = 'Outros'), 'paw');

select * from rotasegura.tipo_denuncia_tipodenuncia
select * from rotasegura.denuncias_denuncia
