USE programa_bolsas ;
select NmCli as Nome_do_Cliente, CdCli as Codigo_do_cliente, SUM(Qtd)*SUM(VrUnt) AS total from TbVendas
where status = 'Concluído'
group by NmCli
order by total desc limit 0,1;
