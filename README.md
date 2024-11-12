<h1 align="center"> Solana Trading Bot </h1>

Solana Trading Ultimate! Copy trading bot, wallet analyzer, tracker bot, volume bot, sniper bot, MEV bot - all in one AIO solution!

![KR](https://github.com/user-attachments/assets/6bb546c9-3f49-4b28-b5a8-5cc5f2be0307)

# Parser/Analyzer Wallets  
![line](https://github.com/user-attachments/assets/e22f0971-b76d-4c90-acb7-fc9a0cda5d4c)

## **기능:**  
1. **계약 데이터를 빠르게 파싱하여 분석 가능.**  
2. **무제한의 지갑 및 계약 데이터 파싱 지원.**  
3. **다양한 필터링 옵션을 통해 원하는 데이터만 추출.**  
4. **자동으로 Excel 파일 생성으로 실시간 모니터링 가능.**  

![excel](https://github.com/user-attachments/assets/4d70e408-13c4-479c-bd46-8e66e3479fac)

- **최대 빠른 거래** - 1분 미만의 빠른 거래 최대 횟수  
- **최소 로켓 비율** - +100% 이익으로 종료된 거래 최소 비율  
- **지갑 연령** - 지갑 생성 후 X일 ~ Y일  
- **MCAP 분포** - 특정 시가총액 범위 내 거래 비율  
- **필터 비활성화** - 필터 없이 모든 데이터를 포함한 파일 생성  
- **연결된 지갑** - SOL 전송과 관련된 연결 지갑 로깅  
- **승률 정렬** - 승률/ROI 기준 상위 지갑부터 정렬  
- **구매 데이터 표시** - 파싱된 지갑의 토큰 구매 내역 포함  
- **빠른 거래 비율** - 1분 미만의 거래 비율  
- **매도량 > 매수량** - 실질 PNL 및 ROI 왜곡을 방지  
- **중간 ROI** - 중간 ROI 계산  
- **로켓 비율** - +100% 이상의 수익 거래 비율  
- **평균 거래 시간**  

*Photon에서 토큰 주소를 입력하고 거래자의 지갑을 지정하여 각 거래를 세부적으로 분석할 수 있습니다. 모든 지갑 목록으로 돌아가려면 테이블 오른쪽 상단의 "뒤로가기" 버튼을 클릭하세요.*  

---

# Tracker Wallets  
```
 "tracker": [
        ("월렛 추가 ➕", "add_wallet"),         # Add wallet
        ("월렛 관리 🛠️", "mwallet"),          # Manage wallet
        ("멀티 월렛 💼", "muwallet"),          # Multi Wallet
        ("전용 봇 🤖", "dbot"),                # Dedicated bot
        ("그룹 관리 👥", "groups"),            # Groups
        ("알림 🔔", "noti"),                  # Notifications
        ("설정 ⚙️", "settracker"),             # Settings
```
- **트래커를 통해 복사 중인 지갑의 모든 거래를 추적하며, 직관적이고 상세한 인터페이스 제공.**

### **거래 필터**
- NFT, 스왑, 전송, 기타 거래를 포함하거나 제외하는 옵션을 선택할 수 있습니다.  
```
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
```
---

# 소개  
![line](https://github.com/user-attachments/assets/e22f0971-b76d-4c90-acb7-fc9a0cda5d4c) 

**SolVolume**은 Raydium, PUMP.FUN, MOONSHOT과 같은 솔라나 기반 플랫폼을 사용하여 거래 전략을 자동화합니다.  
- 이더리움에서 솔라나로 거래 활동이 이동하는 트렌드를 포착하여, 몇 달 간의 조용한 개발 끝에 **SolVolumeBot**을 선보입니다.  
- 솔라나에서의 트레이딩 전략을 한 단계 끌어올릴 수 있는 강력한 도구입니다.  

---

# V1.2.7 주요 기능  

1. **💎 볼륨 봇**: SOL 매수 범위 및 지연 시간 설정으로 자연스러운 거래 볼륨 생성.  
2. **🎯 스나이퍼 봇**: 서브 지갑으로 대량 구매를 지원하며, 특정 지갑이 민팅한 새 토큰을 빠르게 감지.  
3. **💲 토큰 생성기**: PUMP.FUN과 Raydium에서 토큰 발행 지원, 지갑 할당 및 스나이핑 보호 제공.  
4. **⚠️ 지갑 세팅**: 마스터 지갑과 서브 지갑 설정을 통해 수수료, 우선 순위, 슬리피지 관리 가능.  
5. **📊 유동성 관리**: Raydium 또는 Orca 플랫폼에서 유동성 풀 생성 및 제거 지원.  
6. **🔄 시장 조성 및 거래 봇**: 스왑 및 대량 스왑 도구 제공, 유동성 보장 및 스프레드 최적화.  
7. **📦 대량 작업**: 다수의 지갑 생성 및 토큰 대량 전송 기능 제공.  
8. **💰 펌프 전략**: 펌프 전략 툴 제공, 마이크로 트레이딩 지원.  
9. **📜 유용한 도구**: 특정 블록 높이에서 토큰 스냅샷, WSOL 교환 도구 추가.  
10. **⚙️ 설정**: 언어 변경, 소프트웨어 업데이트, 로그 확인 가능.  

---

## ✅ **1시간 무료 체험 제공!** ✅  

[![Custom Button](https://img.shields.io/badge/클릭-웹사이트-blue?style=for-the-badge)](https://solvolume.fun)  
[![Custom Button](https://img.shields.io/badge/가격-blue?style=for-the-badge)](https://solvolume.fun/#carousel_7e48)  
[![FAQ](https://img.shields.io/badge/FAQ-blue?style=for-the-badge)](https://solvolume.fun/FAQ.html)  

---

### 체험 버전 사용 방법:
1. **웹사이트에서 "FREE TRIAL" 클릭 후 키를 얻으세요.**  
2. **키를 복사하고 "TAKE ADVANTAGE" 클릭.**  
3. **키를 입력하고 봇 다운로드.**

---

> **💡 TIP**  
> 이해하기 어려운 부분이 있다면, [저희에게 연락하세요!](https://t.me/SolVolSupp_bot)
