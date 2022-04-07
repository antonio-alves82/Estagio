USE programa_bolsas;
select A.NmVdd AS Nome, A.CdVdd as Codigo_do_Vendedor, COUNT(A.CdVdd) AS Total
from TbVendedor A left join TbVendas B on A.CdVdd = B.CdVdd
where B.status = 'Concluído'
Group by A.NmVdd
order by Total desc
limit 0,1;