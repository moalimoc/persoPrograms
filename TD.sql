--TD 1
--1
select COUNT(*) from triangles;
SELECT * FROM triangles where ab+bc+ac = 100;

select * 
from triangles 
where bc*bc = ac*ac + ab*ab;

select count(*) 
from triangles 
where bc*bc = ac*ac + ab*ab;

SELECT *, (ab + bc + ac) as 'perimetre maximale'
from triangles 
where bc*bc = ac*ac + ab*ab
Order by (ab+bc+ac) DESC
Limit 1;

select *
from triangles
EXCEPT 
select * 
from triangles 
WHERE ab > bc + ac or bc > ac + ac or ac > ab + bc;

SELECT ab, ac, bc 
from triangles 
where ab*ac*bc >= 99;



--2
select count(DISTINCT prenom) 
from enregistrement_etat_civil
where sexe = 'F';

SELECT sum(nombre), prenom
from enregistrement_etat_civil
group by prenom;

SELECT count(prenom)
from enregistrement_etat_civil
where annee = 2004 and prenom = 'Mohamed-Ali';

SELECT count(DISTINCT(prenom)), annee
from enregistrement_etat_civil
group by annee;

SELECT sum(nombre) as s, prenom, annee
from enregistrement_etat_civil
where annee = 2004
order by s DESC
limit 1;

----------------------------------
--TD2
--c
--i
select communes.nom, departements.nom, regions.nom, communes.pop
from communes
join departements on communes.dep = departements.id
join regions on departements.reg = regions.id

--ii
select communes.pop
from communes
where communes.nom = 'Chelles'

select count(communes.nom) 
from communes
where communes.pop > (select communes.pop from communes where communes.nom = 'Chelles' ORder by pop DESC LIMIT 1)

--iii
select C.nom, C.pop, R.nom
FROM communes AS C
join departements as D on C.dep = D.id
join regions AS R on D.reg = R.id
WHERE C.pop > 100000
order by C.pop DESC

--iv
select D.nom, SUM(C.pop) 
FROM communes AS C
join departements as D on C.dep = D.id
Group by D.nom

select D.nom, SUM(C.pop) 
FROM communes AS C
join departements as D on C.dep = D.id
Group by D.nom
order by SUM(C.pop) desc limit 1










