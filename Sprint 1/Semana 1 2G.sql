USE programa_bolsas;
select A.CodAutor, A.Nome, COUNT(*) as Livros_publicados From 
AUTOR A inner join LIVRO B 
on A.CodAutor = B.Autor
Group By A.CodAutor, A.nome order by Livros_publicados Asc Limit 0,1;