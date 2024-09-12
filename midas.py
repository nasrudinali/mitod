import urllib.parse
import urllib.request
import json
from colorama import init, Fore, Style
import time
import datetime
import random
init(autoreset=True)
# Define color variables
RED = Fore.RED + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
MAGENTA = Fore.MAGENTA + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
WHITE = Fore.WHITE + Style.BRIGHT
 

bot_token = "7468313179:AAF0bAZBKbbnX_vuj5DFRH6dFq-WR5iCa5w"
chat_id = "968480911"

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print(f"{Fore.GREEN+Style.BRIGHT}Notification sent successfully.")
            else:
                print(f"{Fore.RED+Style.BRIGHT}Failed to send notification. Status code: {response.status}")
    except Exception as e:
        print(f"{Fore.RED+Style.BRIGHT}Error sending notification: {str(e)}")


def get_headers(access_token=None):
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    }

    if access_token:
        headers["authorization"] = f"Bearer {access_token}"
    return headers

def auth(init_data, retries=3, delay=2):
    url = "https://api-tg-app.midas.app/api/auth/register"
    headers = get_headers()
    body = {
        "initData": init_data,
        "source": 'ref_e73a596d-2dc8-4e40-9697-4c242e438439'
    }
    data = json.dumps(body).encode('utf-8')
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req) as response:
                hasil = response.read().decode('utf-8')
                if response.status == 201:
                    return hasil
                else:
                    print(f"{RED}Error: QUERY INVALID / MATI", flush=True)
                    return None
        except (urllib.error.URLError, ValueError) as e:
            print(f"{RED}Error getting token: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{YELLOW}Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None

def user_detail(access_token, retries=3, delay=2):
    url = f"https://api-tg-app.midas.app/api/user"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))
                if response.status == 200:
                    return response_json
                else:
                    print(f"{RED}Error: Gagal mendapatkan user info", flush=True)
                    return None
        except (urllib.error.URLError, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}User info: Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None
     
def get_tasks(access_token,retries=3,delay=2):
    url = f"https://api-tg-app.midas.app/api/tasks/available"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))
                if response.getcode() == 200:
                    return response_json
                else:
                    print(f"{RED}[ Task ] : Error: Gagal mendapatkan data", flush=True)
                    return None
        except (urllib.error.URLError, ValueError) as e:
            # print(f"{RED}[ Task ] : Error daily_login: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}[ Task ] : Error  Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None

def get_cekin(access_token, retries=3, delay=2):
    url = f"https://api-tg-app.midas.app/api/streak"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))
                if response.getcode() == 200:  # Use getcode() instead of status_code
                    return response_json
                else:
                    print(f"{RED}[ Check-in ] : Error: Gagal mendapatkan data", flush=True)
                    return None
        except (urllib.error.URLError, ValueError) as e:
            if attempt < retries - 1:
                print(f"{RED}[ Check-in ] : Error  Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None

def get_referal(access_token,retries=3,delay=2):
    url = f"https://api-tg-app.midas.app/api/referral/status"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))
            
                if response.getcode() == 200:
                    return response_json
                else:
                    print(f"{RED}[ Check-in ] : Error: Gagal mendapatkan data", flush=True)
                    return None
        except (urllib.error.URLError, ValueError) as e:
            # print(f"{RED}[ Task ] : Error daily_login: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}[ Check-in ] : Error  Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None


def claim_referal(access_token,retries=3,delay=2):
    url = f"https://api-tg-app.midas.app/api/referral/claim"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))  # Parse JSON response before raising for status
                if response.getcode() == 201:
                    return response_json, response.getcode()
                elif response.getcode() == 400:
                    return response_json, response.getcode()
                else:
                    return None, None
        except (urllib.error.URLError, ValueError) as e:
            # print(f"{RED}[ Task ] : Error daily_login: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}[ Referal ] : Error  Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None, None
def claim_cekin(access_token,retries=3,delay=2):
    url = f"https://api-tg-app.midas.app/api/streak"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))# Parse JSON response before raising for status
                if response.getcode() == 201:
                    return response_json, response.getcode()
                elif response.getcode() == 400:
                    return response_json, response.getcode()
                else:
                    return None, None
        except (urllib.error.URLError, ValueError) as e:
            # print(f"{RED}[ Task ] : Error daily_login: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}[ Check-in ] : Error  Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None, None
            
