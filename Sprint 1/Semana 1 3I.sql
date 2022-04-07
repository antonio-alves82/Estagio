USE programa_bolsas ;
select Estado as Estado ,sum(Qtd) as Numero_de_Itens ,sum(VrUnt) AS Valor_por_Item ,sum(Qtd) * sum(VrUnt) as Total_de_Gastos
from TbVendas where status = 'Concluído'
group by Estado;

