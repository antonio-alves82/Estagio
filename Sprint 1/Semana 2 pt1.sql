USE programa_bolsas ;

select A.Cod as Código_do_Livro, A.Titulo as Titulo, A.Autor as Código_do_Autor, B.Nome as Nome_do_Autor, A.Valor as Valor, A.CodEditora as Código_da_Editora,  A.Nome as Nome_da_Editora
from(select * from LIVRO C RIGHT JOIN EDITORA D on C.Editora = D.CodEditora ) A left join AUTOR B
on A.Autor = B.CodAutor
group by A.Nome 
order by A.valor desc 
limit 0,10;