def play_game(access_token,retries=3,delay=2):
    url = f"https://api-tg-app.midas.app/api/game/play"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers,  method='POST')
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))# Parse JSON response before raising for status
                # print(response_json)
                if response.getcode() == 201:
                    return response_json, response.getcode()
                elif response.getcode() == 400:
                    return response_json, response.getcode()
                else:
                    return None, None
        except urllib.error.HTTPError as e:
            print(f"{RED}    ->  Error : {e}", flush=True)
            # print(f"Status Code: {e.code}")
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})",end="\r",  flush=True)
                time.sleep(delay)
            else:
                return None, None
        except (urllib.error.URLError, ValueError) as e:
            print(e.code)
            print(f"{RED}    ->  Error : {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})",end="\r",  flush=True)
                time.sleep(delay)
            else:
                return None, None
            
def process_task(access_token, task_id,retries=3,delay=2):
    url = f"https://api-tg-app.midas.app/api/tasks/start/{task_id}"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))# Parse JSON response before raising for status
                if response.getcode() == 201:
                    return response_json, response.getcode()
                elif response.getcode() == 400:
                    return response_json, response.getcode()
                else:
                    print(f"{RED}    ->  : Error: Gagal mendapatkan data", flush=True)
                    return None, None
        except urllib.error.HTTPError as e:
            print(f"{RED}    ->  Error : {e}", flush=True)
            # print(f"Status Code: {e.code}")
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})",end="\r",  flush=True)
                time.sleep(delay)
            else:
                return None, None
        except (urllib.error.URLError, ValueError) as e:
            print(e.code)
            print(f"{RED}    ->  Error : {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})",end="\r",  flush=True)
                time.sleep(delay)
            else:
                return None, None
 

