USE programa_bolsas;

select Editora, count(Publicacao) as Total_de_Publicacoes 
from LIVRO group by Editora;