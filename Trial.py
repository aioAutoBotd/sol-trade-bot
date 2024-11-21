# To test or purchase the source code, contact @SolVolSupp_bot on Telegram
# To test or purchase the source code, contact @SolVolSupp_bot on Telegram
# To test or purchase the source code, contact @SolVolSupp_bot on Telegram


import os
import sys
import winshell
import curses
from win32com.client import Dispatch

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for development and for one-file bundled executables """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def create_shortcut():
    """ Create a shortcut on the desktop """
    source_file = sys.executable

    # Create a shortcut on the desktop
    desktop = winshell.desktop()
    path = os.path.join(desktop, "solvolumefun-1.04.lnk")
    target = source_file
    wDir = os.path.dirname(source_file)
    icon = resource_path("icon.ico")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

def main_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    current_row = 0
    current_menu = "main"

    menu = {
    "main": [
        ("💊 카피-트레이딩", "COPY"),  # COPY-TRADING
        ("🎯 스나이퍼 봇", "army"),   # Snipe Bot
        ("💰 MEV-봇", "pump_strategies"),  # MEV-BOT
        ("⚠️ 월렛 설정", "wallet"),     # Wallet Set
        ("⚙️ 설정", "settings"),        # Settings
        ("❌ 종료", "exit")             # Exit
    ],
    "COPY": [
        ("월렛 추가", "add_wallet"),      # Add wallet
        ("포지션 보기", "positions"),     # View positions
        ("월렛 트래커", "tracker"),       # Wallet tracker
        ("월렛 파서", "parser"),          # Wallet parser
        ("뒤로 가기", "main")             # Back
    ],
    "army": [
        ("스나이퍼 배치 🔫", "deploy_sniper"), # Deploy Sniper
        ("스나이퍼 철수 🔄", "withdraw_sniper"), # Withdraw Sniper
        ("스나이퍼 상태 보기 👀", "view_sniper_status"), # View Sniper Status
        ("뒤로 가기", "main")              # Back
    ],
    "wallet": [
        ("월렛 잔액 보기 💵", "view_balance"), # View Wallet Balance
        ("자금 이체 💸", "transfer_funds"),   # Transfer Funds
        ("월렛 추가 ➕", "add_wallet"),       # Add Wallet
        ("월렛 삭제 ❌", "delete_wallet"),    # Delete Wallet
        ("뒤로 가기", "main")                # Back
    ],
    "pump_strategies": [
        ("샌드위치 공격 🥪", "sandwich"),       # Sandwich Attack
        ("프론트 러닝 🚀", "front_running"),    # Front-running
        ("백 러닝 🏃‍♂️", "back_running"),      # Back-running
        ("차익 거래 💹", "arbitrage"),          # Arbitrage
        ("펌핑 그룹 🚨", "pump_coordination"), # Pump Coordination
        ("뒤로 가기", "main")                  # Back
    ],
    "settings": [
        ("RPC 설정", "rpc"),                 # PRC
        ("뒤로 가기", "main")                # Back
    ],
    "parser": [
        ("월렛 업로드 📤", "upload_a_file"),  # Upload wallets
        ("마이그레이션 파싱", "parse_migrated"), # Parse Migrated
        ("설정 ⚙️", "setparser"),             # Settings
        ("뒤로 가기", "main")                # Back
    ],
    "tracker": [
        ("월렛 추가 ➕", "add_wallet"),         # Add wallet
        ("월렛 관리 🛠️", "mwallet"),          # Manage wallet
        ("멀티 월렛 💼", "muwallet"),          # Multi Wallet
        ("전용 봇 🤖", "dbot"),                # Dedicated bot
        ("그룹 관리 👥", "groups"),            # Groups
        ("알림 🔔", "noti"),                  # Notifications
        ("설정 ⚙️", "settracker"),             # Settings
        ("뒤로 가기", "main")                 # Back
    ],
    "setparser": [
        ("최소 잔액", "min_balance"),          # Min Balance
        ("최대 잔액", "max_balance"),          # Max Balance
        ("최소 WR%", "min_wr"),                # Min WR%
        ("최대 WR%", "max_wr"),                # Max WR%
        ("최소 ROI%", "min_roi"),              # Min ROI%
        ("최대 ROI%", "max_roi"),              # Max ROI%
        ("기간: 30일", "period"),              # Period
        ("최소 거래", "min_trades"),           # Min Trades
        ("최대 거래", "max_trades"),           # Max Trades
        ("MCAP 분포", "mcap_distribution"),   # MCAP Distribution
        ("뒤로 가기", "COPY")                 # Back
    ],
    "settracker": [
        ("🔔 알림 사용자 지정", "custom_notifications"), # Customize notifications
        ("⚠️ 버튼 사용자 지정", "custom_buttons"),      # Customize buttons
        ("⏸️ RAY 일시 중지/재개", "pause_ray"),          # Pause/resume RAY
        ("⛓️ 체인 선택", "select_chains"),              # Select chains
        ("❌ 주소 차단", "block_address"),               # Block address
        ("🖼NFT: ✔️", "nft_toggle"),                   # NFTs
        ("♻️스왑: ✔️", "swaps_toggle"),                 # Swaps
        ("📈구매: ✔️", "buys_toggle"),                  # Buys
        ("📉판매: ✔️", "sells_toggle"),                 # Sells
        ("✏️첫 구매만: ❌", "first_buy_toggle"),         # First Buy Only
        ("🔋최소 거래 SOL: 0", "min_trade_sol"),         # Min trade SOL
        ("🪫최대 거래 SOL: 0", "max_trade_sol"),         # Max trade SOL
        ("🛡토큰 민트: ✔️", "token_mint_toggle"),         # Token mint
        ("🔋최소 SOL 전송: 0", "min_sol_transfer"),       # Min SOL transfer
        ("🪫최대 SOL 전송: 0", "max_sol_transfer"),       # Max SOL transfer
        ("💸최소 토큰 전송 USD: 0", "min_token_transfer_usd"), # Min token transfer USD
        ("📤토큰 전송: ✔️", "token_transfers_toggle"),    # Token transfers
        ("🖼cNFT: ✔️", "cnfts_toggle"),                 # cNFTs
        ("DRiP: ✔️", "drip_toggle"),                   # DRiP
        ("🔥소각: ✔️", "burn_toggle"),                  # Burn
        ("✅승인: ✔️", "approvals_toggle"),             # Approvals
        ("팁: ❌", "tips_toggle"),                      # Tips
        ("☄️Jupiter: ✔️", "jupiter_toggle"),           # Jupiter
        ("☄️Jupiter DCA: ✔️", "jupiter_dca_toggle"),   # Jupiter DCA
        ("☄️Jupiter Perps: ✔️", "jupiter_perps_toggle"), # Jupiter Perps
        ("💊PumpFun: ✔️", "pumpfun_toggle"),           # PumpFun
        ("🧬Raydium: ✔️", "raydium_toggle"),           # Raydium
        ("수신: ✔️", "incoming_toggle"),                # Incoming
        ("송신: ✔️", "outgoing_toggle"),                # Outgoing
        ("뒤로 가기", "tracker")                       # Back
    ]
}

    title = [
" /      \ /      \|  \     |  \   |  \/      \|  \     |  \  |  \  \     /  \        \ ",
"|  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓     | ▓▓   | ▓▓  ▓▓▓▓▓▓\ ▓▓     | ▓▓  | ▓▓ ▓▓\   /  ▓▓ ▓▓▓▓▓▓▓▓ ",
"| ▓▓___\▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓   | ▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓▓\ /  ▓▓▓ ▓▓__     ",
" \▓▓    \| ▓▓  | ▓▓ ▓▓      \▓▓\ /  ▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓▓▓\  ▓▓▓▓ ▓▓  \    ",
" _\▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓       \▓▓\  ▓▓| ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓\▓▓ ▓▓ ▓▓ ▓▓▓▓▓    ",
"|  \__| ▓▓ ▓▓__/ ▓▓ ▓▓_____   \▓▓ ▓▓ | ▓▓__/ ▓▓ ▓▓_____| ▓▓__/ ▓▓ ▓▓ \▓▓▓| ▓▓ ▓▓_____ ",
" \▓▓    ▓▓\▓▓    ▓▓ ▓▓     \   \▓▓▓   \▓▓    ▓▓ ▓▓     \\ ▓▓    ▓▓ ▓▓  \▓ | ▓▓ ▓▓     \ ",
"  \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓    \▓     \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓      \▓▓\▓▓▓▓▓▓▓▓ "
     ]

    def print_menu(stdscr, selected_row_idx):
        stdscr.clear()
        # Print the title
        for i, line in enumerate(title):
            stdscr.addstr(i, 0, line, curses.color_pair(5))
        stdscr.addstr(len(title) + 1, 0, "개발자: solvolume.fun", curses.color_pair(2))
        stdscr.addstr(len(title) + 2, 0, "메뉴", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(len(title) + 3, 0, "화살표 키를 사용하세요. 확인하려면 Enter 키를 누르세요.", curses.color_pair(2))

        # Print the menu
        current_menu_items = menu[current_menu]
        for idx, item in enumerate(current_menu_items):
            x = 0
            y = idx + len(title) + 5
            if idx == selected_row_idx:
                stdscr.addstr(y, x, item[0], curses.color_pair(3))
            else:
                stdscr.addstr(y, x, item[0])
        stdscr.refresh()

    # Implementation of license key prompt, and other functionalities that are part of the original structure remain intact.

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlighted menu item
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Title color
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Subtitle color
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Bright green title color

    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu[current_menu]) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_item = menu[current_menu][current_row]
            if selected_item[1] == "exit":
                break
            elif selected_item[1] == "main":
                current_menu = "main"
                current_row = 0
            elif selected_item[1] in menu:
                current_menu = selected_item[1]
                current_row = 0
            else:
                prompt_license_key(stdscr)
        print_menu(stdscr, current_row)

if __name__ == "__main__":
    create_shortcut()
    curses.wrapper(main_menu)

# To test or purchase the source code, contact @SolVolSupp_bot on Telegram