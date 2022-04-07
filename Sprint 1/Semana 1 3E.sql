USE programa_bolsas ;

select A.NmDep as Nome_do_Dependente , A.InepEscola as Inep_da_Escola, B.NmVdd as Vendedor, sum(C.VrUnt) * sum(C.Qtd) as Total
from TbDependente A left join TbVendedor B on A.CdVdd = B.CdVdd
left join TbVendas C on B.CdVdd = C.CdVdd
where C.status = 'Concluído'
group by A.NmDep, A.InepEscola
order by Total desc
limit 0,1;
