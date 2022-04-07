USE programa_bolsas;
select NmPro as Nome_do_Produto ,CdPro as Codigo_do_Produto, SUM(Qtd) AS Quantidade_Total from TbVendas
where DtVen between '2014-02-03' and '2018-02-02' and status = 'Concluído'
group by NmPro,CdPro
order by Quantidade_Total desc
limit 0,1;


