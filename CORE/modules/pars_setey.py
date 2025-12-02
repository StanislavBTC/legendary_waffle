import netifaces 

interfaces = netifaces.interfaces()
print(interfaces)

'''
import netifaces

# Получение списка всех интерфейсов
interfaces = netifaces.interfaces()

# Перебор всех интерфейсов
for interface in interfaces:
    try:
        # Получение адресов для текущего интерфейса
        addresses = netifaces.ifaddresses(interface)
        
        # Получение IPv4 адреса (если есть)
        if netifaces.AF_INET in addresses:
            ipv4_info = addresses[netifaces.AF_INET][0]
            print(f"Интерфейс: {interface}")
            print(f"  IP-адрес: {ipv4_info['addr']}")
            print(f"  Маска сети: {ipv4_info['netmask']}")
    except ValueError:
        # Обработка ошибок, например, если интерфейс не существует
        print(f"Не удалось получить информацию для интерфейса {interface}")

https://codeby.net/threads/polucheniye-bazovykh-parametrov-setevykh-interfeisov-po-umolchaniyu-dlya-ispol-zovaniya-v-proyektakh-python.80824/ 
полезная штука
'''