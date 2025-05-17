# ╔════════════════════════════════════════════════════════════╗
# ║        AUTO REPORTADOR DE USUARIOS PARA ROBLOX            ║
# ║      Instalación automática de dependencias y uso fácil    ║
# ║        Contacto: Discord @bochisline                      ║
# ╚════════════════════════════════════════════════════════════╝

import sys
import subprocess
import os
import time

# Auto-instalación de dependencias
try:
    import requests
except ImportError:
    print("Instalando dependencias necesarias...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

import webbrowser

# Diccionario de idiomas
LANGS = {
    "es": {
        "banner": """
╔════════════════════════════════════════════════════════════╗
║        AUTO REPORTADOR DE USUARIOS PARA ROBLOX            ║
║      Instalación automática de dependencias y uso fácil    ║
║        Contacto: Discord @bochisline                      ║
╚════════════════════════════════════════════════════════════╝
""",
        "menu_title": "=== Menú Principal ===",
        "menu_1": "1) Auto reportador (ingresar usuario)",
        "menu_2": "2) Ayuda para obtener cookie",
        "menu_3": "3) Salir",
        "menu_4": "4) ¿Necesitas más ayuda? (YouTube)",
        "select_option": "Selecciona una opción: ",
        "invalid_option": "Opción no válida. Intenta de nuevo.",
        "exit": "Saliendo...",
        "help_title": "\n=== Ayuda para obtener tu cookie .ROBLOSECURITY ===",
        "help_1": "1. Inicia sesión en https://www.roblox.com/ en tu navegador.",
        "help_2": "2. Presiona F12 para abrir las herramientas de desarrollador.",
        "help_3": "3. Ve a la pestaña 'Application' o 'Aplicación'.",
        "help_4": "4. Busca 'Cookies' en el menú izquierdo y selecciona 'https://www.roblox.com'.",
        "help_5": "5. Copia el valor de la cookie llamada '.ROBLOSECURITY'.",
        "help_6": "6. Pega ese valor cuando el programa lo solicite o en el archivo cookie.txt.\n",
        "help_7": "7. ¿Necesitas más ayuda? Escribe 'mas' para ver tutoriales en YouTube.",
        "cookie_not_found": "No se encontró cookie.txt. Por favor, pega tu .ROBLOSECURITY cookie a continuación:",
        "cookie_saved": "Cookie guardada en cookie.txt.",
        "user_id": "ID del usuario a reportar (o 'volver'): ",
        "reason": "Razón del reporte: ",
        "num_reports": "¿Cuántos reportes deseas enviar?: ",
        "invalid_number": "Número inválido.",
        "sending_report": "Enviando reporte {}/{}...",
        "reports_sent": "Reportes enviados exitosamente: {}/{}\n",
        "report_error": "Error al reportar usuario {}: {} {}",
        "connection_error": "Error de conexión: {}",
        "back": "volver"
    },
    "en": {
        "banner": """
╔════════════════════════════════════════════════════════════╗
║        ROBLOX USER AUTO REPORTER                         ║
║   Automatic dependency installation and easy to use       ║
║        Contact: Discord @bochisline                      ║
╚════════════════════════════════════════════════════════════╝
""",
        "menu_title": "=== Main Menu ===",
        "menu_1": "1) Auto reporter (enter user)",
        "menu_2": "2) Help to get cookie",
        "menu_3": "3) Exit",
        "menu_4": "4) Need more help? (YouTube)",
        "select_option": "Select an option: ",
        "invalid_option": "Invalid option. Try again.",
        "exit": "Exiting...",
        "help_title": "\n=== Help to get your .ROBLOSECURITY cookie ===",
        "help_1": "1. Log in to https://www.roblox.com/ in your browser.",
        "help_2": "2. Press F12 to open developer tools.",
        "help_3": "3. Go to the 'Application' tab.",
        "help_4": "4. Look for 'Cookies' in the left menu and select 'https://www.roblox.com'.",
        "help_5": "5. Copy the value of the cookie named '.ROBLOSECURITY'.",
        "help_6": "6. Paste that value when the program asks or in the cookie.txt file.\n",
        "help_7": "7. Need more help? Type 'more' to see YouTube tutorials.",
        "cookie_not_found": "cookie.txt not found. Please paste your .ROBLOSECURITY cookie below:",
        "cookie_saved": "Cookie saved in cookie.txt.",
        "user_id": "User ID to report (or 'back'): ",
        "reason": "Report reason: ",
        "num_reports": "How many reports do you want to send?: ",
        "invalid_number": "Invalid number.",
        "sending_report": "Sending report {}/{}...",
        "reports_sent": "Reports sent successfully: {}/{}\n",
        "report_error": "Error reporting user {}: {} {}",
        "connection_error": "Connection error: {}",
        "back": "back"
    }
}

def seleccionar_idioma():
    print("Seleccione idioma / Select language:")
    print("1) Español")
    print("2) English")
    while True:
        op = input("Opción / Option: ").strip()
        if op == "1":
            return "es"
        elif op == "2":
            return "en"
        else:
            print("Opción no válida / Invalid option.")

def mostrar_ayuda(lang):
    l = LANGS[lang]
    print(l["help_title"])
    print(l["help_1"])
    print(l["help_2"])
    print(l["help_3"])
    print(l["help_4"])
    print(l["help_5"])
    print(l["help_6"])
    print(l["help_7"])
    extra = input("¿Quieres ver tutoriales en YouTube? (escribe 'mas'/'more' o Enter para volver): ").strip().lower()
    if extra in ["mas", "more"]:
        print("Abriendo YouTube con la búsqueda: 'como encontrar robloxsecurity cookie'...")
        webbrowser.open("https://www.youtube.com/results?search_query=como+encontrar+robloxsecurity+cookie")

def load_cookie(lang, cookie_file="cookie.txt"):
    l = LANGS[lang]
    if not os.path.exists(cookie_file):
        print(l["cookie_not_found"])
        cookie = input("Cookie: ").strip()
        with open(cookie_file, "w") as f:
            f.write(cookie)
        print(l["cookie_saved"])
        return cookie
    else:
        with open(cookie_file, "r") as f:
            return f.read().strip()

def report_user(user_id, reason, cookie, lang):
    l = LANGS[lang]
    url = "https://www.roblox.com/abusereport/submit"  # Puede no ser válido
    headers = {
        "Cookie": f".ROBLOSECURITY={cookie}",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    data = {
        "targetUserId": user_id,
        "reason": reason,
        "comment": "Reporte automático" if lang == "es" else "Automatic report"
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        if response.status_code == 200:
            return True
        else:
            print(l["report_error"].format(user_id, response.status_code, response.text))
            return False
    except Exception as e:
        print(l["connection_error"].format(e))
        return False

def menu(lang):
    l = LANGS[lang]
    while True:
        print(l["banner"])
        print(l["menu_title"])
        print(l["menu_1"])
        print(l["menu_2"])
        print(l["menu_4"])
        print(l["menu_3"])
        print("═════════════════════════════════════════════════════════════")
        print(" Discord @bochisline")
        print("═════════════════════════════════════════════════════════════")
        opcion = input(l["select_option"]).strip()
        if opcion == "1":
            auto_reportador(lang)
        elif opcion == "2":
            mostrar_ayuda(lang)
        elif opcion == "4":
            print("Abriendo YouTube con la búsqueda: 'como encontrar robloxsecurity cookie'...")
            webbrowser.open("https://www.youtube.com/results?search_query=como+encontrar+robloxsecurity+cookie")
        elif opcion == "3":
            print(l["exit"])
            break
        else:
            print(l["invalid_option"])

def auto_reportador(lang):
    l = LANGS[lang]
    cookie = load_cookie(lang)
    while True:
        user_id = input(l["user_id"])
        if user_id.lower() == l["back"]:
            break
        reason = input(l["reason"])
        try:
            num_reports = int(input(l["num_reports"]))
        except ValueError:
            print(l["invalid_number"])
            continue

        success = 0
        for i in range(num_reports):
            print(l["sending_report"].format(i+1, num_reports))
            if report_user(user_id, reason, cookie, lang):
                success += 1
            time.sleep(1)  # Espera 1 segundo entre reportes para evitar bloqueos

        print(l["reports_sent"].format(success, num_reports))

if __name__ == "__main__":
    idioma = seleccionar_idioma()
    menu(idioma)
