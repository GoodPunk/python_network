# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

ospf_route_temp = ospf_route.strip().split()
#print (ospf_route_temp)
ospf_r1 = ospf_route_temp[0]
ospf_r2 = ospf_route_temp[1].strip("[]")
ospf_r3 = ospf_route_temp[3].strip(",")
ospf_r4 = ospf_route_temp[4].strip(",")
ospf_r5 = ospf_route_temp[5]

print (template.format(ospf_r1,ospf_r2,ospf_r3,ospf_r4,ospf_r5))
