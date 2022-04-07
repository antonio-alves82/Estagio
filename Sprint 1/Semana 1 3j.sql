USE programa_bolsas;

select A.NmDep as Nome_do_Dependente, B.NmVdd as Vendedor, sum(C.VrUnt) * sum(C.Qtd) as valor_gasto
From TbDependente A Left join TbVendedor B on A.CdVdd = B.CdVdd
left join TbVendas C on B.CdVdd = C.CdVdd
where C.status = 'Concluído'
group by A.NmDep, A.InepEscola
order by valor_gasto asc;