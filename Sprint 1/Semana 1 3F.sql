USE programa_bolsas;

select NmPro as Nome_do_produto , NmCanalVendas AS Local_da_venda, SUM(Qtd) AS total
from TbVendas where status = 'Concluído' and CdCanalVendas in (1,2)
group by NmCanalVendas, NmPro 
order by total asc limit 0,10;