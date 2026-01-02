import requests
import json
import webbrowser

class OsintMachine:
    def __init__(self, phone):
        self.phone = phone
        self.results = {}

    def get_operator_info(self):
        """Определяет регион и оператора (Фундамент)"""
        print("[*] Поиск определеных данных")
        try:
            r = requests.get(f"https://htmlweb.ru/geo/api.php?json&telcod={self.phone}")
            data = r.json()
            self.results['operator'] = data.get('0', {}).get('oper', 'Не найдено')
            self.results['region'] = data.get('0', {}).get('name', 'Не найдено')
        except:
            self.results['operator'] = "Ошибка запроса"

    def check_social_presence(self):
        """Проверка наличия в мессенджерах (Социальный след)"""
        print("[*] Генерирую ссылки для проверки мессенджеров...")
        self.results['wa_link'] = f"https://api.whatsapp.com/send?phone={self.phone}"
        
        self.results['tg_link'] = f"https://t.me/+{self.phone}"

    def leak_check_query(self):
        """Имитация запроса к базам утечек (Deep Search)"""
        print("[*] Поиск в архивах утечек (LeakCheck/Scylla)...")
        
        self.results['leaks'] = f"https://www.google.com/search?q=site:leakcheck.io+{self.phone}"

    def run_all(self):
        self.get_operator_info()
        self.check_social_presence()
        self.leak_check_query()
        
        print("\n--- ОТЧЕТ ПО ОБЪЕКТУ ---")
        for key, value in self.results.items():
            print(f"{key.upper()}: {value}")
            
        webbrowser.open(self.results['wa_link'])
        webbrowser.open(self.results['leaks'])
        webbrowser.open(f"https://mirror.bullseye.com/search?q={self.phone}")

if __name__ == "__main__":
    target = input("Введите номер телефона: ")
    osint = OsintMachine(target)
    osint.run_all()
