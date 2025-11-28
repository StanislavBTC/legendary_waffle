# парсер всех сетевых интерфейсов системы

import netifaces 

interfaces = netifaces.interfaces()
print(interfaces)