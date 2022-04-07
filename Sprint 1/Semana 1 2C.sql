USE programa_bolsas;

SELECT A.Nome as Nome_da_Editora, COUNT(B.COD) AS total_de_livros FROM EDITORA A INNER JOIN LIVRO B
on A.CodEditora = B.Editora
group by A.Nome 
order by total_de_livros DESC 
limit 0,5;
