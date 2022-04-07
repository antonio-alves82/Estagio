USE programa_bolsas;

select A.Estado, avg(A.Gastos) AS Media_de_Gastos from
	(select Estado, Qtd, VrUnt, Qtd*VrUnt as Gastos from TbVendas) A group by A.Estado
order by Media_de_gastos asc;