def claim_task(access_token, task_id, retries=3, delay=2):
    url = f"https://api-tg-app.midas.app/api/tasks/claim/{task_id}"
    headers = get_headers(access_token)
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req) as response:
                response_json = json.loads(response.read().decode('utf-8'))  # Parse JSON response before raising for status
                if response.getcode() == 201:
                    return response_json, response.getcode()
                elif response.getcode() == 400:
                    return response_json, response.getcode()
                else:
                    print(f"{RED}    ->  : Error: Gagal mendapatkan data", flush=True)
                    return None, None
        except urllib.error.HTTPError as e:
            response = e.read().decode('utf-8')  # Decode the byte object
            if e.code == 400:
                return json.loads(response), e.code  # Parse JSON response
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None, None
        except (urllib.error.URLError, ValueError) as e:
            print(f"{RED}    ->  Error : {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None, None
def print_welcome_message():
    print(Fore.WHITE + r"""
          
🆂🅸🆁🅺🅴🅻
          
█▀▀ █▀▀ █▄░█ █▀▀ █▀█ █▀█ █░█ █▀
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▄█ █▄█ ▄█
          """)
    print(Fore.GREEN + Style.BRIGHT + "Midas BOT")
    print(Fore.BLUE + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA\n\n")
  

def main():
    print_welcome_message()
    mode = input(Fore.YELLOW + f"Only Check Balance? (y/n): ").strip().upper()
    while True:                
        total_balance = 0 
        # Read data from query.txt and perform authentication for each line
        with open('query.txt', 'r') as file:
            init_data_lines = file.readlines()
        
        for index, init_data in enumerate(init_data_lines, start=1):
            init_data = init_data.strip()  # Remove any extra whitespace
            if not init_data:
                continue
            print(f"{YELLOW}Getting access token...", end="\r", flush=True)
            access_token = auth(init_data)
            time.sleep(1)
            if access_token is None:
                continue
            user_info = user_detail(access_token)
            print(f"{YELLOW}Getting User info...    ", end="\r", flush=True)
            time.sleep(1)
            if user_info is not None:
                firstname = user_info.get('firstName')
                gameplay = user_info.get('gamesPlayed')
                username = user_info.get('username')
                ticket = user_info.get('tickets')
                balance = user_info.get('points')
                total_accounts = len(init_data_lines)  # Add this line to get the total number of accounts

                print(f"{CYAN}====== Akun ke - {index} dari {total_accounts} | {username} =======            ", flush=True)
                print(f"{CYAN}[ Name ] : {firstname} ", flush=True)
                print(f"{CYAN}[ Gameplayed ] : {gameplay} ", flush=True)
                print(f"{CYAN}[ Ticket ] : {ticket} ", flush=True)
                print(f"{CYAN}[ Balance ] : {balance} ", flush=True)
                total_balance += balance

                if mode == 'y':
                    continue
                ## CHECK-IN =================================================================
                print(f"{YELLOW}[ Check-in ] : Checking..", end="\r", flush=True)
                ghalibie = get_cekin(access_token)
                time.sleep(1)
                if ghalibie is not None:
                    claimable = ghalibie.get('claimable')
                    point_reward = ghalibie.get('nextRewards', {}).get('points', 0)
                    ticket_reward = ghalibie.get('nextRewards', {}).get('tickets', 0)
                    day = ghalibie.get('streakDaysCount')
                    if claimable:
                        print(f"{YELLOW}[ Check-in ] : Day {day} - Reward {point_reward} point and {ticket_reward} ticket. Claiming..", end="\r", flush=True)
                        ghalibie, status_code = claim_cekin(access_token)
                        if ghalibie is not None:
                            if status_code == 201:
                                print(f"{GREEN}[ Check-in ] : Day {day} - Reward {point_reward} point and {ticket_reward} ticket. Claimed!                ", flush=True)
                            else:
                                print(f"{RED}[ Check-in ] : Day {day} - Reward {point_reward} point and {ticket_reward} ticket. Already Claimed!                ", flush=True)
                    else:
                        print(f"{GREEN}[ Check-in ] : Day {day} Already Check-in                ", flush=True)
                ## END CHECK-IN =================================================================
                

                ## PLAY GAME =================================================================
                while ticket > 0:
                    print(f"{YELLOW}[ Game ] : Playing game..", end="\r", flush=True)
                    ghalibie, status_code = play_game(access_token)
                    time.sleep(1)
                    if ghalibie is not None:
                        if status_code == 201:
                            point_game = ghalibie.get('points')
                            print(f"{GREEN}[ Game ] : Success.  Got {point_game} points             ", flush=True)
                            ticket -= 1
                        else:
                            message = ghalibie.get('message')
                            print(f"{RED}[ Game ] : {message}               ", flush=True)
                
                ## END PLAY GAME =================================================================


                ## REFERAL CHECK =================================================================
                print(f"{YELLOW}[ Refferal ] : Checking...", end="\r", flush=True)
                ghalibie = get_referal(access_token)
                if ghalibie is not None:
                    can_claim = ghalibie.get('canClaim')
                    totalpoint = ghalibie.get('totalPoints')
                    ticket = ghalibie.get('totalTickets')
                    if can_claim:
                        print(f"{GREEN}[ Refferal ] : Ready. Reward {totalpoint} point and {ticket} ticket. Claiming..", end="\r", flush=True)
                        ghalibie, status_code = claim_referal(access_token)
                        if ghalibie is not None:
                            if status_code == 201:
                                print(f"{GREEN}[ Refferal ] : Success. Reward {totalpoint} point and {ticket} ticket.                                        ", flush=True)
                            else:
                                print(f"{RED}[ Refferal ] : {ghalibie.get('message')}                                   ", flush=True)
                    else:
                        print(f"{RED}[ Refferal ] : Nothing to claim.                                        ", flush=True)

                ## GET TASK AND CLEAR TASK =================================================================
                print(f"{YELLOW}[ Task ] : Getting Task List..", end="\r", flush=True)
                ghalibie = get_tasks(access_token)
                time.sleep(1)
                if ghalibie is not None:
                    print(f"{YELLOW}[ Task ] : List Task                        ", flush=True)
                    for task in ghalibie:
                        task_id = task.get('id')
                        title = task.get('description')
                        award = task.get('points')
                        isCompleted = task.get('completed')
                        mechanic = task.get('mechanic')
                        if isCompleted == True:
                            print(f"{YELLOW}    -> {title} - {Style.RESET_ALL}{Fore.YELLOW}Point: {award} {GREEN}Completed {Style.RESET_ALL}          ", flush=True)
                            continue
                        
                        if mechanic != 'CHECK_STATUS_CLAIM':
                            ghalibie, status_code = process_task(access_token, task_id)
                        
                            print(f"{YELLOW}    -> {title} - Point: {award} Clearing...{Style.RESET_ALL} ", end="\r", flush=True)
                            time.sleep(2)
                            # print(ghalibie)
                            if ghalibie is not None:
                                # print(task_id,status_code)
                                if status_code == 201:
                                    # print(ghalibie)
                                    state = ghalibie['state']
                                    if state == 'CLAIMABLE':
                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Point: {award} {CYAN}Claiming..{Style.RESET_ALL}                 ", end="\r", flush=True)
                                elif status_code == 400:
                                    message = ghalibie['message']
                                    if 'it is not in a waiting state' in message:
                                        print( f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Point: {award} {GREEN}Already Clear. Claiming..{Style.RESET_ALL}                 ", end="\r", flush=True)
                   
                            ghalibie, status_code = claim_task(access_token, task_id)
                            time.sleep(2)
                            if ghalibie is not None:
                                if status_code == 201:
                                    state = ghalibie['state']
                                    if state == 'COMPLETED':
                                        print(f"{YELLOW}    -> {title} - {Style.RESET_ALL}{Fore.YELLOW} Point: {award} {GREEN}Claimed{Style.RESET_ALL}                                            ", flush=True)
                                elif status_code == 400:
                                    # print(ghalibie)
                                    message = ghalibie['message']
                                    if 'is not in a claimable state' in message:
                                        print( f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Point: {award} {RED}Not Ready to Claim{Style.RESET_ALL}                 ", flush=True)
                                    elif 'cannot be claimed before' in message:
                                        print( f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Point: {award} {CYAN}Pending Claim. Wait Next Loop{Style.RESET_ALL}                 ", flush=True)
                                    else:
                                        print(f"{YELLOW}    -> {title} - {Style.RESET_ALL}{Fore.YELLOW} Point: {award} {GREEN}{ghalibie}{Style.RESET_ALL}          ", flush=True)
                        else:
                            ghalibie, status_code = claim_task(access_token, task_id)
                            time.sleep(2)
                            if ghalibie is not None:
                                if status_code == 201:
                                    state = ghalibie['state']
                                    if state == 'COMPLETED':
                                        print(f"{YELLOW}    -> {title} - {Style.RESET_ALL}{Fore.YELLOW} Point: {award} {GREEN}Claimed{Style.RESET_ALL}                               ", flush=True)
                                elif status_code == 400:
                                    message = ghalibie['message']
                                    if 'is not in a claimable state' in message:
                                        print( f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Point: {award} {RED}Not Ready to Claim{Style.RESET_ALL}                 ", flush=True)
                                    else:
                                        print(f"{YELLOW}    -> {title} - {Style.RESET_ALL}{Fore.YELLOW} Point: {award} {GREEN}{ghalibie}{Style.RESET_ALL}          ", flush=True)
                ## END GET TASK AND CLEAR TASK =================================================================
                                


                                

        
                

           
        
        
        total_accounts = len(init_data_lines) 
    
        message = f"""          
                🔰<b>Midas RWA Report</b>
                
        📁 <b>Total Accounts:</b> {total_accounts}
        🔰 <b>Total Balance:</b> {total_balance:,.0f}
        == Sirkel Generous ==
        """
         
        send_telegram_message(bot_token, chat_id, message)
        print(f"{GREEN}Total Balance from all accounts: {total_balance}{Style.RESET_ALL}")
        print(Fore.BLUE + Style.BRIGHT + f"\n==========SEMUA AKUN TELAH DIPROSES==========\n", flush=True)
        animated_loading(3600)

def animated_loading(duration):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        for frame in frames:
            print(f"\rMenunggu waktu claim berikutnya {frame} - Tersisa {remaining_time} detik         ", end="", flush=True)
            time.sleep(0.25)
    print("\rMenunggu waktu claim berikutnya selesai.                            ", flush=True)
# Execute the main function
if __name__ == "__main__":
    main()
