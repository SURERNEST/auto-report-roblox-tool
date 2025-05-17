import sys
import subprocess
import os
import time
import random
import webbrowser

try:
    import requests
except ImportError:
    print("Instalando dependencias necesarias...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

try:
    import msvcrt  # Para Windows
except ImportError:
    msvcrt = None

LANGS = {
    "es": {
        "report_error": "Error al reportar usuario {}: {} {}",
        "connection_error": "Error de conexión: {}",
        "user_id": "ID de usuario a reportar (o 'volver' para regresar): ",
        "reason": "Razón del reporte: ",
        "num_reports": "Número de reportes a enviar: ",
        "invalid_number": "Número inválido.",
        "sending_report": "Enviando reporte {}/{}...",
        "reports_sent": "Reportes enviados exitosamente: {}/{}",
        "back": "volver",
        "help": (
            "Este programa automatiza reportes de usuarios en Roblox.\n"
            "Debes colocar tu cookie de sesión en 'cookie.txt' y, opcionalmente, proxies en 'proxies.txt'.\n"
            "IMPORTANTE: Es altamente recomendable usar una VPN o proxies para evitar baneos de IP.\n"
            "No uses tu IP real para evitar sanciones."
        ),
        "menu_title": "=== AUTO REPORTADOR DE USUARIOS ROBLOX ===",
        "menu_author": "@bochisline en Discord",
        "menu_options": [
            "Auto reportes",
            "Ayuda",
            "Leer antes de usar",
            "¿Cómo obtener la cookie de Roblox?",
            "Salir"
        ],
        "menu_choice": "Selecciona una opción (Enter): ",
        "read_before": (
            "AVISO IMPORTANTE:\n"
            "Usa SIEMPRE una VPN o proxies para evitar baneos de IP al usar este programa.\n"
            "No uses tu IP real. Si no sabes cómo, busca información antes de continuar."
        ),
        "youtube_search": "https://www.youtube.com/results?search_query=como+encontrar+cookie+roblox+roblosecurity",
        "goodbye": "¡Hasta luego!",
        "lang_select": "Selecciona idioma:",
        "lang_options": ["Español", "Inglés", "Português (BR)"]
    },
    "en": {
        "report_error": "Error reporting user {}: {} {}",
        "connection_error": "Connection error: {}",
        "user_id": "User ID to report (or 'back' to return): ",
        "reason": "Reason for report: ",
        "num_reports": "Number of reports to send: ",
        "invalid_number": "Invalid number.",
        "sending_report": "Sending report {}/{}...",
        "reports_sent": "Reports sent successfully: {}/{}",
        "back": "back",
        "help": (
            "This program automates user reports on Roblox.\n"
            "You must put your session cookie in 'cookie.txt' and optionally proxies in 'proxies.txt'.\n"
            "IMPORTANT: It is highly recommended to use a VPN or proxies to avoid IP bans.\n"
            "Do not use your real IP to avoid sanctions."
        ),
        "menu_title": "=== ROBLOX USER AUTO REPORTER ===",
        "menu_author": "@bochisline on Discord",
        "menu_options": [
            "Auto reports",
            "Help",
            "Read before using",
            "How to get Roblox cookie?",
            "Exit"
        ],
        "menu_choice": "Select an option (Enter): ",
        "read_before": (
            "IMPORTANT NOTICE:\n"
            "ALWAYS use a VPN or proxies to avoid IP bans when using this program.\n"
            "Do not use your real IP. If you don't know how, search for information before continuing."
        ),
        "youtube_search": "https://www.youtube.com/results?search_query=how+to+find+roblox+cookie+roblosecurity",
        "goodbye": "Goodbye!",
        "lang_select": "Select language:",
        "lang_options": ["Español", "English", "Português (BR)"]
    },
    "br": {
        "report_error": "Erro ao reportar usuário {}: {} {}",
        "connection_error": "Erro de conexão: {}",
        "user_id": "ID do usuário para reportar (ou 'voltar' para retornar): ",
        "reason": "Motivo do relatório: ",
        "num_reports": "Número de relatórios para enviar: ",
        "invalid_number": "Número inválido.",
        "sending_report": "Enviando relatório {}/{}...",
        "reports_sent": "Relatórios enviados com sucesso: {}/{}",
        "back": "voltar",
        "help": (
            "Este programa automatiza relatórios de usuários no Roblox.\n"
            "Você deve colocar seu cookie de sessão em 'cookie.txt' e, opcionalmente, proxies em 'proxies.txt'.\n"
            "IMPORTANTE: É altamente recomendável usar uma VPN ou proxies para evitar banimento de IP.\n"
            "Não use seu IP real para evitar sanções."
        ),
        "menu_title": "=== AUTO REPORTADOR DE USUÁRIOS ROBLOX ===",
        "menu_author": "@bochisline no Discord",
        "menu_options": [
            "Auto relatórios",
            "Ajuda",
            "Leia antes de usar",
            "Como obter o cookie do Roblox?",
            "Sair"
        ],
        "menu_choice": "Selecione uma opção (Enter): ",
        "read_before": (
            "AVISO IMPORTANTE:\n"
            "SEMPRE use uma VPN ou proxies para evitar banimento de IP ao usar este programa.\n"
            "Não use seu IP real. Se não souber como, procure informações antes de continuar."
        ),
        "youtube_search": "https://www.youtube.com/results?search_query=como+achar+cookie+roblox+roblosecurity",
        "goodbye": "Até logo!",
        "lang_select": "Selecione o idioma:",
        "lang_options": ["Espanhol", "Inglês", "Português (BR)"]
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def arrow_menu(options, title="", author=""):
    idx = 0
    while True:
        clear_screen()
        if title:
            print(title)
        if author:
            print(author)
        print()
        for i, opt in enumerate(options):
            if i == idx:
                print(f"-> {opt}")
            else:
                print(f"   {opt}")
        print("\n(Usa flechas ↑ ↓ y Enter para seleccionar)")
        key = get_key()
        if key == "UP":
            idx = (idx - 1) % len(options)
        elif key == "DOWN":
            idx = (idx + 1) % len(options)
        elif key == "ENTER":
            return idx

def get_key():
    # Windows
    if msvcrt:
        while True:
            key = msvcrt.getch()
            if key == b'\xe0':  # Special keys (arrows, f keys, ins, del, etc.)
                key2 = msvcrt.getch()
                if key2 == b'H':
                    return "UP"
                elif key2 == b'P':
                    return "DOWN"
            elif key == b'\r':
                return "ENTER"
    else:
        # Unix/Linux/Mac
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                ch = sys.stdin.read(1)
                if ch == '\x1b':
                    ch2 = sys.stdin.read(1)
                    if ch2 == '[':
                        ch3 = sys.stdin.read(1)
                        if ch3 == 'A':
                            return "UP"
                        elif ch3 == 'B':
                            return "DOWN"
                elif ch == '\r' or ch == '\n':
                    return "ENTER"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def select_language():
    langs = ["es", "en", "br"]
    idx = arrow_menu(
        [LANGS["es"]["lang_options"][0], LANGS["en"]["lang_options"][1], LANGS["br"]["lang_options"][2]],
        title="=== Selección de idioma / Language selection / Seleção de idioma ==="
    )
    return langs[idx]

def load_cookie(lang, cookie_file="cookie.txt"):
    if os.path.exists(cookie_file):
        with open(cookie_file, "r") as f:
            return f.read().strip()
    else:
        print(LANGS[lang]["connection_error"].format("No se encontró el archivo de cookie."))
        sys.exit(1)

def load_proxies(proxy_file="proxies.txt"):
    proxies = []
    if os.path.exists(proxy_file):
        with open(proxy_file, "r") as f:
            for line in f:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
    return proxies

def get_proxy_dict(proxy_str):
    if "@" in proxy_str:
        user_pass, host_port = proxy_str.split("@")
        proxy_url = f"http://{user_pass}@{host_port}"
    else:
        proxy_url = f"http://{proxy_str}"
    return {
        "http": proxy_url,
        "https": proxy_url
    }

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

def report_user(user_id, reason, cookie, lang, proxies=None):
    l = LANGS[lang]
    url = "https://www.roblox.com/abusereport/submit"
    headers = {
        "Cookie": f".ROBLOSECURITY={cookie}",
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/json"
    }
    data = {
        "targetUserId": user_id,
        "reason": reason,
        "comment": "Reporte automático" if lang == "es" else ("Relatório automático" if lang == "br" else "Automatic report")
    }
    proxy_dict = None
    if proxies:
        proxy_str = random.choice(proxies)
        proxy_dict = get_proxy_dict(proxy_str)
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10, proxies=proxy_dict)
        if response.status_code == 200:
            return True
        else:
            print(l["report_error"].format(user_id, response.status_code, response.text))
            return False
    except Exception as e:
        print(l["connection_error"].format(e))
        return False

def auto_reportador(lang):
    l = LANGS[lang]
    cookie = load_cookie(lang)
    proxies = load_proxies()
    if proxies:
        print("Proxies cargados: {}".format(len(proxies)))
    else:
        print("No se encontraron proxies. Se usará la IP local.")
    while True:
        print("\nEscribe 'ayuda' para ver información de seguridad.")
        user_id = input(l["user_id"])
        if user_id.lower() == l["back"]:
            break
        if user_id.lower() == "ayuda" and lang == "es":
            print(l["help"])
            continue
        if user_id.lower() == "help" and lang == "en":
            print(l["help"])
            continue
        if user_id.lower() == "ajuda" and lang == "br":
            print(l["help"])
            continue
        reason = input(l["reason"])
        try:
            num_reports = int(input(l["num_reports"]))
        except ValueError:
            print(l["invalid_number"])
            continue

        success = 0
        for i in range(num_reports):
            print(l["sending_report"].format(i+1, num_reports))
            if report_user(user_id, reason, cookie, lang, proxies):
                success += 1
            time.sleep(1)
        print(l["reports_sent"].format(success, num_reports))

def show_help(lang):
    print(LANGS[lang]["help"])
    input("\nPresiona Enter para volver al menú...")

def show_read_before(lang):
    print(LANGS[lang]["read_before"])
    input("\nPresiona Enter para volver al menú...")

def open_youtube(lang):
    url = LANGS[lang]["youtube_search"]
    webbrowser.open(url)
    print("Abriendo YouTube...")
    time.sleep(2)

def main_menu(lang):
    l = LANGS[lang]
    while True:
        opt = arrow_menu(
            l["menu_options"],
            title=l["menu_title"],
            author=l["menu_author"]
        )
        if opt == 0:
            auto_reportador(lang)
        elif opt == 1:
            show_help(lang)
        elif opt == 2:
            show_read_before(lang)
        elif opt == 3:
            open_youtube(lang)
        elif opt == 4:
            print(l["goodbye"])
            break

if __name__ == "__main__":
    lang = select_language()
    main_menu(lang)
