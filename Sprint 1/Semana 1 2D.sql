USE programa_bolsas;

select Autor, count(Publicacao) as Total_de_Publicacoes from LIVRO group by Autor;