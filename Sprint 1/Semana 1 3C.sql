use programa_bolsas;

select CodVendedor as Codigo , A.NmVdd as Vendedor , Valor_da_venda ,
    concat(A.PercComissao,"%") as '%' ,round((C.Valor_da_venda * A.PercComissao) / 100 ,3)as Valor_da_comissao
from( select B.CdVdd as CodVendedor , sum(B.Qtd) * sum(B.VrUnt) as Valor_da_venda from TbVendas B where B.status = 'Concluído'
		group by B.CdVdd) C
left join TbVendedor A on C.CodVendedor = A.CdVdd ;